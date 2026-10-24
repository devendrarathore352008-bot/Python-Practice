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
