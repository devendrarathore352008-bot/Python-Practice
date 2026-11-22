def get_fib(N):
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    else:
        # This is recursion: the function calls itself!
        return get_fib(N - 1) + get_fib(N - 2)        

def is_prime(n):
    found = True
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                found = False
                break
    else:
        found = False
    return found

while True:
    data = input().split()

    if data[0] == "END":
        break
    else:
        