number = 9999
result = 0
while number > 0:
    digit = number % 10
    result = result + digit
    number = number // 10
    if number == 0 and result > 9:
        number = result
        result = 0
print(result)
