with open('demo1.txt','r') as file:
    lines = file.readlines()

print(lines)
for line in lines:
    print(line.strip()) #strip() method remove whitespaces for a given string