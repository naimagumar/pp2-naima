
import os

file_path = os.path.join(os.path.dirname(__file__), "demofile.txt")

if os.path.exists(file_path):
    os.remove(file_path)
    print("The file has been deleted")
else:
    print("The file does not exist")
