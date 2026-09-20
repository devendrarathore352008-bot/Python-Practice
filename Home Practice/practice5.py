first_name = "Devendra"
surname = "Rathore"
age = 18
height = 5.9 
vote_eligibility = True
non_vegetarian = False
petname = None

print(first_name)
print(age)
print(height)
print(vote_eligibility)
print(non_vegetarian)

print()

print("-------------Types of data-----------------")

print()

print(type(first_name))
print(type(age))
print(type(height))
print(type(vote_eligibility))
print(type(non_vegetarian))

print()

print("-------------converting data types----------")

print()

print(float(age))
print(int(height))
print(not(vote_eligibility))
print((non_vegetarian))
print(bool(age))
print(bool(petname))


print()


print("------------Operations------------")

print()

print("--------for strings-----------")

print()

print(first_name+surname)
# print(first_name*surname) it will show error
# print(first_name+2) it will show error
print(first_name*3)
# print(first_name/surname) it will show error

print()

a = 15
b = 4
c = 3.0

print("-----For integers & floot----------")

print(a+b)
print(a+c)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print(a/c)
print(a*c)
print(a//c)

print()

print("-----For boolean-----")

print()

first = True # it is always 1
second = False # it is always 0
third = True
fourth = False

print(first + second + fourth)
print(first + third + fourth)
print(second + third + fourth)
print(first + second + third + fourth)

print("checking with not")

print(not(first + second + fourth))
print(not(first + third + fourth))
print(not(second + third + fourth))
print(not(first + second + third + fourth))

print("with some variables")
print(not(first + second))
print(not(first + third))
print(not(second + third))
print(not(first + second + third))

print()

print("------------------Logical Operators-----------------")

print()

print("And")

print()

print(first and second )
print(first and third)
print(second and third and fourth)
print(first and second and third and fourth)

print()

print("OR")

print()

print(first or second )
print(second or fourth)
print(first or third or fourth)
print(second or third or fourth)
print(first or second or third or fourth)


print("----------------\nEnding Data Types\n----------------")

print()


print("----Grade Calculator----")

print()

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("FAILED")




import random

# 1. Setup the game
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# 2. Start the game loop
while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1  # Count this turn

    # 3. Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
        
    elif guess > secret_number:
        print("Too high! Try again.")
        
    else:
        print("You got it!")
        print("It took you", attempts, "turns.")
        break  # This stops the loop and ends the game





import time

print("Welcome to the Reverse Number Guessing Game!")
print("Think of a secret whole number between 1 and 100.")
print("Do not tell me! I will try to guess it.")
print("Type 'h' if my guess is too high, 'l' if it's too low, or 'c' if it's correct.")
print("---------------------------------------------")

# Start with the full range of possibilities
low = 1
high = 100
attempts = 0

# The computer keeps guessing until it finds the number
while True:
    # Calculate the middle number of the current range
    # '//' does integer division (e.g., 5 // 2 is 2, not 2.5)
    guess = (low + high) // 2
    attempts = attempts + 1
    
    print(f"\nMy guess number {attempts} is: {guess}")
    feedback = input("Is it too High (h), too Low (l), or Correct (c)? ").lower()
    
    if feedback == 'c':
        print(f"\nHooray! I guessed your number in {attempts} attempts!")
        break  # Game over, exit the loop
        
    elif feedback == 'h':
        # If the guess was too high, your number must be smaller.
        # Change the upper bound to be right below this guess.
        high = guess - 1
        
    elif feedback == 'l':
        # If the guess was too low, your number must be larger.
        # Change the lower bound to be right above this guess.
        low = guess + 1
        
    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")
        attempts = attempts - 1  # Don't penalise the computer for a typo
        
    # Safety check: if you gave conflicting feedback, low will become greater than high
    if low > high:
        print("\nHmm... are you sure? The clues you gave contradict each other!")
        break

    

