start = 1
end = 20
index = 1
max = 1

while index <= end:
    max = max*index
    index = index + 1

result = 0
index = end

while index <= max:
    is_divisible_by_all = True
    counter = start
    while counter <= end:
        if index % counter != 0:
            is_divisible_by_all = False
            break
        counter = counter + 1
    if is_divisible_by_all:
        result = index
        print(result)
        exit(0)
    index = index + end
