# # Date : 08/09/2026

# print("Hello World.")

# a = float(input("Enter the first number:"))
# b = float(input("Enter the second number:"))

# sum = a + b
# print(f"The sum of given two numbers is {sum} .")



# # Area of circle

# radius = float(input("Enter the radius of circle: "))

# area_of_circle = 3.14*radius*radius
# print(f"The Area of circle is {area_of_circle}")



# # Swap Two Numbers

# x = float(input("Enter the value of x: "))
# y = float(input("Enter the value of y: "))

# # Taking a extra variable

# extra = x
# x = y
# y = extra

# print(f"The value of x is {x} and y is {y}")



# Print Even Or Odd

# x = float(input("Enter the value of x: "))

# if x % 2 == 0:
#     print(f"The number {x} is Even.")

# else:
#     print(f"The number {x} is Odd.")




# find leap year

# year = int(input("Enter the year: "))

# if year % 4 == 0:
#     print(f"The Year {year} is a leap year.")
# else:
#     print(f"The Year {year} is not a leap year.")




# Find The Factorial

num = int(input("Enter the number:"))

Factors = []

for i in range(1,num+1):
    if num % i == 0:
        Factors.append(i)
        i += 1

print(f"The Factors of number {num} are {Factors}")