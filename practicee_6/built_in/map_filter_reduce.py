
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)
from functools import reduce

numbers = [5, 2, 8, 1, 4]

# len(): number of elements
print("Length:", len(numbers))

# sum(): sum of elements
print("Sum:", sum(numbers))

# min(): smallest element
print("Minimum:", min(numbers))

# max(): largest element
print("Maximum:", max(numbers))

# map(): apply a function to every element
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# filter(): select elements that satisfy a condition
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# reduce(): combine elements into one result
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# enumerate(): get index and value
for index, number in enumerate(numbers):
    print(index, number)

# zip(): combine corresponding elements
names = ["Aliya", "Dana", "Miras"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(name, score)

# sorted(): sort elements
print("Sorted:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# Type conversion
text = "123"
integer = int(text)
decimal = float(text)
string = str(integer)

print(integer, type(integer))
print(decimal, type(decimal))
print(string, type(string))
print("Boolean:", bool(integer))
