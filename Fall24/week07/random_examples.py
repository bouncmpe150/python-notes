import random

# # 1. random() - Generate a random floating-point number between 0.0 and 1.0
print("random():", random.random())

# 2. randint(a, b) - Generate a random integer between a and b (inclusive)
print("randint(1, 10):", random.randint(-10, 10))

# 3. uniform(a, b) - Generate a random floating-point number between a and b
print("uniform(1, 10):", random.uniform(10, 100))

# 4. choice(seq) - Pick a random element from a non-empty sequence
colors = ['red', 'green', 'blue', 'yellow']
print("choice(colors):", random.choice(colors))

# 5. choices(population, k=n) - Pick n random elements with replacement (duplicates allowed)
print("choices(colors, k=10):", random.choices(colors, k=10))

# 6. sample(population, k=n) - Pick n unique elements without replacement
numbers = list(range(1, 11))
print("sample(numbers, k=3):", random.sample(numbers, k=5))

# 7. shuffle(x) - Shuffle the list in place
random.shuffle(numbers)
print("shuffle(numbers):", numbers)

# 8. randrange(start, stop, step) - Pick a random number from range(start, stop, step)
print("randrange(0, 100, 10):", random.randrange(0, 100, 3))
