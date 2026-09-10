#                       { Date: 10/09/2026 }
'''

Write a program that takes an integer n and prints all of the following using loops only.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

*****
****
***
**
*

Odd numbers: 1 3 5
Even numbers: 2 4

Factorial of 5 = 120
 
'''

n = int(input("Enter the number:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ",)
    print()

print()

i = n
while i > 0 :
    print("*" * i)
    i -= 1
print()


print("Odd numbers:", end=" ")
for i in range(1,n+1,2):
    print(i,end=" ")
print()

print("Even numbers:", end=" ")
for i in range(2,n+1,2):
    print(i,end=" ")

print()
print()

factorial = 1
i = n
while i > 0:
    factorial *= i
    i -= 1
print(f"Factorial of {n} = {factorial}")


''' Write a program to print prime numbers from 1 to 100'''

num = 2
list =[]

while num <= 100:
    is_prime = True
    j = 2
    while j < num:
        if num % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        list.append(num)

    num += 1

print(f"Total prime numbers b/w 1 - 100 = {len(list)} \nList = {list}")