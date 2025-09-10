
# 2. Write a Python function that takes an integer and checks if it is positive, negative, or zero.
# Return "Positive", "Negative", or "Zero" based on the input.

def check_sign_alt(num):
    if num > 0:
        return "Positive"
    else:
        if num < 0:
            return "Negative"
        else:
            return "Zero"


def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


print(check_sign_alt(0))
print(check_sign_alt(-1))
print(check_sign_alt(1))

