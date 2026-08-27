'''
Assignment:- Find the largest number from the given three integers.
'''

#manual solution

first = int(input("Enter the first value: "))
second = int(input("Enter the second value: "))
third = int(input("Enter the third value: "))

if first >= second and first >= third:
    print(first," is the largest number.")
elif second >= first and second >= third:
    print(second," is the largest number.")
else:
    print(third," is the largest number.")


#in-built funtion solution

first_num = int(input("Enter the first value: "))
second_num = int(input("Enter the second value: "))
third_num = int(input("Enter the third value: "))

largest_num = max(first_num, second_num, third_num)
print(largest_num, "is the largest number among three.")


