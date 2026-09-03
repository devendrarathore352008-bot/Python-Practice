li = [10,20,30,40,50]
for i in li:
    print(i)


for i in range(0,501):
    if i % 2 == 0:
        print(i)


# Take input as a number and print its table

table = int(input("Enter The Number: "))

for i in range(1,11):
    print(table,"*",i, "=", table*i)


    


# Write a program to compute the nth term of a geometic progression (ar^n-1).

a = int(input("Enter starting number:"))
r = int(input("Enter the value of r:"))
n = int(input("Enter the value of n:"))

for i in range(1,n+1):
    print(a*r**(i-1))






# Write a program for the sum of all natural numbers

n = int(input("Enter the number:"))
total_sum = 0
for i in range(1,n+1):
    total_sum += i

print(total_sum)