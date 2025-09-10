
# Write a Python function that takes two numbers as input.
# If both numbers are greater than zero, return "Both Positive".
# If only one number is greater than zero, return "One Positive".
# If neither number is greater than zero, return "None Positive".

def check_both_positive(num1, num2):
    if num1 > 0 and num2 > 0:  # if num1 and num2 > 0 doesn't work
        return "Both Positive"
    elif num1 > 0 or num2 > 0:
        return "One Positive"
    else:
        return "None Positive"
