#                                                          (Date:09/09/2026)

# Practicing Six Programms.




#    Write A Program To Calculate The SIMPLE INTEREST Using Formula. 


# Take Principal, Rate and Time as Input from the User

Principal = float(input("Enter the principal amount (₹): "))
Rate = float(input("Enter the rate percentage (%): "))
Time = float(input("Enter the time period (years): "))


Simple_int = (Principal*Rate*Time) / 100

Total_amount = Simple_int + Principal

print("------ SIMPLE INTEREST-------")
print("Principal Amount:", "₹",Principal)
print("Simple Interest:", "₹",Simple_int)
print("Total Amount:","₹",Total_amount)






# write a program to convert temp from degree celsius to degree farenheit

print("-----Converting Celsius to Farenheit-----")

Celsius = float(input("Enter the temperature in  Celsius:"))

Farenheit = (Celsius * 9/5) + 32

print(f"The {Celsius} degree celsius is equal to {Farenheit} degree farenheit")


# write a program to check a given number even or odd

print("-----Checking Number is Odd or Even-----")
num = int(input("Enter the number:"))


if num % 2 == 0:
    print(f"The given number {num} is Even.")
else:
    print(f"The given number {num} is Odd.")


# program to check which number is greater

print("---    Checking Which Number is Greater b/w two numbers    ---")



num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))



if num1 > num2 :
    print(f"First number {num1} is Greater Than Second Number.")

elif num2 > num1:
    print(f"Second number {num2} is Greater Than First Number.")

else:
    print("Both numbers are equal.")






# Q.3 Practice by using if,elif or else conditional statements to check which number is greater among three numbers.

print("---   Checking Which Number is Greater among three numbers   ---")


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
    



# write a table

print("----Printing The Table-----")

table = int(input("Enter the number:"))

for i in range(1,11):
    print(f"{table} * {i} = {table*i} ")



