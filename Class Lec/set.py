s1 = set({'a',9,8.5,10})
s2 = set(('b',5.9,9,1))

union = s1|s2
intersection = s1&s2
assymetric = s1^s2

print(9 in s1)
print("set 1")
print(s1)
print("set 2")
print(s2)
print("Union of s1 and s2")
print(union)
print("Intersection of s1 and s2")
print(intersection)
print("Assymetric of s1 and s2")
print(assymetric)


s1.add("Devendra")
s2.add("Mohammad")

print(s1)
print()

print(s2)
print()

s1.remove("Devendra")
s2.remove("Mohammad")

print(s1)
print()
print(s2)