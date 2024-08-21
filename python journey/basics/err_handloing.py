# try:
#  try to do this
# except:
#  if x happens, stop here
# except Exception as e:
#  if something else bad happens, stop here
# else:
#  if no exceptions, continue on normally here
# finally:
#  do this code no matter what happened above
# def main():
#     get_int()
   

def get_int():
        while True:
            try:
                x = int(input("what is x? "))
            except ValueError:
                print("x is not an integer")
            finally:
                 if input == int:
                      break
       
            
           
get_int()
# if __name__ == "main":
#     main()