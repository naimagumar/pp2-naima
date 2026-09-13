fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
for i in range(1, 11):
    if i == 5:
        break

    print(i)
numbers = [1, 2, 3, 7, 9]

for number in numbers:
    if number == 7:
        print("Found!")
        break

    print(number)
fruits = ["banana", "orange", "apple", "grape"]

for fruit in fruits:
    if fruit == "apple":
        break

    print(fruit)
for i in range(1, 10):
    if i % 2 == 0:
        break

    print(i)