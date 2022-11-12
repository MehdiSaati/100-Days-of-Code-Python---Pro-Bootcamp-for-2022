# your life in weeks Calculator
print("Wellcome Your Life In Weeks Calcuator")
age = input(" What is your current age? ")
# Calculator months and weeks and day
age_as_int = int(age)

# we live until  90 years old.
years_remaining = 90 - age_as_int

#There are 365 days in year, 52 weeks in a year and 12 months in a year
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} , {weeks_remaining} weeks and {months_remaining} months left" 
print(message)

