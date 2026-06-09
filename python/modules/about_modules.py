# in python, modules are objects that contains all the functions, classes, variables defined in module. 
# python executes the module file from top to bottom creating module objects

# this in database.py
def connect_db():
    print("connected to db")

db_url = "mongodb://localhost:27017"

# then in another file we can do
import database
# and call the function defined in database.py file
database.connect_db()
print(database.db_url)



# three ways to import modules in python
# 1. safest method:
import math # it keeps all the imported functions inside math namespace
math.sqrt(2)

# 2. a little convinient for constantly used functions
from math import sqrt # we can use sqrt() directly without the need of math
sqrt(2)

# 3. wildcard ( dont use this )
from math import * # dumps everything from math module into the file we are working in, possible leading to namespace errors and making debugging harder


# packages: modules of modules
# when the project grows, we simply group the modules into packages
# a package is simply a directory containing .py files

### important:
# Historically, Python required a file named __init__.py inside a directory to recognize it as a package. 
# While modern Python (3.3+) can work without it, it is still the industry standard to include an empty __init__.py. 
# It signals to other developers (and your IDE) that "this folder is a Python package."

# my_backend/
# │
# ├── main.py
# └── api/                <-- This is a package
#     ├── __init__.py     
#     ├── routes.py       <-- This is a module
#     └── auth.py         <-- This is a module

#To import from this structure: 
# from api.routes import handle_request
# OR
# import api.routes
import dsa.arrays.arrayADT
dsa.arrays.arrayADT.myArray


# golden rule: if __name__ == "__main__":
# bc importing a file executes the module, we need a way to stop certain code from running if the file is being imported as a utility
# python automatically assign a special variable __name__ to the string "__main__" only if file is executed directly by python interpreter

# scraper.py
def fetch_data():
    return "Data fetched!"

# This block ONLY runs if you type `python scraper.py` in the terminal.
# It gets ignored if another file does `import scraper`.
if __name__ == "__main__":
    print("Testing the scraper locally...")
    print(fetch_data())

### this allows to create tools that can be run as standalone background process and cleanly imported as modules