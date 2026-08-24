basePrice = 300
dataUsage = int(input("Enter data usage here: "))
primeUser = input(" are you a Prime user? Yes or No?: ")
overUsage = 0
primeDiscount = 0
if dataUsage > 5:
    overUsage = basePrice + 50
if primeUser == "Yes":
    primeDiscount = basePrice * 10/100

totalPrice = basePrice + overUsage - primeDiscount
print(f"""
        1.  basePrice: {basePrice}
        2.  primeDiscount:{primeDiscount}
        3.  total(with overUsage or not): {totalPrice}
        


""")
