import re

text = "hello_world python_code Hello_World"

result = re.findall(r"[a-z]+_[a-z]+", text)

print(result)