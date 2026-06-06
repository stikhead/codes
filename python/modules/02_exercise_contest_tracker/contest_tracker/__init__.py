# Use relative imports to pull functions from the submodules into the package namespace
from .api import fetch_upcoming
from .parser import format_times

# Optional but strictly Pythonic: Define __all__ to explicitly declare the public API
# This controls what gets exported if someone uses `from contest_tracker import *`
__all__ = ["fetch_upcoming", "format_times"]

# Why This Matters
# we you didn't have the __init__.py set up this way, whoever is writing main.py would have to know our internal file structure and write:
from contest_tracker.api import fetch_upcoming
from contest_tracker.parser import format_times
# By controlling the namespace at the __init__.py level, we abstract away the complexity. 
# we are completely free to refactor, rename, or split api.py into ten different files later,
# and main.py will never break because the top-level import contract remains identical.