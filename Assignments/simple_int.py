
#    Write A Program To Calculate The SIMPLE INTEREST Using Formula (Date:27/08/2026)


# Take Principal, Rate and Time as Input from the User

Principal = float(input("Enter the principal amount (₹): "))
Rate = float(input("Enter the rate percentage (%): "))
Time = float(input("Enter the time period (years): "))


Simple_int = (Principal*Rate*Time) / 100

Total_amount = Simple_int + Principal

print("------ SIMPLE INTEREST-------")
print("Principal Amount:", "₹",Principal)
print("Simple Interest:", "₹",Simple_int)
print("Total Amount:","₹",Total_amount)



##               Calculate Without Formula

# Take principal, rate and time as Input from the User

principal = float(input("Enter the principal amount (₹): "))
rate = float(input("Enter the rate percentage (%): "))
time = float(input("Enter the time period (years): "))


r = rate / 100

simple_int_1 = principal*r*1

total_simple_int = simple_int_1*time

total_amount = principal+total_simple_int



print("----- SIMPLE INTEREST------")

print("Principal Amount:","₹",principal)
print("Simple Interest:","₹",total_simple_int)
print("Total Amount:","₹",total_amount)

