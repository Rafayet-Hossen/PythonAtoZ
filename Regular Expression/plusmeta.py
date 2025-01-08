import re

string = "aac"
pattern = "a{2}c"

if re.match(pattern,string):
    print("Match pattern")
else:
    print("No Match Pattern")    