# Adding Even Numbers
total_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_number += number
print(total_number)

# other ways
total_number2 = 0
for number in range(2, 101, 2):
    total_number2 += number
print(total_number2)
 