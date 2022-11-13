# BMI Calculator version 2.0
print("Wellcome BMI v2.0")
 
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg :"))

bmi = weight/ height ** 2
bmi_as_round = round(bmi)
if bmi_as_round < 18.5:
    print(f"Your BMI is :{bmi_as_round}, you are Underweight.")
elif bmi_as_round < 25:
    print(f"Your BMI is :{bmi_as_round}, you are Normalweight.")
elif bmi_as_round < 30:
    print(f"Your BMI is :{bmi_as_round}, you are Overweight.")
elif bmi_as_round < 35:
    print(f"Your BMI is :{bmi_as_round}, you are Obese.")
else:
    print(f"Your BMI is :{bmi_as_round}, you are Clinically obese.")

