num = int(input("Enter the value: "))
original = num
reversed = 0
while num > 0:
    digit = num % 10
    num = num // 10
    reversed = reversed * 10 + digit
if reversed == original:
    print("is a palindrome")
else:
    print("not a palindrome")
