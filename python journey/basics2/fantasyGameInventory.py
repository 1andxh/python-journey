inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print("Inventory:")

def displayInventory(inventory):
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(inventory)

# list to dictionary function

inv= {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inv, addedIems):
    
    print('your new inventory is: ')
    for item in addedIems:
        inv[item] = inv.get(item, 0) + 1

addToInventory(inv,dragonLoot)
displayInventory(inv)
    
