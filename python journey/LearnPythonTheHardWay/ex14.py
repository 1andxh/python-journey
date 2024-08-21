# prompting and passing
from sys import argv

script, username = argv
prompt = '> '

print(f"hi {username}, i'm the {script} script.")
print(f"i'd like to ask you a few aquestions.")
print(f"do you like me {username}?")
likes =input(prompt)

print(f"where do you live {username} ?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer} computer. nice!!
""")

# type python3.12 ex14.py (username)