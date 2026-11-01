evenCount = 0
oddCount = 0

numbers = [8, 15, 22, 31, 40, 55, 62]

for i in range(len(numbers)):
    if i % 2 == 0:
        evenCount = evenCount + 1

    if i % 2 != 0:
        oddCount = oddCount + 1

print("Even numbers: ",evenCount)
print("Odd numbers: ",oddCount)