import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)

print(y)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, sort_keys=True))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


print(json.dumps(x, indent=4, sort_keys=True))
import json


x = '{"name": "Emil", "age": 30}'


y = json.loads(x)

print(y["age"])

import json

emp = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(emp))

print("Now convert from JSON to Python")
d = json.loads(emp)
print("Converted to Python", type(d))
print(d)

import json

# JSON Syntax
json_text = '{"name": "Naima", "age": 18, "student": true}'

# Parsing JSON (loads)
data = json.loads(json_text)
print("Python object:", data)

# Converting Python to JSON (dumps)
json_string = json.dumps(data)
print("JSON string:", json_string)

# Writing JSON Files
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON Files
with open("data.json", "r") as file:
    info = json.load(file)

print("Read from file:", info)

# Working with JSON data
print("Name:", info["name"])
print("Age:", info["age"])
print("Student:", info["student"])