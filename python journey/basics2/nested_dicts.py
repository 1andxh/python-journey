allGuests = {
    'Kofi': {'apples': 5, 'bofrot': 7},
    'Yaa': {'cakes': 10, 'boba': 6},
    'Harry': {'cups': 4, 'wings': 15}
}

def stuff_brought(guests, items):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(items, 0)
    return num_brought
    
print('Number of things brought:')
print(f"- apples\t  {stuff_brought(allGuests, 'apples')}")
print(f"- bofrot\t  {stuff_brought(allGuests, 'bofrot')}")
print(f"- cakes \t  {stuff_brought(allGuests, 'cakes')}")
print(f"- boba  \t  {stuff_brought(allGuests, 'boba')}")
print(f"- cupsn \t  {stuff_brought(allGuests, 'cups')}")
print(f"- wings \t  {stuff_brought(allGuests, 'wings')}")


# dictionary = {'foo': 42}
# print(dictionary)
spam = {'bar':100}
print(spam['foo'])