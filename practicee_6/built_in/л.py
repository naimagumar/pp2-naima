
import os
import shutil
from functools import reduce
from pathlib import Path
import string

# Create a main folder for all exercises
base_dir = "python_practice"
os.makedirs(base_dir, exist_ok=True)

files_dir = os.path.join(base_dir, "files")
backup_dir = os.path.join(base_dir, "backup")
nested_dir = os.path.join(base_dir, "folder1", "folder2")

os.makedirs(files_dir, exist_ok=True)
os.makedirs(backup_dir, exist_ok=True)
os.makedirs(nested_dir, exist_ok=True)


# ==================================================
# PART 1. FILE HANDLING
# ==================================================

print("\n--- PART 1: FILE HANDLING ---")

file_path = os.path.join(files_dir, "sample.txt")

# 1. Create a text file and write sample data
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.\n")
    file.write("File handling practice.\n")

# 2. Read and print file contents
print("\nFile contents:")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())

# 3. Append new lines and verify content
with open(file_path, "a", encoding="utf-8") as file:
    file.write("New line 1\n")
    file.write("New line 2\n")

print("Content after appending:")
with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())

# 4. Copy and back up files using shutil
copy_path = os.path.join(files_dir, "sample_copy.txt")
backup_path = os.path.join(backup_dir, "sample_backup.txt")

shutil.copy2(file_path, copy_path)
shutil.copy2(file_path, backup_path)

print("File copied and backup created.")

# 5. Delete files safely
delete_path = os.path.join(files_dir, "sample_copy.txt")

if os.path.exists(delete_path) and os.path.isfile(delete_path):
    if os.access(delete_path, os.W_OK):
        os.remove(delete_path)
        print("Copy deleted safely.")
    else:
        print("No permission to delete the copy.")
else:
    print("File does not exist or is not a regular file.")


# ==================================================
# PART 2. DIRECTORY EXERCISES
# ==================================================

print("\n--- PART 2: DIRECTORIES ---")

# 1. Create nested directories
os.makedirs(nested_dir, exist_ok=True)
print("Nested directories created.")

# 2. List files and folders
print("\nItems in the main folder:")
print(os.listdir(base_dir))

# 3. Find files by extension
print("\nText files:")
for root, dirs, files in os.walk(base_dir):
    for name in files:
        if name.endswith(".txt"):
            print(os.path.join(root, name))

# 4. Move/copy files between directories
move_source = os.path.join(files_dir, "move_me.txt")
move_destination = os.path.join(backup_dir, "move_me.txt")

with open(move_source, "w", encoding="utf-8") as file:
    file.write("This file will be moved.")

# Copy the file
shutil.copy2(move_source, os.path.join(backup_dir, "move_me_copy.txt"))

# Move the original file
shutil.move(move_source, move_destination)

print("File copied and moved.")


# ==================================================
# PART 3. BUILT-IN FUNCTIONS
# ==================================================

print("\n--- PART 3: BUILT-IN FUNCTIONS ---")

numbers = [1, 2, 3, 4, 5, 6]

# 1. map(): apply a function to every item
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# filter(): select items that satisfy a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 2. reduce(): combine all items into one result
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)

# 3. enumerate(): get index and value
print("\nUsing enumerate:")
for index, value in enumerate(numbers):
    print(index, value)

# zip(): iterate through lists in pairs
names = ["Ali", "Dana", "Ayan"]
scores = [90, 85, 95]

print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

# 4. Type checking and conversions
value = "123"

print("\nType checking and conversions:")
print("Original value:", value)
print("Type:", type(value))

number = int(value)
decimal_number = float(value)

print("As integer:", number, type(number))
print("As float:", decimal_number, type(decimal_number))
print("As string:", str(number), type(str(number)))
print("Is number an integer?", isinstance(number, int))


# ==================================================
# PART 4. FILES AND DIRECTORIES COMBINED
# ==================================================

print("\n--- PART 4: FILES AND DIRECTORIES ---")

# 1. List only directories, only files, and all items
specified_path = base_dir

if os.path.isdir(specified_path):
    items = os.listdir(specified_path)

    only_directories = [
        name for name in items
        if os.path.isdir(os.path.join(specified_path, name))
    ]

    only_files = [
        name for name in items
        if os.path.isfile(os.path.join(specified_path, name))
    ]

    print("Directories only:", only_directories)
    print("Files only:", only_files)
    print("All items:", items)
else:
    print("Specified path is not a directory.")

# 2. Check existence, readability, writability, executability
print("\nAccess checks:")
print("Exists:", os.path.exists(specified_path))
print("Readable:", os.access(specified_path, os.R_OK))
print("Writable:", os.access(specified_path, os.W_OK))
print("Executable:", os.access(specified_path, os.X_OK))

# 3. Check path and find filename and directory portion
path_to_check = file_path

if os.path.exists(path_to_check):
    print("\nPath exists:", path_to_check)
    print("Filename:", os.path.basename(path_to_check))
    print("Directory:", os.path.dirname(path_to_check))
else:
    print("Path does not exist.")

# 4. Count the number of lines in a text file
with open(file_path, "r", encoding="utf-8") as file:
    line_count = sum(1 for line in file)

print("\nNumber of lines:", line_count)

# 5. Write a list to a file
my_list = ["Apple", "Banana", "Orange"]
list_path = os.path.join(files_dir, "list.txt")

with open(list_path, "w", encoding="utf-8") as file:
    for item in my_list:
        file.write(item + "\n")

print("List written to file.")

# 6. Generate 26 text files: A.txt to Z.txt
alphabet_dir = os.path.join(base_dir, "alphabet")
os.makedirs(alphabet_dir, exist_ok=True)

for letter in string.ascii_uppercase:
    alphabet_file = os.path.join(alphabet_dir, letter + ".txt")
    with open(alphabet_file, "w", encoding="utf-8") as file:
        file.write("This is file " + letter)

print("Created A.txt through Z.txt.")

# 7. Copy contents of one file to another
source_file = file_path
destination_file = os.path.join(files_dir, "content_copy.txt")

with open(source_file, "r", encoding="utf-8") as source:
    content = source.read()

with open(destination_file, "w", encoding="utf-8") as destination:
    destination.write(content)

print("File contents copied.")

# 8. Delete a file by specified path after checking access
path_to_delete = os.path.join(files_dir, "delete_me.txt")

# Create a test file so the example can be run
with open(path_to_delete, "w", encoding="utf-8") as file:
    file.write("This file is created for the deletion exercise.")

if os.path.exists(path_to_delete):
    if os.path.isfile(path_to_delete):
        if os.access(path_to_delete, os.W_OK):
            try:
                os.remove(path_to_delete)
                print("File deleted successfully.")
            except OSError as error:
                print("Could not delete file:", error)
        else:
            print("File is not writable.")
    else:
        print("The specified path is not a file.")
else:
    print("File does not exist.")

print("\nAll exercises completed.")
