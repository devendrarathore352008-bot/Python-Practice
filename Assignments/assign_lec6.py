#                                   {   Date:02/09/2026    }


# Q.1 Practice by using if,elif or else conditional statements to check whether the number is even or odd.

print("---Checking Even Or Odd---")   
#Taking number as an input from the user

num = int(input("Enter the number:"))

# using conditional statements

if num % 2 == 0 :
    print("Number is Even.")

else:
    print("Number is Odd.")

print("---End Of The Program---")



# Q.2 Practice by using if,elif or else conditional statements to check which number is greater between two numbers.


print("---    Checking Which Number is the greatest b/w two numbers    ---")

# Taking numbers as input from the users

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

# using conditional statement to check which is greater b/w two numbers

if num1 > num2 :
    print(f"First number {num1} is Greater Than Second Number.")

elif num2 > num1:
    print(f"Second number {num2} is Greater Than First Number.")

else:
    print(f"Both numbers are equal.")


print("---End Of The Program---")



# Q.3 Practice by using if,elif or else conditional statements to check which number is greater among three numbers.

print("---   Checking Which Number is the Greatest among three numbers   ---")

# Taking numbers as input from the user

number1 = int(input("Enter The First Number :"))
number2 = int(input("Enter The Second Number :"))
number3 = int(input("Enter The Third Number :"))


# using conditional statements to check which number is greater

if (number3 == number1) and (number2 == number1) and (number2 == number3):
    print("All three numbers are equal to each other.")

elif (number1 > number2) and (number1 > number3) :
    print(f"{number1} is the greatest number.")

elif (number2 > number1) and (number2 > number3) :
    print(f"{number2} is the greatest number.")

else:
    print(f"{number3} is the greatest number.")


print("---End Of The Program---")
    



