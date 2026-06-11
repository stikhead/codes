import re
text = "User email is test@student.edu"
# re.search(regex, string) finds the first occurance of a pattern
match = re.search(r"[\w.-]+@[\w.-]+", text)
if match:
    print(match.group())


# re.sub(regex, replace, string) strips all non alphanumeric characters from a messy string
clean = re.sub(r"[^\w\s]", "", "Hello!!! world???")
print(clean)