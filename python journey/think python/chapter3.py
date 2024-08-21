# functions

# exercise 3.1
""" Write a function named right_justify that takes a string named s as a parameter
 and prints the string with enough leading spaces so that the last letter of the string is in column 70
 of the display"""
def right_justify(s):
    spaces = 70 - len(s)
    print(' ' * spaces + s)

right_justify('monty')

# exercise 3.2

def do_twice(f,value):
    f(value)
    f(value)

def print_twice(string):
    print(string)
    print(string)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
print('do twice:\n')
do_twice(print_twice, 'spam')
print('do four: \n')
do_four(print, 'spam')


# exerice 3.3
def print_separator():
    print('+', (' -' * 4), '+', (' -' * 4), '+')

def print_rows():
    for _ in range(4):
        print('|', ' ' * 8, '|', ' ' * 8, '|')

def grid():
    print_separator()
    print_rows()
    print_separator()
    print_rows()
    print_separator()

grid()

def big_grid():
    grid()
    
big_grid()