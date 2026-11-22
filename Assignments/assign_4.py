#                                 Date: 14/11/2026



# Q.1 Write a python program to check whether a given string is a palindrome.

str_1 = input("Enter a text: ") 
text = str_1.lower()
rev_text = text[::-1]
if text == rev_text:
    print(f"'{str_1}' is a Palindrome")
else:
    print(f"'{str_1}' is not a Palindrome")

# Q.2 Develop a python program to count the number of uppercase letters, lowercase letters, digits and special characters in a string.

word = input("Enter a word: ")

upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for letter in word:
    if letter.isupper():
        upper_count += 1
    elif letter.islower():
        lower_count += 1
    elif letter.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special Characters: {special_count} ") 


# Q.3 Write a python program to remove duplicate elements from a list without using built-in set functions.

lst = [1,2,"Dev",3,"Python",1,"Dev",3]
new_list = []

for element in lst:
    if element not in new_list:
        new_list.append(element)
        
print(new_list)


# Q.4 Develop a python program to sort a list in ascending and descending order using list methods.

lst = [10,1,15,16,3,9,30,42,18,25]
asc_list = lst.copy()
asc_list.sort()

desc_list = lst.copy()
desc_list.sort(reverse=True)
print(f"Original List: {lst}")
print(f"Ascending Order: {asc_list}")
print(f"Descending Order: {desc_list}")


# Q.5 Write a python program to merge two lists and eliminate duplicate elements.

list_1 = [ 1,2,3,4]
list_2 = [2,1,5,6,3]

merged_list = list(set(list_1+list_2))

print("Merged List:", merged_list)


# Q.6 Develop a python program to find the frequency of each character in a string.

text = input("Enter a text:")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char]+1
    else:
        frequency[char] = 1

print(frequency)


# Q.7 Write a python program to create a dictionary containing student names and marks and display the topper.

student_data = {
    "Raja": 78,
    "Pawan": 89,
    "Nikki": 96,
    "Rohit":80,
    "Tina": 87,
    "Nisha": 97,
    "RDJ": 99
}
topper = max(student_data,key = student_data.get)
print(topper)