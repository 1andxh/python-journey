spam = {'color':'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

# list(spam.keys())
for k, v in spam.items():
    print(f"key: {k} Value: {str(v)}")


# checking whether a key or value exists i dictionary
register = {'name': 'zophie', 'age': 7, 'sex': 'male'}
print('name' in register.keys())
print('zophie' in register.values())
print('color'  in register.keys())

# the get() method
picnicItems = {'apples': 5, 'cups': 2}
print(f"i am bringing {str(picnicItems.get('cups', 0))} cups")
print(f"i am bringing {str(picnicItems.get('eggs', 0))} eggs")


# the setdefault() method
books = {'name': 'pooka', 'cabinet': 5}
if 'color' not in books:
    books['color']='black'

print(books.setdefault('color','black'))


# setdefault
message = 'it was a bright cold  day in april, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)


