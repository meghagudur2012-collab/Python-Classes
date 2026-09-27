for i in range(1,9):
    print(f"{i} -> {i*2}")

for i in range(1,51):
    if (i % 7 == 0) :
        print(i)

for i in range(1,61):
    if(i % 4 == 0 and i % 6 == 0):
        print(i)

for i in range(1, 26):
    if(i % 5 == 0 or i % 3 == 0):
        print(i)

for i in range(1,41):
    if(i % 4 == 0 and i % 8 != 0):
        print(i)