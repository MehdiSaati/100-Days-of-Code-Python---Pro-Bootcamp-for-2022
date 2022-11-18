# Area Calc Exercise
import math
test_h = int(input("Height of wall : "))
test_w = int(input("Width of wall  : "))
coverage = 5
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    number_of_cans_round = math.ceil(number_of_cans)
    print(f"You'll need{number_of_cans_round} cans of paint")
paint_calc(height = test_h, width = test_w, cover = coverage)
input("<")