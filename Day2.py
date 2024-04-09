#A tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip_percentage / 100)
Each_person = "{:.2f}".format(total_bill / people) #formatting to 2 digits instead of using round()
print("Each person should pay "+ Each_person)

