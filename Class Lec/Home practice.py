number = int(input("Enter The Value:"))
l_digit = 0

while number > 0:
    digit = number % 10
    if digit > l_digit:
        l_digit = digit
    number //= 10
print(l_digit)
