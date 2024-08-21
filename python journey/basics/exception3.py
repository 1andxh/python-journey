class Error(Exception):
    # base class for other exceptioins
    pass

# custom error to inherit from error class
class EmptyFileError(Error):
    pass

try:
    thefile = open('customers-100.csv')
    line_count = len(thefile.readlines)
    if line_count > 2:
        raise EmptyFileError
    
except FileNotFoundError:
    print('\nFile not found')

# handle custom errors for too few rows
except EmptyFileError:
    print('\n file name: customers-100.csv is empty')

# handle all other exceptions
except Exception as e:
    print('\n\nFailed: the error was ' + str(e))
    thefile.close

else:
    print()

    # file must be open by now if its passed all this
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("good")