n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    i = 2
    prime = True
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")