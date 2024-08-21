# x = int(input("what's x? "))

# if x % 2 == 0:
#     print("even")
# else:
#     print("odd")

# n = 1
# while n < 14:
#     if (n % 2 == 0):
#         print(n, 'is even')
#     else:
#         print(n, 'is odd')
#     n += 1

def main():
    x = int(input('enter number: '))
    if is_even(x):
        print("even")
    else:
        print('odd')

def is_even(n):
        # if n % 2 == 0:
        #     return True
        # else:
        #     return False
    return True if n % 2 == 0 else False


main()