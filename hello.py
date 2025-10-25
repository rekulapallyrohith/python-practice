num = 20
factorial = 1
for index in range(1, num+1):
    factorial *= index
for index in range(num, factorial, num):
    is_divisible_by_all = True
    for counter in range(1, num+1):
        if index % counter != 0:
            is_divisible_by_all = False
            break
    if is_divisible_by_all:
        print(index)
        break
