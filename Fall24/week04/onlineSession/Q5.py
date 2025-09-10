
# Write a Python function that takes three integers as input and determines if they can form a valid triangle.
# A triangle is valid if the sum of any two sides is greater than the third side.
# If the sides form a valid triangle, return the type of triangle based on its sides:
# "Equilateral" if all three sides are equal.
# "Isosceles" if exactly two sides are equal.
# "Scalene" if all sides are different.
# If the sides do not form a valid triangle, return "Not a valid triangle".

def triangle_type(a, b, c):
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Check for the type of triangle
        if a == b == c:
            return "Equilateral"
        elif a == b or b == c or a == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a valid triangle"


print(triangle_type(3, 4, 5))
