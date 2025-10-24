
start =1
max = 1000
result = 0

while start < max:
    if start % 3 ==0 or start % 5 == 0:
        result = result + start
    start = start + 1
print(result)