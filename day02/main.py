# Tip Calculator
# initialize the variables as empty strings, since input() returns strings
bill = ""
tip = ""
pepole = ""

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $ "))
tip = int(input("Wath percentage tip woud you like to give? 10, 12, or 15? "))
pepole = int(input("How many pepole to split the bill?"))

# get the percentage
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
# add the tip to the base bill
total_bill = bill + total_tip_amount
# calculate the split bill and round to 2 decimal places
bill_per_person = total_bill / pepole
final_amount = round(bill_per_person,2)
# using a uniform message, even if there was just a single person
print(f"Each person should pay: ${final_amount}")

