import json


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


def print_users(users):
    for user in users:
        print(user)


def filter_users_by_name(name):
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    print_users(filtered_users)


def filter_users_by_age(age):
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    users = load_users()
    filtered_users = [
        user for user in users if user["email"].lower() == email.lower()
    ]
    print_users(filtered_users)


def main():
    prompt = (
        "What would you like to filter by? "
        "(Currently, 'name', 'age', and 'email' are supported): "
    )
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
