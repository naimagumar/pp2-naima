import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

import re

txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x)

import re

txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
import re

txt = "hello planet"

x = re.findall("he..o", txt)
print(x)
import re

txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

import re

txt = "hello planet"

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
import re

txt = "hello planet"


x = re.findall("he.*o", txt)

print(x)

import re

txt = "hello planet"

print(x)

import re

txt = "hello planet"



x = re.findall("he.{2}o", txt)

print(x)

import re

txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "The rain in Spain"

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "The rain in Spain"

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"


x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#sets
import re

txt = "The rain in Spain"


x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "The rain in Spain"

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "The rain in Spain"



x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


import re

txt = "The rain in Spain"

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "8 times before 11:45 AM"


x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


import re

txt = "8 times before 11:45 AM"


x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
import re

txt = "8 times before 11:45 AM"


x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())