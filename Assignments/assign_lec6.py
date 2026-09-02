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


print("---    Checking Which Number is Greater b/w two numbers    ---")

# Taking numbers as input from the users

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

# using conditional statement to check which is greater b/w two numbers

if num1 > num2 :
    print("First number is Greater Than Second Number.")

else:
    print("Second number is Greater Than First Number.")


print("---End Of The Program---")



# Q.3 Practice by using if,elif or else conditional statements to check which number is greater among three numbers.

print("---   Checking Which Number is Greater among three numbers   ---")

# Taking numbers as input from the user

number1 = int(input("Enter The First Number :"))
number2 = int(input("Enter The Second Number :"))
number3 = int(input("Enter The Third Number :"))


# using conditional statements to check which number is greater

if (number1 > number2) and (number1 > number3) :
    print("First Number is greater than other two numbers.")

elif (number2 > number1) and (number2 > number3) :
    print("Second Number is greater than other two numbers.")

else:
    print("Third Number is greater than other two numbers.")


print("---End Of The Program---")
    



