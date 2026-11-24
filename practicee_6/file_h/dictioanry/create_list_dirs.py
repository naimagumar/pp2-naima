
import os

os.makedirs("folder1/folder2", exist_ok=True)

print(os.listdir("."))

for item in os.listdir("."):
    if os.path.isdir(item):
        print("Directory:", item)
    elif os.path.isfile(item):
        print("File:", item)



