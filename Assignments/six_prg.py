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

print()
print("---End Of The Program---")
print()



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


print()
print("---End Of The Program---")
print()



# Q.3 Practice by using if,elif or else conditional statements to check which number is greater among three numbers.

print("---   Checking Which Number is the Greatest among three numbers   ---")


number1 = int(input("Enter The First Number :"))
number2 = int(input("Enter The Second Number :"))
number3 = int(input("Enter The Third Number :"))



if (number3 == number1) and (number2 == number1) and (number2 == number3):
    print("All three numbers are equal to each other.")

elif (number1 > number2) and (number1 > number3) :
    print(f"{number1} is the greatest number.")

elif (number2 > number1) and (number2 > number3) :
    print(f"{number2} is the greatest number.")

else:
    print(f"{number3} is the greatest number.")


print()
print("---End Of The Program---")
print()


# Q.4 Print even number from 1 to 100

print()
print("--Even Numbers 1-100--")
for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")

print()
print()
print("---End Of The Program---")
print()

# Q.5 Print odd number from 1 to 100

print("--Odd Numbers 1-100--")
for i in range(1,101):
    if i % 2 != 0:
        print(i,end=" ")

print()
print()
print("---End Of The Program---")
print()
print()

# Q.6 Print prime number from 1 to 100

print("--Prime Numbers 1-100 By For Loop")

for prime in range(2,101):
    for j in range(2,prime):
        if prime % j == 0:
            break
    else:
        print(prime,end=" ")

print()
print()

print("--Prime Numbers 1-100 By While Loop")

n = 2

while n <= 100:
    j = 2
    while j < n:
        if n % j == 0:
            break
        j += 1
    else:
        print(n,end=" ")
    n += 1

print()
print()
print("---End Of The Program---")