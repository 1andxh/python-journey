def print_lyrics():
    print("i'm a lumberjack, and i'm okay")
    print("i sleep all night and work all day")


# print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# repeat_lyrics()
    

"""Parameters and arguments"""
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('spam '*3)
print_twice(42)