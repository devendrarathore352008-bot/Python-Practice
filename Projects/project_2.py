#                                { Date : 18/09/2026 }

''' 

Q. Let's assume you are planning to use your Python skills to build a PBLApp for Mobile.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know how much it will cost to operate per day, per week, per month.

Write a Python program that displays the answers to the following questions:

    How much does it cost to operate one server per day?

    How much does it cost to operate one server per week?

    How much does it cost to operate one server per month?

    How many days can I operate one server with $918?

'''

# ---------------------------------------------Code--------------------------------------------------

hourly_rate = 0.51

hour_per_day = 24
days_per_week = 7
days_per_month = 30


per_day_cost = hourly_rate * hour_per_day
per_week_cost = per_day_cost * days_per_week
per_month_cost = per_day_cost * days_per_month

budget = 918
days = budget / per_day_cost

print(f"How much does it cost to operate one server per day? \n Answer: ${per_day_cost:.2f}")

print(f"How much does it cost to operate one server per week? \n Answer: ${per_week_cost:.2f}")

print(f"How much does it cost to operate one server per month? \n Answer: ${per_month_cost:.2f}")

print(f"How many days can I operate one server with ${budget}? \n Answer: {days:.1f} days.")

'''
You can use these print statements if you don't want to use f string method which is little bit typical.


print("How much does it cost to operate one server per day?")
print("$", cost_per_day)
print()

print("How much does it cost to operate one server per week?")
print("$", cost_per_week)
print()

print("How much does it cost to operate one server per month?")
print("$", cost_per_month)
print()

print("How many days can I operate one server with $918?")
print(days_with_budget, "days")

'''