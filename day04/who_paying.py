# Who's Paying?
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Spliting string method
namesASCSV = input("Give me everybody\'s name, seperated by a coma. ")
names = namesASCSV.split(", ")

# # Get the total number of items in list.
# num_items = len(names)
# # Generate random number between 0 the last item in list
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to by the meal today" )
