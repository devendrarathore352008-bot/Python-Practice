name = "Devendra"
age = 18
s1 = "My name is {} and I am {} years old."
print(s1.format(name,age))

statement = "{0} is a good student. {0} is a {1} student. {0} is {2} years old."
p1 = "Devendra"
p2 = "BCA"
p3 = 18

print(statement.format(p1,p2,p3))

s = "HNVerma"
s2 = s.swapcase()
print(s2)



# List 

List1= [10,2.56, "Hello",("Welcome","to", "Python", "World")]

lst1,lst2,lst3,lst4 = List1

List2 = [10,20,30,40,50,100.65,200,1.23]

print(lst1)
print(lst2)
print(lst3)
print(lst4)

sequence = list({10,20,30,1.23})

print(min(List2))
print(max(List2))
print(len(List2))
print(sequence)


list = [10,20,30,40,50,60,70,80,20,40,10,1000]

print(list, "This is original List")
print()

print(list.index(10), "Indexing Method")
print(list)
print()

print(list.count(10), "Count Method")
print(list)
print()

print(list.pop(), "Last object automatic pop method")
print(list)
print()

print(list.pop(1), "pop method by giving index")
print(list)
print()

print(list.insert(1, 100), "insert method")
print(list)
print()

print(list.remove(60), "Remove Method")
print(list)
print()

print(list.reverse(), "Reverse method")
print(list)
print()

print(list.sort(), "sort method")
print(list)


# Different elements in list

list1 = ["Devendra",18,5.9, ("He","is","very","disciplined","boy")]
list2 = ["MD",19,6.2, ("He","is","very","punctual","boy")]
list = [10]
list4 = [1,2,3,4,5]

list3 = list1 + list2
# print(list1 * list2) can't multiply
print(list1 * 2)
print(list3)

#print(list1 - list2) can't subtract

print(list1[1] + list2[1])

print(min(list))
print(max(list))
print(len(list1))
print(list(sequence))

print(list2[-1])



seq = ["Dev",("Hello World"),[1,3,4,5],"Dev"]
print("Dev" in seq)
print("Dev" not in seq)
for e in seq:
    print(e,end=" ")



# Using for loop in list

list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for e in list:
    sum += e

print(f"Sum of the elements of list = {sum}")

