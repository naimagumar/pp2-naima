
import os
import shutil
from pathlib import Path

# os: get the current working directory
print("Current directory:", os.getcwd())

# Create a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")

# shutil: copy a file
shutil.copy("example.txt", "copy.txt")
print("File copied")

# pathlib: work with file paths
path = Path("example.txt")
print("File exists:", path.exists())
print("File name:", path.name)
print("File suffix:", path.suffix)

# Delete the copied file
os.remove("copy.txt")
print("Copy deleted")
