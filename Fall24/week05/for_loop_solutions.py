# Question 1
def sum_of_list(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

print(sum_of_list([1,2,3,4]))

#Question 2
def reverse_str(str):
    reversed = ""

    for i in str:
        reversed = i + reversed
    return reversed

print(reverse_str("hello"))

# Question 3
def max_in_list(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest


print(max_in_list([1,2,3,4,5]))

# Question 4
def string_concat(str1, str2):
    result = ""

    for char in str1:
        result += char

    for char2 in str2:
        result += char2

    return result

print(string_concat("Cmpe ", "150"))

# Question 5
def split_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

print(split_even_odd([1,2,3,4,5]))

# Question 6
def cumulative_sum(numbers):
    cum_sum = []
    total = 0
    for num in numbers:
        total += num
        cum_sum.append(total)
    return cum_sum

print(cumulative_sum([1,2,3,4]))

# Question 7
def print_number_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end= " ")
        print()

print_number_pattern(5)

# Question 8
def digital_clock(second_limit):
    for hour in range(60):
        for min in range(60):
            for sec in range(60):
                current_seconds = hour*3600 + min*60 + sec
                if current_seconds > second_limit:
                    return
                print(f"{hour:02} hello :{min:02}:{sec:02}")

digital_clock(45)

# Question 9
def print_pascals_triangle(n):
    triangle = []

    for i in range(n):
        # The first and last elements of each row in Pascal's Triangle are always 1.
        row = [1] * (i + 1)  # Create a row with i + 1 elements, all initialized to 1.
        if i > 1:
            for j in range(1, i):
               # Each number is the sum of the two above it
               # triangle[i - 1][j - 1]: This is the element just to the left above.
               # triangle[i - 1][j]: This is the element directly above.
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

tri = print_pascals_triangle(6)
n = len(print_pascals_triangle(6))
for i in range(n):
    print(" "* (n-i), end= " ", sep = " ")
    for j in range(0, i+1):
        print(tri[i][j], end= " ", sep = " ")
    print("")

# Question 10
def checkerboard(n):
    for i in range(n): #rows
        for j in range(n): #columns
            if (i+j) % 2 == 0:
                print("X", end= " ")
            else:
                print("O", end= " ")

        print()

checkerboard(5)




