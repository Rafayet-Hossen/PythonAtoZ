#Meta Characters
import re

string = "bc"

pattern = "ab*c"

if re.match(pattern,string):
    print("Match pattern")
else:
    print("No Match Pattern")    