# names, variables, code, funtions

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# args is kind of pointless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("first!")
print_none()
