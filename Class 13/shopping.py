cart = []

for i in range(6):
    item = input("Enter an item: ")
    cart.append(item)

print(cart)

for i in range(3):
    item = input("Which item do you want to remove?: ")
    cart.remove(item)

print(cart)