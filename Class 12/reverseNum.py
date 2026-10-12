i = int(input("Enter here: "))
reversed = 0
while i > 0:
    digit = i % 10
    reversed = reversed * 10 + digit
    i //= 10

print(reversed)
