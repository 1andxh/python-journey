try:
    thefile = open('customers-100.csv')
    line_count = len(thefile.readlines())

    if line_count > 2:
        raise Exception

# handle missing file error
except FileNotFoundError:
    print('\nfile cannot be found')

# handle all other exceptions
except Exception as e:
    print('\nFailed: The error was ' + str(e))
    thefile.close