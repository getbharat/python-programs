from math_helper import add, multiply, subtraction, division

# from import *
# import math_helper

user_input = input("Input 2 number for addition separated by ','\n")
nums = user_input.split(",")

# print(math_helper.add(nums[0], nums[1]))
print(add(nums[0], nums[1]))
