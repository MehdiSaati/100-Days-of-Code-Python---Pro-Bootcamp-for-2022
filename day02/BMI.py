# BMI Calculator
print("Wellcome BMI Project")
 
height = input("Enter your height in m : ")
weight = input("Enter your weight in kg :")
height_as_float = float(height)
weight_as_int = int(weight)
bmi = weight_as_int / height_as_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

