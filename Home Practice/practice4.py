#                                { Date: 12/01/2026 }

# Write a program to check if a given integer number is Positive, Negative, or Zero.

try:
    
    num = int(input("Enter The Number: "))

    if num == 0:
        print(f"The given number({num}) is ZERO. ")
    elif num > 0:
        print(f"The given numer({num}) is POSITIVE.")
    else:
        print(f"The given number({num}) is NEGATIVE.")
except ValueError:
    print("Invalid")



# Write a program to given two non-negative integer values, print true if they have the same last digit, such as with 27 and 57

try:
    number1 = int(input("Enter The First Number: "))
    number2 = int(input("Enter The Second Number: "))

    if number1 < 0 or number2 < 0:
        print("Please Put Positive Values Only!")

    else:
        print(number1 % 10 == number2 % 10)

except ValueError:
    print("Invalid Number")