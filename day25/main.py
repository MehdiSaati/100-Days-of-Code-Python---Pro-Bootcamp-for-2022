import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day25")

# with open("weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
    
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

#convert to dictionary
data_dict = data.to_dict()
print(data_dict)

#convert to list
temp_list = data["temp"].to_list()

# average columns - temp

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
print(data["temp"].mean())

#Max in columns by series method
print(data["temp"].max())

#Get Data in columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data["day"] == "Monday"])


# Get maximum temp row data
max_temp = data.temp.max()
print(data[data.temp == max_temp])


monday = data[data.day == "Monday"]
print(monday.condition)

# convert celsius to fahrenheit
monday_Celsius = int(monday.temp)
monday_Fahrenheit = 9.0/5.0 * monday_Celsius + 32
print(f"Temperature:{monday_Celsius} Celsius , {monday_Fahrenheit} F") 

# Create dataframe from scratch
data_student_dict ={
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_student_dict)
print(data)
data.to_csv("new_data.csv")
