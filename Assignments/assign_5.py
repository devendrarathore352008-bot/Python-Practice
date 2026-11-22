#                                                        Date: 18/11/2026

# Q.1 Write a Python program using user-defined functions to calculate the area and perimeter of a rectangle.

# def area_of_rectangle(length,breadth):
#     return length*breadth

# def per_of_rectangle(length,breadth):
#     return 2*(length + breadth)

# area = area_of_rectangle(10,20)
# perimeter = per_of_rectangle(7,15)

# print(f"Area of rectangle: {area}")
# print(f"Perimeter of rectangle: {perimeter}")


def area_of_rectangle(length, breadth):
  return length * breadth


def per_of_rectangle(length, breadth):
  return 2 * (length + breadth)



try:
  length = float(input("Enter the length of the rectangle: "))
  breadth = float(input("Enter the breadth of the rectangle: "))

  if length < 0 or breadth < 0:
    print("Dimensions cannot be negative.")
  else:
    area = area_of_rectangle(length, breadth)
    perimeter = per_of_rectangle(length, breadth)

    print(f"Area of rectangle: {area}")
    print(f"Perimeter of rectangle: {perimeter}")
except ValueError:
  print("Please enter valid numbers.")







# Q.2 Develop a Python program using default and keyword arguments to calculate simple and compound interest. 

def calculate_simple_interest(principal, rate=5.0, time=1.0):
  """
  Default rate is 5% per annum, default time is 1 year
  """
  si = (principal * rate * time) / 100
  return si


def calculate_compound_interest(principal, rate=5.0, time=1.0, n=1):
  """
  Default rate=5%, time=1 year, n=1 (compounded annually)
  """
  # Formula: A = P(1 + r/(100*n))^(n*t), CI = A - P
  amount = principal * (1 + (rate / (100 * n))) ** (n * time)
  ci = amount - principal
  return ci


# 1. Using default arguments 
print("--- Using Default Arguments ---")
si_default = calculate_simple_interest(10000)
ci_default = calculate_compound_interest(10000)
print(f"Simple Interest (Default 5% for 1 yr): ₹{si_default:.2f}")
print(f"Compound Interest (Default 5% for 1 yr, annually): ₹{ci_default:.2f}")

# 2. Using keyword arguments 
print("\n--- Using Keyword Arguments ---")
si_kw = calculate_simple_interest(time=2.5, principal=50000, rate=8.2)
# Compounded quarterly (n = 4)
ci_kw = calculate_compound_interest(
    principal=50000, rate=8.2, time=2.5, n=4
)

print(f"Simple Interest (Keyword args): ₹{si_kw:.2f}")
print(f"Compound Interest (Keyword args, quarterly): ₹{ci_kw:.2f}")







def fibonacci_term(n):
  """Recursive function to return the nth Fibonacci number.

  (0-indexed: fib(0)=0, fib(1)=1)
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_term(n - 1) + fibonacci_term(n - 2)


def generate_fibonacci_series(n):
  """Generate a list of Fibonacci numbers up to N terms."""
  if n <= 0:
    return []

  # Generate series by calling fibonacci_term for each index from 0 to n-1
  return [fibonacci_term(i) for i in range(n)]


# Example usage:
n_terms = 10
series = generate_fibonacci_series(n_terms)
print(f"Fibonacci series up to {n_terms} terms: {series}")








# List of student dictionaries containing name, roll number, and marks
students = [
    {"name": "Aarav", "roll_no": 101, "marks": 85},
    {"name": "Priya", "roll_no": 102, "marks": 92},
    {"name": "Kabir", "roll_no": 103, "marks": 78},
    {"name": "Ananya", "roll_no": 104, "marks": 95},
    {"name": "Rohan", "roll_no": 105, "marks": 88},
]

# 1. Sort students by marks in ascending order (lowest to highest)
sorted_by_marks_asc = sorted(students, key=lambda x: x["marks"])

# 2. Sort students by marks in descending order (highest to lowest / merit list)
sorted_by_marks_desc = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order")
for student in sorted_by_marks_asc:
  print(
      f"Name: {student['name']:<8} | Roll No: {student['roll_no']}"
      f" | Marks: {student['marks']}"
  )

print("Descending Order")
for student in sorted_by_marks_desc:
  print(
      f"Name: {student['name']:<8} | Roll No: {student['roll_no']}"
      f" | Marks: {student['marks']}"
  )





# Create a menu-driven python program using modular programming where each menu option is implemented as a separate function.

def add(a,b):
  return a + b

def sub(a,b):
  return a - b

def multi(a,b):
  return a * b

def div(a,b):
  if b == 0:
    return " Error Not Found"
  return a / b



print("--- Calculator --- ")

while True:
  try:
    a = float(input("\nEnter the first number: "))
    b = float(input("Enter the second number: "))
  except ValueError:
    print("Invalid inputs !!")
    continue
  print()

  print("--- Choose option from [1-6] ---")
  print("\n1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")
  print("6. Type Again")
  print()

  while True:
    try:
      choice = int(input("\nEnter your choice [1-6]: "))
    except ValueError:
      print("Invalid choice !!")
      continue
    print()

    if choice < 1 or choice > 6:
      print("Invalid Choice !!")
      continue
    else:
      break

  if choice == 6:
    continue
  elif choice == 1:
    print(f"Addition({a} + {b}) : {add(a,b)}")
  elif choice == 2:
    print(f"Subtraction({a} - {b}) : {sub(a,b)}")

  elif choice == 3:
    print(f"Multiplication({a} * {b}) : {multi(a,b)}")
  elif choice == 4:
    print(f"Division({a} / {b}) : {div(a,b)}")
  else:
    print("--- Thankyou ---")
    break