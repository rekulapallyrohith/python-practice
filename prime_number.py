num = int(input("Enter the value: "))
n = 2
Is_prime = True
while n < num:
    if num % n == 0:
        Is_prime = False
        break
    n = n + 1
if Is_prime:
    print("is a prime number")
else:
    print("not a prime number")