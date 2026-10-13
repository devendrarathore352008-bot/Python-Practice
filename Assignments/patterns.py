# Left aligned increasing star pattern

for i in range(1,6):
    print(" * " * i)

print()
print()

# Left aligned increasing star pattern

for i in range(5,0,-1):
    print(" * " * i)


print()
print()

# Right aligned increasing star pattern

#using f string for it
for i in range(1,6):
    print(f"{'*' * i:>5}")

print()

for i in range(1,6):
    print(" " * (5-i) + "*" * i)


print()
print()

# right aligned decreasing star pattern

for i in range(5,0,-1):
    print(f"{'*' * i:>5}")


print()
print()

# inverted pyramid pattern

for i in range(9,0,-2):
    spaces = (9-i )// 2
    print(" " * spaces + "*" * i)

print()
print()

# left aligned pyramid pattern

for i in range(1,6):
    print("*" * i)
for i in range(4,0,-1):
    print("*" * i)

print()
print()

# right aligned pyramid pattern
for i in range(1,6):
    print(" " * (5-i) + "*" * i)
for i in range(4,0,-1):
    print(" " * (5-i) + "*" * i)


print()

# left align number pyramid

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()


print()
print()

# Middle pattern diamond shape

for i in range(1,6):
    print(" " * (5-i) + "*" * (2 * i -  1))

for i in range(4,0,-1):
    print(" " * (5-i) + "*" * (2 * i - 1))
  