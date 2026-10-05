import re

text = "Hello Python apple WORLD"

result = re.findall(r"[A-Z][a-z]+", text)

print(result)