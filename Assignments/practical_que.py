# #                                            Date: 15/10/2026

# # Que.1 Program to count the number of each vowel in a string.

# def count_vowels(text):
#     vowels = "aeiou"
#     counts = {v: 0 for v in vowels}
    
#     for char in text.lower():
#         if char in counts:
#             counts[char] += 1
            
#     return counts


# sample = input("Enter the message: ")
# result = count_vowels(sample)
# print(result)





# # Que.2 Program to Find Sum of Natural Numbers Using Recursion. 

# def sum_of_natural_num(num):
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num + sum_of_natural_num(num-1)

# number = int(input("Enter the number:"))
# result = sum_of_natural_num(number)
# print(f"Sum of first {number} natural numbers: {result}")


# # Que.3 Program to Display powers of 2 using Anonymous Function.

# terms = 6
# powers_of_two = list(map(lambda x: 2 ** x, range(terms)))

# for index, value in enumerate(powers_of_two):
#     print(f"2^{index} = {value}")





# # Que.4 Program to accept three digits and print all possible combinations from the digits.

# def print_combinations(a: int, b: int, c: int):
#     digits = [a, b, c]

#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 if i != j and j != k and i != k:
#                     print(f"{digits[i]}{digits[j]}{digits[k]}")


# d1 = int(input("Enter first digit: "))
# d2 = int(input("Enter second digit: "))
# d3 = int(input("Enter third digit: "))

# print_combinations(d1, d2, d3)



# # Que. 5 Program to find he sum of the series: 1+x^2/2+x^3/3+...x^n/n.

# def series_sum(x: float, n: int) :
#     if n < 1:
#         return 0.0

#     total = 1.0  
#     for i in range(2, n + 1):
#         total += (x ** i) / i
#     return total


# x_value = float(input("Enter value of x: "))
# n_value = int(input("Enter value of n: "))

# print(f"Sum of the series: {series_sum(x_value, n_value)}")



# # Que. 6 Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.
# def create_number_square_tuples(n: int):
#     return [(num, num ** 2) for num in range(1, n + 1)]


# limit = int(input("Enter upper limit: "))
# result = create_number_square_tuples(limit)
# print(result)

# # Que.7 Program to Count the Frequency of Words Appearing in a String Using a Dictionary.
# def word_frequency(text):
#     counts = {}

#     for word in text.lower().split():
#         counts[word] = counts.get(word, 0) + 1

#     return counts


# sentence = input("Enter a sentence: ")
# frequencies = word_frequency(sentence)

# for word, count in frequencies.items():
#     print(f"{word}: {count}")



# Que.15 Program to find the area of rectangle using Classes
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

rect = Rectangle(length, width)
print("Area of rectangle:", rect.area())