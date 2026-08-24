totalBill = float(input("Enter purchase amount here: "))
couponCode = input("Enter input code here: ")

amountDiscount = 0
couponDiscount = 0
validCoupon = "SAVE10"
if totalBill > 100:
    amountDiscount = totalBill * 5/100
if couponCode == validCoupon:
    couponDiscount = 5
finalBill = totalBill - amountDiscount - couponDiscount
print(f"""
    1. totalBill    :  {totalBill}
    2. amountDiscount    :  {amountDiscount}
    3. couponDiscount    :  {couponDiscount}
    4. finalBill    :  {finalBill}
""")