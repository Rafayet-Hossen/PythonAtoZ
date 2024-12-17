def save_user_data():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    contact = input("Enter Your Contact: ")
    with open("datasheet.txt","a") as file:
        information = f'{name}\n{email}\n{contact}\n'
        file.write(information)
def read_user_date():
    with open("datasheet.txt","r") as file:
        information = file.readlines()
        for info in information:
            print(info.strip())

while True:
    choice = input("Do you want to save your data? (y/n): ")
    if choice == "y":
        save_user_data()
    else:
        read_user_date()
        break

