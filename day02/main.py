# Tip Calculator
# initialize the variables as empty strings, since input() returns strings
bill = ""
tip = ""
pepole = ""

print("Welcome to the tip calculator.")

while True:
    bill = float(input("What was the total bill? $ "))
    # check if it's not a negative number
    # zero is fine, as they might be eating for free
    if bill < 0:
        print("The bill can't be negative. please try again ...")
    else:
        break
while True:
    tip = input("How much tip would you like to give? 10, 12, or 15? ")
    # list of acceptable choices
    choices_list = ["10", "12", "15"]
    # make sure the input is one of them
    if tip not in  choices_list:
        print("Please enter 10, 12 or 15.")
    else:
        tip_as_int = int(tip)
        break
while True:
    people = input("How many pepole to split the bill?")
    # make sure it's a non-zero natural number
    if not people.isdigit() or people == "0":
        print("Please enter a valid number of people (1,2,3, etc.)")
    else:
        people_as_int = int(people)
        break
# get the percentage
tip_as_percent = tip_as_int /100
total_tip_amount = bill * tip_as_percent
# add the tip to the base bill
total_bill = bill + total_tip_amount
# calculate the split bill and round to 2 decimal places
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person,2)
# using a uniform message, even if there was just a single person
print(f"Each person should pay: ${final_amount}")


