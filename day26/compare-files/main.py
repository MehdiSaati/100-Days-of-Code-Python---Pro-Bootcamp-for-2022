# Compare 2 file by List Comprehension
import os
os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day26/compare-files")

with open("file1.txt") as file1:
    file_1_data = file1.readlines()
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
# result = [new_item for item in list if test]
result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

