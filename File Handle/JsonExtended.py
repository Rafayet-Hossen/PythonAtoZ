import json
import os
user_list = []

def read_user_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as f:
            load_date = json.load(f)
            for info in load_date:
                print(info['name'])
                print(info['email'])
                print(info['contact'])


while True:
    name = input("Enter (exit) means Exit else Enter Name: ")
    if name == "exit":
        break
    email = input("Enter Email Address: ")
    contact = input("Enter Contact Number: ")
    user_data = {
        "name": name,
        "email": email,
        "contact": contact
    }
    user_list.append(user_data)

    try:
        with open("user_data.json", "w") as file:
            json.dump(user_list, file)
        print("User Data Saved Successfully")
    except FileNotFoundError as error:
        print(error)

read_user_data()