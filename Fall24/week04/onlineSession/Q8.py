
# Sum of Digits: Write a recursive function that takes a positive integer n
# and returns the sum of its digits.
# For example, if the input is 123, the output should be 1 + 2 + 3 = 6

def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  # Recursive call


print(1357/10)
print(1357//10)
print(1357 % 10)

print(sum_of_digits(1357))
