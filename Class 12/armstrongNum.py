i = int(input("Enter a number: "))
copy = i
sum = 0

while copy > 0:
    digit = copy % 10
    sum = sum + digit ** 3
    copy = copy // 10

if sum == i:
    print("Yes, it's an Armstrong number.")
else:
    print("No, it's not an Armstrong number.")