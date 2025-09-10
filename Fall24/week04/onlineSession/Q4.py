
# Write a Python function that checks if a number is divisible by both 3 and 5.
# If it is, return "Divisible by both". If it is only divisible by 3, return "Divisible by 3".
# If it is only divisible by 5, return "Divisible by 5".
# If it is divisible by neither, return "Not Divisible by 3 or 5".

def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:  # this has to come first, else execution will enter 3 or 5 first and terminate
        return "Divisible by both"
    elif num % 3 == 0:
        return "Divisible by 3"
    elif num % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not Divisible by 3 or 5"


