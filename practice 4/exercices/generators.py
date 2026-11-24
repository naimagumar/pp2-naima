# 1
def gen_squares(n):
    for i in range(n + 1):
        yield i * i

# 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)

# 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("n = "))

print("1. Squares up to N:")
for x in gen_squares(n):
    print(x, end=" ")
print()

print("2. Even numbers:")
print(",".join(even_numbers(n)))

print("3. Divisible by 3 and 4:")
for x in divisible_by_3_and_4(n):
    print(x, end=" ")
print()

a = int(input("a = "))
b = int(input("b = "))

print("4. Squares from a to b:")
for x in squares(a, b):
    print(x, end=" ")
print()

print("5. Countdown:")
for x in countdown(n):
    print(x, end=" ")