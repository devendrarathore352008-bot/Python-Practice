#                                    { Date: 10/09/2026 }

''' 
                               NESTED LOOPS
        Nested loops means to write a loop inside another loop.

## Important Point: Make sure not to avoid INTENDATION(the space in left side of code).
        
Nested (For) Loop Syntax

for <variable> in <sequence>:
    for <variable> in <sequence>:
        statements(s)
    statements(s)


Nested (while) Loop Syntax

while expression:
    while expression:
        statements(s)
    statements(s)



'''

# Program to write table from 2 to 10 (Using {for} nested loop)

for i in range(2,11):
    for j in range(1,11):
        print(i*j,end = " ")
    print("\n")


# Program to print pattern pyramid(Using {for} nested loop)

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()



'''
                                (break) STATEMENT

It is use to stop the loop completely after the statement.

Syntax

for <variable> in <sequence>:
    if condition:
        break

'''

# Simple Example

for number in range(1,6):
    if number == 3:
        print("Found The Number, Breaking out of the loop")
        break 
        # Here it will break loop if number = 3
        # if we don't use break statement it will print the number till the 5 because we mention range(1,6)
    print("current number", number)

print("Loop ended completely")


# Another Tough example

print("Enter 5 positive values")
sum = 0

for i in range(5):
    value = int(input())
    if value < 0 :
        break
    sum += value

print("Sum =", sum)


'''
                                (continue) STATEMENT
    
    It is used to skip the specific part and continue further.

Syntax

for <variable> in <sequence>:
    if condition:
        break

'''

# Simple Example

for num in range(1,6):
    if num == 3: # here it will skip three and print further numbers
        continue
    print(num)


# Another example

print("Enter 5 positive values")
sum = 0

for i in range(5):
    value = int(input())
    if value < 0 :
        continue
    sum += value

print("Sum =", sum)


# Find out what kind of loop it is

'''

i = 1
while i <= 10:
    if i % 2 == 0:
        continue
    print(i,end=" ")
    i = i + 1

'''

# It is an infinite loop








'''
             Practicing Several Programs Using Loop
'''

# A program to write odd numbers 1 to 100

for num in range(1,101):
    if num % 2 != 0:
        print(num,end=" ")


# A program to write even numbers 1 to 100

for num in range(1,101):
    if num % 2 == 0:
        print(num,end=" ")


# A program to write prime numbers 1 to 100
# for prime in range(1,101):
#     for j in range(2,prime):
#         if prime % j  == 0:

prime_list=[]

for prime in range(2,101):
    for j in range(2,prime):
        if prime% j == 0:
            break
    else:
        prime_list.append(prime)

print(f"The prime numbers b/w 1 - 100 is {len(prime_list)}\nList: {prime_list}")








'''
This is second method 

for prime in range(2,101):
    it_is_prime = True
    for j in range(2,prime):
        if prime % j  == 0: 
            it_is_prime = False 
            break
    if it_is_prime == True:
        print(prime)


'''


    