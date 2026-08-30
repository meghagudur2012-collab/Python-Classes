food_total = float(input("Enter food total: "))
membership = input("Membership (yes/no): ").lower()


serv_charge = food_total * 0.05
billWithService = food_total + serv_charge

# Step 2: Apply 10% discount if member
if membership == "yes":
    discount = billWithService * 0.10
else:
    discount = 0

final_bill = billWithService - discount

print(f"""
            food total: {food_total}
            with service charge: {billWithService}
            discount: {discount}
            final bill: {final_bill}


""")