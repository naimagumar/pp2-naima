
import shutil
import os

os.makedirs("destination", exist_ok=True)

with open("example.txt", "w") as file:
    file.write("Hello!")

shutil.copy("example.txt", "destination/example.txt")
print("File copied")


