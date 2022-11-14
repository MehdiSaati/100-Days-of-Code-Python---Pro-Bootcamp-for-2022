# treasure map by list
row1 = ["-","-","-"]
row2 = ["-","-","-"]
row3 = ["-","-","-"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do want to put the treasure?")

horizanl = int(position[0])
vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizanl - 1] = "X"
map[vertical - 1][horizanl - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
 
