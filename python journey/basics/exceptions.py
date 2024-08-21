# def main():
#     get_int()

# def get_int():
#     while True:
#         try:
#             x = int(input("x: "))
#         except ValueError:
#             print("x not an integer")

#         else:
#             break

#     # print(f"x is {x}")
#     return x

# main()

try:
    # open the file
    thefile = open('customers-100.csv')
    # watch for common error and stop program if it happens
except FileNotFoundError:
    print("sorry, i don't see a file named customers-100.csv")
    # catch any unexpected error and stop program if one happen
except Exception as err:
    print(err)
    # otherwise, if nothing bad has happened by now, just keep going
else:
    # file must be open by now
    print("\n")

    # print each line from file
    for each_line in thefile:
        print(each_line)
    thefile.close()
    print("all good!")

