# Split Sentence and lenght of words
sentence = "What is the Airspeed Velocity of an unladen Swallow?"

# https://www.w3schools.com/python/ref_string_split.asp
words_list = sentence.split()
print(words_list)

# dict = {new_key:new_value for item in list}
result = {word:len(word) for word in words_list}

print(result)
input(">")