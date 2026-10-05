n = int(input("Enter Here: "))
n_is_prime = "yes n is a prime number."

for i in range(2, n):
    if(n%i==0):
        n_is_prime = "no"
        print(f"{n} is not a prime number, because it is divisiable by {i}")
        break
if n_is_prime == "yes n is a prime number.":
    print(f"{n} is a prime number")
