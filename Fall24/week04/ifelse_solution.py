
file_name = input()

# Received a, b, and c as floating point numbers from the user file,
# Assume that each value is in a single line
# DO NOT write any prompt messages inside the input functions.
#-------------------------------------------------------------------------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

file = open(file_name)

a = float(file.readline())
b = float(file.readline())
c = float(file.readline())

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#-------------------------------------------------------------------------------------------------------------------------------
print("a: %.2f, b: %.2f, c: %.2f" % (a,b,c) )

# Define the required functions in the following section.
# HINT: There should be three functions: calculate_1st_degree_root, calculate_delta, calculate_2nd_degree_value
#-------------------------------------------------------------------------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def  calculate_1st_degree_root():
    return -b/a

def calculate_delta():
    delta = b*b - 4*a*c
    return delta

def calculate_2nd_degree_value(user_x_value):
    x = float(user_x_value)
    return a * x * x   +    b * x    +    c


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#-------------------------------------------------------------------------------------------------------------------------------
print(calculate_1st_degree_root())

delta = calculate_delta()

import math

if delta > 0:

# Calculate x1 to be -b + square root of delta / 2a
# and x2 to be -b - square root of delta / 2a
# you can use math.sqrt for square root operation
# print their respective values

# Be careful about the indentation
#-------------------------------------------------------------------------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Delta is greater than 0 ")
    print(calculate_2nd_degree_value(x1))
    print(calculate_2nd_degree_value(x2))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#-------------------------------------------------------------------------------------------------------------------------------
    print("%.3f, %.3f" % (x1, x2))

elif delta == 0:
#Calculate x as a single root. Be careful about the indentation
#-------------------------------------------------------------------------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    x = -1*b / (2*a)
    print("Delta is  0 ")
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#-------------------------------------------------------------------------------------------------------------------------------
    print( "%.3f" % x)
else:
    print("No real roots")


