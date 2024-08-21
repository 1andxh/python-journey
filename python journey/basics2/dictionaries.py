myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}
print(myCat['size'])

print('my cat has ' + myCat['color'] + ' fur')

spam = {1234: 'luggage combination', 42: 'the answer'}


birthdays = {'Alice': 'May 1 ', 'Paa':'Aug 13 ', 'Nii': 'Mar 4 '}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name.casefold() in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('i do not have birthday information for ' + name)
        print('what is their birthday?')
        date = input()
        birthdays[name] = date
        print('birthday database updated') 