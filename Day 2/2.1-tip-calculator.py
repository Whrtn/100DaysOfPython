print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15?")
num_of_people = input("How many people to split the bill?")

# converting to correct types
bill = float(bill)
tip_percentage = int(tip_percentage)
num_of_people = int(num_of_people)

# calculations
tip = bill * (tip_percentage / 100)
total_bill = bill + tip
paying_each = round(total_bill / num_of_people, 2)

print(f"Each person should pay: ${paying_each}")



