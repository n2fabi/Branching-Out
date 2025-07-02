import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def  filter_users_by_age(age_min, age_max):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if age_min < user["age"] < age_max]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name','email' and 'age' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_min = int(input("Enter a minimum age to filter users: ").strip())
        age_max = int(input("Enter a maximum age to filter users: ").strip())
        filter_users_by_age(age_min, age_max)

    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_users_by_name(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
