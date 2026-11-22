# # To call the whole functions including in the file

# import calculator

# addition = calculator.add(10,5)
# sub = calculator.sub(500,399)
# mul = calculator.mul(20,25)
# div = calculator.div(100,20)

# print("Addition")
# print(addition)
# print()
# print("Subtraction")
# print(sub)
# print()
# print("Multiplication")
# print(mul)
# print()
# print("Division")
# print(div)


# # To call the specific function from the file

# from calculator import div

# print(div(100,5))

# # To call the any variable from the file

# from calculator import add,z
# print(add(2,z))
# print(z)


# # To assign the function a nickname for better efficiency

# from calculator import add as a
# print(a(10,50))


# from print import greet
# result = greet()
# print(result)


# # Using inbuilt modules

# import math
# print(math.pi)
# print(math.pow(2,3.1))
# print(math.sqrt(625))


# import random

# num = random.randint(1,100)
# print("Random number :",num)



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n-1) + (n-2)

print(fib(8))