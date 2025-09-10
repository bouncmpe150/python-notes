# Question 1
N = int(input("give me the length of the list: "))
my_list = []
for i in range(N):
    m = int(input("give me the element: "))
    my_list.append(m)

avg = sum(my_list)/N
print(avg, end= " ")
for element in my_list:
    if element > avg:
        print(element, end= " ")

#Question 2

def find_freq(list):
    freq_list = [0] * 101 # 0 and 100 (inclusive)
    for i in range(len(list)):
        freq_list[list[i]] += 1
    for i in range(len(freq_list)):
        if freq_list[i] != 0:
            print(i, ' --> ', freq_list[i], end="\n")


find_freq([1,4,5,67,87,1,1])



# Question 3
list = []

for _ in range(5):
    num = int(input("give me the element: "))
    list.append(num)

transformed_list = [x ** 5 for x in list]
print(transformed_list)

# Question 4
def shift_k_number(list, k):
    shift_amount = k % len(list) # check whether the given number is out of list length 
    return list[k:] + list[:k]

print(shift_k_number([1,2,3,4,5], 1))

# Question 5
def reverse(list):
    reversed_list = []
    for el in reversed(list):
        print(el, end= ' ')
        reversed_list.append(el)

    return reversed_list

print(reverse([1,3,-4,5, 2]))

# Question 6
def remove_x(list, x):
    list_without_x = []
    for i in range(len(list)):
        if list[i] != x:
            list_without_x.append(list[i])

    return list_without_x

print(remove_x([1,1,1,5,6,6,7,8], 1))
print(remove_x([45] * 10, 45))

# Question 7
def remove_dup(list):
    seen_numbers = []
    for i in range(len(list)):
        if not list[i] in seen_numbers:
            seen_numbers.append(list[i])

    return seen_numbers

print(remove_dup([1,1,1,2,3,5,5,5]))

# Question 8
def odd_occurrence(list):
    odd_element = []
    for i in range(len(list)):
        if list[i] in odd_element:
            odd_element.remove(list[i])
        else:
            odd_element.append(list[i])

    return odd_element

print(odd_occurrence([1,1,3,4,2, 'apple', 'apple', 'banana']))


# Question 9
def fraction(frac1, frac2):
    return (((frac1[0] * frac2[1]) + (frac1[1] * frac2[0])), (frac1[1] * frac2[1]))

print(fraction((1,3), (4,5)))

# Question 10a
def dist(p1, p2):
    distance_in_x_axis = p1[0]-p2[0]
    distance_in_x_axis_squared = distance_in_x_axis ** 2

    distance_in_y_axis = p1[1] - p2[1]
    distance_in_y_axis_squared = distance_in_y_axis ** 2

    squared_distance = distance_in_x_axis_squared + distance_in_y_axis_squared
    distance = squared_distance ** 0.5
    return distance

    # An alternative way to do the same thing
    # return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**0.5

print(dist((3, 0), (0, 4)))
print(dist((5, 8), (10, 20)))
print(dist((3, 6), (3, 6)))

# Question 10b
def closest(p1, p2):
    dist1 = dist(p1, (0, 0))
    dist2 = dist(p2, (0, 0))
    if dist1 < dist2:
        return p1
    else:
        return p2

print(closest((3, 0), (0, 4)))
print(closest((11, 7), (6, 8)))

# Question 10c
N = int(input())
points = []
farthest_index1, farthest_index2, max_dist = -1, -2, -6
for i in range(N):
    line = input()
    elements = line.split()
    point = (int(elements[0]), int(elements[1]))
    points.append(point)
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = dist(points[i], points[j])
        if distance > max_dist:
            max_dist = distance
            farthest_index1 = i
            farthest_index2 = j

print('Distance:', max_dist)
print('Point 1:', points[farthest_index1])
print('Point 2:', points[farthest_index2])

# Question 11
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble_sort([4, 2, 8, 6, 7, 3, 1, 5]))
#print(sorted([4, 2, 8, 6, 7, 3, 1, 5]))

print(bubble_sort([4, -2, 4, 6, -7, 3, 1, 5]))
#print(sorted([4, -2, 4, 6, -7, 3, 1, 5]))


