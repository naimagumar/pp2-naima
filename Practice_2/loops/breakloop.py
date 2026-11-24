i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1
while True:
    text = input("Enter something: ")

    if text == "exit":
        break

    print(text)
i = 1

while i <= 100:
    if i % 7 == 0:
        print("Found:", i)
        break

    i += 1
number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct!")
        break

    print("Try again!")
