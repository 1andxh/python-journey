def main():
    print_row(4)
    print_squares(5)


def print_row(width):
    print("?" * width, sep=" ")

def print_squares(size):
    # for each row in square 
    for i in range(size):
        print("[] "* size)



       


    



main()