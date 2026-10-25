# 1. Fibonacci Series
N = int(input())
a = 0
b = 1
if N <= 0 :
    print("Invalid Input")
elif N == 1:
    print(0)
else:
    print(a, b,end=" ")
    for i in range(N-2):
        next_number = a+b
        print(next_number,end=" ")
        a = b
        b = next_number

# Armstrong Numbers
L = int(input())
R = int(input())

for num in range(L,R+1):
    str_num = str(num)
    length = len(str_num)
    number = 0
    for j in str_num:
        number += int(j) ** length
        

    if number == num:
        print(number,end=" ")


#Perfect Positive Number
N = int(input())
total = 0
for i in range(1,N):
    if N % i == 0:
        total += i

if total == N:
    print("Perfect Number")
else:
    print("Not Perfect")


# Check the number is Palindrome or not without using STRING SLICING 
N = int(input())
temp = N
rev = 0
while N > 0:
    digit = N % 10
    rev = (rev * 10) + digit
    N = N // 10
    
if temp == rev:
    print(rev)
    print("Palindrome")
else:
    print(rev)
    print("Not Palindrome")

# With String Slicing

N = int(input())
temp = str(N)
rev = temp[::-1]

    
if N == int(rev):
    print(int(rev))
    print("Palindrome")
else:
    print(int(rev))
    print("Not Palindrome")


# Common vowel count problem

S = input()
vowel = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for i in S:
    if i in vowel:
        vowel_count += 1
    else:
        consonant_count += 1

is_prime = True
if vowel_count <= 1:
    is_prime = False
else:
    for j in range(2, int(vowel_count**0.5) + 1):
        if vowel_count % j == 0:
            is_prime = False
            break


final_output = []

if is_prime:
    final_output.append(S[::-1])
else:
    final_output.append(S.upper())


final_output.append(vowel_count)
final_output.append(consonant_count)


print(*final_output)



# Using function and implementing Prime number and Factorial in it

N = int(input())
numbers = list(map(int,input().split()))

def is_prime(n):
    if n > 1:
        for j in range(2,n):
            if n % j == 0:
                return False
        return True
    else:
        return False

def get_factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i

    return factorial

for num in numbers:
    if is_prime(num):
        print(get_factorial(num))
    else:
        print("Not Prime")

# Reverse string and using vowel technique

S = input().split()
vowel = "aeiouAEIOU"
result = []

for char in S:
    first_char = char[0]
    if first_char in vowel:
        char = char.upper()
        result.append(char)
    else:
        char = char[::-1]
        result.append(char)

print(*result)