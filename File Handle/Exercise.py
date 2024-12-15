while True:
    with open('names.txt','a') as file:
        name = input("Enter your name:")
        file.write(f'{name}\n')
        choice = input("Do you want to add another name:y/n")
        if choice == 'n':
            break

with open('names.txt','r') as file:
    names = file.readlines()

with open('names.txt','w') as file:
    for name in names:
        file.write(name.capitalize())

with open('names.txt','r') as file:
    names = file.readlines()
for name in names:
    print(name.strip())