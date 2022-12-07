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
print(data["temp"])
 
input(">")