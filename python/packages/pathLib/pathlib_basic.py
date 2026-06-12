# For a long time, Python developers used os.path to mash strings together to create file paths (e.g., os.path.join(dir, file)). 
# pathlib changes that by treating file paths as objects instead of plain strings, making your code cleaner and cross-platform (Windows vs. Mac/Linux) by default.

from pathlib import Path
curr_dir = Path.cwd() # current working directory

data_folder = curr_dir/"data"/"exports" # create a new path using '/' operator

# create the directory if it doesnt exist
data_folder.mkdir(parents=True, exist_ok=True)

# new file inside that folder
my_file = data_folder/"report.txt"

# writing and reading text
my_file.write_text("hello patjlib!")
print(my_file.read_text())

# check file properties
print(f"exists? {my_file.exists()}")
print(f"extension: {my_file.suffix}")