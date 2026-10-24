# total_price = float(input("Enter the total price of the product: "))
# discount_rate = float(input("Enter the discount percentage: "))
# gst_rate = float(input("Enter the GST percentage: "))


# discount_amount = total_price * (discount_rate / 100)
# price_after_discount = total_price - discount_amount

# gst_amount = price_after_discount * (gst_rate / 100)

# final_payable_amount = price_after_discount + gst_amount


# print("\n-- Bill Summary --\n")
# print(f"Original Price : {total_price:.2f} Rupees")
# print(f"Discount ({discount_rate}%) : -{discount_amount:.2f} Rupees")
# print(f"Price: {price_after_discount:.2f} Rupees")
# print(f"G.S.T. ({gst_rate}%) : +{gst_amount:.2f} Rupees")

# print("\n-------------------------------------------------------------------------------------------------------")

# print(f"Total Payable Amount : {final_payable_amount:.2f} Rupees")

# print("-------------------------------------------------------------------------------------------------------\n")

# print("------- !! THANKS FOR VISITING !! SEE YOU SOON !! -------")


# mark1 = int(input("Enter the marks: "))
# mark2 = int(input("Enter the marks: "))
# mark3 = int(input("Enter the marks: "))
# mark4 = int(input("Enter the marks: "))
# mark5 = int(input("Enter the marks: "))

# print(sum([mark1,mark2,mark3,mark4,mark5]))

# year = 2008
# month = 5
# date = 3

# print(year,month,date,sep="-")

# number = eval(input("Enter the number : "))
# if number>0:
#     print("Positive")
# else:
#     print("Negative")

# correct_username = "devendrar_35280"
# correct_password = "Hemu@2008"

# username = input("Enter your username(Ex: example@1234) : ")
# password = input("Enter your password : ")

# if (username == correct_username) and (password == correct_password):
#     print("\nAccess Approved ! \nLoading...........")

# else:
#     print("\nAccess Denied !! Warning, Write correct username or password.")

# num = int (input("Enter the number: "))

# if num < 0 :
#     print("Negative")
# elif num > 0:
#     print("Positive")
# else:
#     print("Zero")

# marks = int(input("Enter your marks: "))
# print()
# if (marks >= 0) and (marks <= 100):
#     if marks >= 90:
#         print("Grade: A")
#     elif marks >= 75:
#         print("Grade: B")
#     elif marks >= 60:
#         print("Grade: C")
#     elif marks >= 45:
#         print("Grade: D")
#     elif marks >= 33:
#         print("Grade: E")
#     else:
#         print("Grade: F (Failed)")

# else:
#     print("! Invalid Input. Please Enter Correct Marks.")

# num1 = eval(input("Enter first number: "))
# num2 = eval(input("Enter second number: "))

# print("\n--- Which operation you want to perform ---\n")
# print("1. Addition\n2.Subtraction\n3.Multiplication\n4.Division")
# print()
# choice = eval(input("Enter your choice[1-4] : "))
# print()
# if (choice >= 1) and (choice <= 4) :
#     if choice == 1:
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif choice == 2:
#             print(f"{num1} - {num2} = {num1 - num2}")
#     elif choice == 3:
#             print(f"{num1} * {num2} = {num1 * num2}")
#     else:
#         print(f"{num1} / {num2} = {num1 / num2}")

# else:
#       print("!! Invalid Choice. Choose number b/w 1-4.")




# correct_username = "scarist_gamer_3528"
# correct_password = "Scarist@2008"

# username = input("Enter your username(Ex: example@1234) : ")

# print()

# if (username == correct_username):
#     print("Username verified !\n")
#     password = input("Enter your password : ")
#     if (password == correct_password) :
#         print("\nPassword Verified !, Access Loading.............")
#     else:
#         print("! Invalid Password. Access Denied !")
# else:
#     print("Access Denied !! Warning, Write correct username.")

# num = 1
# while num <= 10:
#     print(num)
#     num += 1



# num = 2
# while num <=20 :
#     if num % 2 == 0 :
#         print(num)
#     num += 1   
    

# num = 1
# N = int(input("Enter the number: "))
# sum = 0
# while num <= N:
#     sum += num
#     num += 1
# print(sum)


sum = 0
average = 0
count = 0
while True :
    user_message = int(input("Enter the Number: "))
    if user_message != 0:
        sum += user_message
        count += 1
        average = sum / count
    else:
        break

print("Sum :", sum) 
print("Count :", count)
print("Average : ",average)
