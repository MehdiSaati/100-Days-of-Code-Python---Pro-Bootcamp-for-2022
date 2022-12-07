#  The Great Squirrel Census Data Analysis 
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day25/Great_Squirrel_Census")
import pandas

#Count fur color
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

color_list = ["Gray", "Black", "Cinnamon"]
count_list =[gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]

squirrel_data_dict ={
    "Fur Color":color_list,
    "Count": count_list
} 
 
df = pandas.DataFrame(squirrel_data_dict)
print(df)
df.to_csv("squirrel_count.csv")




