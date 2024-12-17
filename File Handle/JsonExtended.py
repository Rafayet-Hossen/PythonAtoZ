import json
import os
user_list = []

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