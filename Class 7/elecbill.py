units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = 500 + (units - 100) * 7
else:
    bill = 1900 + (units - 300) * 10

if bill > 1500:
    bill += bill * 0.08

print(f"""
            units used: {units}
            Final Bill: {bill}

""")