# variable Argument functions
def variableArgumentFunction(*a):
    total = 0
    for i in a:
        total += i
    print(f"Sum = {total}")


# Globa variable

x = 20
def globalvariable():
    y = 15
    print(x)
    print(y)
