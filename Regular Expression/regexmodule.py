import re

str = "abc"

pattern = "a"

if re.match(pattern,str):
    print("Match pattern")
else:
    print("No Match Pattern")    