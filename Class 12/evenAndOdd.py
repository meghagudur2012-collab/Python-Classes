i = int(input("Enter Here:"))
even = 0
odd = 0

while i > 0:
    digit = i % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    i //= 10

print("Even digits", even)
print("Odd digits", odd)