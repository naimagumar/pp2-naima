def my_func(fname):
    print(fname + " Refsnes")
my_func("emil")
my_func("tobias")
my_func("linus")

def my_function(name):
  print("Hello", name)

my_function("Emil")

def my_func(fname, lname):
   print(fname + " " + lname)
my_func("emil", "tobias")
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_func(country = "Norway"):
   print("i am from", country)

my_func("sweden")
my_func("india")
my_func()
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
def my_function(name):
  print("Hello", name)

my_function("Emil")
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)