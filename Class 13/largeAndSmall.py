numbers = [12, 45, 8, 67, 23, 90, 11]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest number:", largest)
print("Smallest number:", smallest)