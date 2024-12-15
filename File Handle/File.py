#file handling
file = open('data.txt', 'r')
content = file.readline()
print(content)
file.close()