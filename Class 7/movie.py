personAge = int(input("Enter Age here: "))
basePrice = 200
studentDiscount = 0
student = input("Are you a student? Yes or no?: ")
childDiscount = 0
if personAge < 12:
    childDiscount = basePrice * 50/100
if student == "Yes":
    studentDiscount = basePrice * 20/ 100

finalPrice = basePrice - childDiscount - studentDiscount

print(f"""
        1. basePrice: {basePrice}
        2. childDiscount: {childDiscount}
        3. studentDiscount: {studentDiscount}
        4. finalPrice {finalPrice}


""")



