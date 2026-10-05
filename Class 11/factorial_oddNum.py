n = int(input("Enter Here: "))
product = 1

for i in range(1, n+1):
    if(i % 2 == 1):
        product = product * i

print(product)
