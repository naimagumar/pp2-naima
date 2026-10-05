import re

text = "abb"

result = re.fullmatch(r"ab*", text)

if result:
    print("Match")
else:
    print("No match")