a = 1
b = 2
result = 2
while a + b < 4000000:
  c = a + b
  if c % 2 == 0:
     result = result + c
  a = b
  b = c
print(result)


