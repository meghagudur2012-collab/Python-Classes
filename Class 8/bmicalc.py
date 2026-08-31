weight = int(input("Enter weight here: "))
height = float(input("Enter height here: "))

BMI = weight / (height * height)
category = " "

if BMI < 18.5:
    category = "Underweight"

elif BMI <= 24.9 and BMI >= 18.5:
    category = "Normal Weight"

elif BMI <= 29.9 and BMI >= 25:
    category = "Over Weight"

elif BMI >= 30:
    category = "Obese"

elif height <= 0 or weight <= 0:
    print("Invalid input. Weight and height must be greater than 0.")

print(f"""
        Weight: {weight}
        Height: {height}
        BMI: {BMI}
        Category: {category}


""")
    