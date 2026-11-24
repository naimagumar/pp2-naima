i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
i = 1

while i <= 5:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1
i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

    print(i)
numbers = [1, -2, 3, -4, 5]
i = 0

while i < len(numbers):
    number = numbers[i]
    i += 1

    if number < 0:
        continue

    print(number)

i = 1

while i <= 20:
    i += 1

    if i % 5 == 0:
        continue

    print(i)