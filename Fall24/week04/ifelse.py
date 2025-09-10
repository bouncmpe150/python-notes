

file_name = input()

# Received a, b, and c as floating point numbers from the user,
# DO NOT write any prompt messages inside the input functions.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print("a: %.2f, b: %.2f, c: %.2f" % (a,b,c) )

# Define the required functions in the following section.
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
print(calculate_1st_degree_root())

delta = calculate_delta()

import math

if delta > 0:

# Calculate x1 to be -b + square root of delta / 2a
# and x2 to be -b - square root of delta / 2a
# print their respective values

# Be careful about the indentation
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
    print("%.3f, %.3f" % (x1, x2))

elif delta == 0:
#Calculate x as a single root. Be careful about the indentation
#----------------------------------------------------------------
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
#----------------------------------------------------------------
    print( "%.3f" % x)
else:
    print("No real roots")



