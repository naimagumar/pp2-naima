
names = ["Aliya", "Dana", "Miras"]
scores = [90, 85, 95]

for index, name in enumerate(names):
    print(index, name)

for name, score in zip(names, scores):
    print(name, score)



value = "123"

print(type(value))
print(isinstance(value, str))

number = int(value)
decimal = float(value)
text = str(number)

print(number, type(number))
print(decimal, type(decimal))
print(text, type(text))
