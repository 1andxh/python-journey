import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyberbullying Awareness Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)


font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
medium_font = pygame.font.Font(None, 48)
intermediate_font = pygame.font.Font(None, 58)


click_sound = pygame.mixer.Sound("click.wav")
correct_sound = pygame.mixer.Sound("correct.wav")
wrong_sound = pygame.mixer.Sound("wrong.wav")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.2)


questions = [
    {
        "question": "What should you do if someone sends you a hurtful message online?",
        "options": ["Reply with a hurtful message", "Ignore it and report it", "Share it with friends", "Delete your account"],
        "correct": 1
    },
    {
        "question": "What is a safe way to handle a cyberbully?",
        "options": ["Confront them in person", "Block and report them", "Ignore it and hope it stops", "Share your password with friends for support"],
        "correct": 1
    },
    {
        "question": "If you witness someone being cyberbullied, what can you do to help?",
        "options": ["Join in to not be targeted", "Report the behavior and offer support", "Ignore it", "Share the bullying posts to raise awareness"],
        "correct": 1
    },
    {
        "question": "What should you avoid sharing on social media to protect your privacy?",
        "options": ["Your favorite movie", "Personal information like your address", "Pictures of your pet", "Your hobbies"],
        "correct": 1
    },
    {
        "question": "What is a good first step if you are being bullied online?",
        "options": ["Ignore it", "Block the bully and report them", "Retaliate with mean comments", "Delete your account"],
        "correct": 1
    }
]


tips = [
    "Always use strong and unique passwords for your online accounts.",
    "Never share personal information with strangers online.",
    "Report any cyberbullying incidents to the platform and seek help from a trusted adult.",
    "Block and report users who send you harmful or unwanted messages.",
    "Keep evidence of cyberbullying messages or posts in case you need to report them.",
    "Adjust your privacy settings on social media to limit who can see your posts.",
    "Think before you post. Once something is online, it can be hard to remove.",
    "Do not respond to bullies. It can escalate the situation.",
    "Talk to someone you trust if you are being bullied online.",
    "Educate yourself on the signs of cyberbullying to better protect yourself and others."
    "Avoid engaging with the bully.",
    "Take screenshots and save any messages or posts that are hurtful.",
    "Use the platform’s tools to block and report the bully.",
    "Adjust your privacy settings to limit who can contact you.",
    "Reach out to friends, family, or a counselor.",
    "Consider speaking with a mental health professional.",
    "Online or in-person groups can offer understanding and advice."
]



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_button(text, x, y, width, height, color, hover_color):
    mx, my = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    if button_rect.collidepoint((mx, my)):
        pygame.draw.rect(screen, hover_color, button_rect)
    else:
        pygame.draw.rect(screen, color, button_rect)
    draw_text(text, font, WHITE, screen, x + 20, y + 10)
    return button_rect

def draw_text_wrapped(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        test_rect = font.render(test_line, True, color).get_rect()
        if test_rect.width <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    lines.append(' '.join(current_line))

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * font.get_linesize()))

def ask_question(question_data, question_index):
    click = False
    answer_buttons = []
    button_rects = []
    paused = False

    while True:
        screen.fill(BLACK)
        draw_text_wrapped(f"{question_index + 1}: {question_data['question']}", intermediate_font, WHITE, screen, 20, 20, WIDTH - 40)


        button_y = 150
        button_height = 50
        button_width = WIDTH - 100

        for i, option in enumerate(question_data["options"]):
            button_rect = draw_button(option, 50, button_y, button_width, button_height, BLUE, GREEN)
            button_rects.append(button_rect)
            button_y += button_height + 10


        pause_button_rect = draw_button("Pause", WIDTH - 150, HEIGHT - 70, 100, 50, BLUE, GREEN)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if click:
            mx, my = pygame.mouse.get_pos()
            if pause_button_rect.collidepoint((mx, my)):
                click_sound.play()
                paused = True

        if paused:
            paused = show_pause_menu()
            if not paused:
                continue

        if click:
            mx, my = pygame.mouse.get_pos()
            for i, button_rect in enumerate(button_rects):
                if button_rect.collidepoint((mx, my)):
                    click_sound.play()
                    if i == question_data["correct"]:
                        correct_sound.play()
                        return True
                    else:
                        wrong_sound.play()
                        return False

        pygame.display.update()

def show_pause_menu():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text("Game Paused", large_font, WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 - 150)
        button_resume = draw_button("Resume", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, BLUE, GREEN)
        button_quit = draw_button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, BLUE, GREEN)

        mx, my = pygame.mouse.get_pos()
        if button_resume.collidepoint((mx, my)) and click:
            click_sound.play()
            return False
        if button_quit.collidepoint((mx, my)) and click:
            click_sound.play()
            return main()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

def show_tips():
    click = False
    tip = random.choice(tips)
    while True:
        screen.fill(BLACK)
        draw_text('Tips to Help Victims', large_font, WHITE, screen, 20, 20)
        draw_text_wrapped(tip, font, WHITE, screen, 20, 80, WIDTH - 40)
        button_back = draw_button('Main Menu', 50, 500, 200, 50, BLUE, GREEN)
        mx, my = pygame.mouse.get_pos()
        if button_back.collidepoint((mx, my)) and click:
            click_sound.play()
            return
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()



def end_game(score, total_questions):
    click = False
    if score == total_questions:
        message = f'Congratulations! Your score: {score}'
        button_text = 'Next Level'
    else:
        message = f'Game Over! Your score: {score}'
        button_text = 'Retry'

    while True:
        screen.fill(BLACK)
        draw_text(message, large_font, WHITE, screen, 20, 20)
        button_action = draw_button(button_text, 50, 100, 200, 50, BLUE, GREEN)
        button_main_menu = draw_button('Main Menu', 50, 200, 200, 50, BLUE, GREEN)
        mx, my = pygame.mouse.get_pos()
        if button_action.collidepoint((mx, my)) and click:
            click_sound.play()
            return 'retry'  
        if button_main_menu.collidepoint((mx, my)) and click:
            click_sound.play()
            return 'main_menu'

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def main_menu():
    click = False
    while True:
        screen.fill(BLACK)
        draw_text('CyberShield', large_font, WHITE, screen, 20, 20)
        button_start = draw_button('Start Game', 50, 100, 200, 50, BLUE, GREEN)
        button_tips = draw_button('Tips', 50, 200, 200, 50, BLUE, GREEN)
        button_exit = draw_button('Exit', 50, 300, 200, 50, BLUE, RED)

        mx, my = pygame.mouse.get_pos()
        if button_start.collidepoint((mx, my)) and click:
            click_sound.play()
            return 'start_game'
        if button_tips.collidepoint((mx, my)) and click:
            click_sound.play()
            return 'show_tips'
        if button_exit.collidepoint((mx, my)) and click:
            click_sound.play()
            pygame.quit()
            exit()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


def game_loop():
    score = 0
    total_questions = len(questions)
    random.shuffle(questions)  # Shuffle the questions before starting the game
    for i, question in enumerate(questions):
        correct = ask_question(question, i)
        if not correct:
            break
        score += 1
    action = end_game(score, total_questions)
    if action == 'retry':
        game_loop()
    elif action == 'main_menu':
        main()

def main():
    while True:
        action = main_menu()
        if action == 'start_game':
            game_loop()
        elif action == 'show_tips':
            show_tips()

if __name__ == "__main__":
    main()



