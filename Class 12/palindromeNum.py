original = int(input("Enter here: "))
i = original
reversed = 0
while i > 0:
    digit = i % 10
    reversed = reversed * 10 + digit
    i //= 10

if reversed == original:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")




