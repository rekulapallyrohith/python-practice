start = 1
end = 10
sum_of_squares = 0
square_sum = 0
while start <= end:
    sum_of_squares = sum_of_squares + start**2
    square_sum = square_sum + start
    start = start + 1
square_sum = square_sum**2    
result = square_sum - sum_of_squares
print(result)
