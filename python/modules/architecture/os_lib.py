# Handles file systems, directories, and environment variables.
import os
from dotenv import load_dotenv

load_dotenv()
db_pass = os.getenv('password' , 'default')
print( db_pass)

filepath = os.path.join("folder", "logs", "error.txt")
print(filepath)