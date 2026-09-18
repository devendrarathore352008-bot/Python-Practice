#                                { Date : 18/09/2026 }

''' 

Q. Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to driver Super-Car.

'''

# ---------------------------Code-------------------------------------

travel_distance = float(input("How far would you like to travel in miles? :- "))

print()

if (travel_distance < 3):
    print("I suggest, You should Ride Bicycle.")
elif (travel_distance < 300):
    print("I suggest, You should Ride Motor-Cycle.")
else:
    print("I suggest, You should Drive Super-Car. ")
