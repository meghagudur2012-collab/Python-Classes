numbers = [11,22,33,44,55,66]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
       numbers[i] = numbers[i] * 10

    elif numbers[i] % 2 != 0:
        numbers[i] = numbers[i] + 5

print(numbers)