# New Dictionary for Weather temp change
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "saturday": 22,
    "Sunday": 24
}
print(weather_c)
# new_dict = {new_key:new_value for (key,value) in dictionary.items()}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
input(">")