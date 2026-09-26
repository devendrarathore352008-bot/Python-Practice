# Q.1 find largest among three numbers using nested if statements.

num1 = float(input("Enter the first num: "))
num2 = float(input("Enter the second num: "))
num3 = float(input("Enter the third num: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(f"The largest number among the given numbers is {largest} ")


# Q.2 Calculate the grade of a student based on percentage using if-elif-else.

percent = float(input("Enter the percentage of student: "))

if (percent < 0) or (percent > 100) :
    print("! Enter Valid Percentage !")
elif percent >= 85 :
    print("Grade: A ")
elif percent >= 70 :
    print("Grade: B ")
elif percent >= 50:
    print("Grade: C ")
elif percent >= 33:
    print("Grade: D")
else:
    print("Grade: F")


# Q.3 Calculate the sum of first N natural numbers using while loop.

N = int(input("Enter a natural number: "))
sum = 0
i = 1

if N <= 0 :
    print("!!Please Enter a valid natural number!!")

else:
    while i <= N:
        sum += i
        i += 1
    print(f"Sum of first {N} natural numbers is {sum}")



N = int(input("Enter the number of terms: "))

a = 0
b = 1

if N <= 0:
    print("!! Invalid, enter a number greater than 0 !!")

elif N == 1:
    print(f"--Fibonacci Series--\n{a}")

else:
    print("--Fibonacci Series--")
    print(a,b,end=" ")

    for i in range(2,N):
        c = a+b
        print(c,end = " ")

        a = b 
        b = c


# Q.4 Write a program to check whether the given number is prime.

# num = int(input("Enter a number: "))
# list = []
# for i in range(2,num+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         list.append(i)

# if num in list:
#         print("Number is prime")
# else:
#     print("It is not prime")


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("It is not prime.")
            break
    else:
        print("It is prime")
else:
    print("It is not prime")


# A program which reverse the digits of a given integer using loops

num = int(input("Enter the number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num//10
print("Reverse =",reverse)


#Q.8 Print the pattern 
'''

*
**
***
****
*****

'''
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()


# Example of nested loop

for i in range(1,4):
    for j in range(1,6):
        print(i,j)