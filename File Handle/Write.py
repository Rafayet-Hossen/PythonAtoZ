# file = open("demo1.txt","a")
# file.write("\nThis is the third line")
# file.close()

with open('demo1.txt','r') as file:
    contents = file.read()
    print(contents)