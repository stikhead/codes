# Controls how the script executes and interacts with the command line.
import sys
# Run via terminal: python sys_lib.py --production
print(sys.argv) # Output: ['sys_lib.py', '--production']

database_connected = False
if not database_connected:
    sys.exit(1) # Kills the script, triggers CI/CD failure, Immediately terminates the program. Passing 1 indicates an error to the OS

sys.setrecursionlimit(1000000000000) # Python natively blocks deep recursion (usually around 1000 calls). You must increase this for Depth-First Search (DFS) on large graphs.

print(sys.executable)