import json


def load_users():
    """Load and return users from users.json."""
    with open("users.json", "r") as file:
        return json.load(file)


def print_users(users):
    """Print each user dict on its own line."""
    for user in users:
        print(user)


def filter_users_by_name(name):
    """Print users whose name matches (case-insensitive)."""
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    print_users(filtered_users)


def filter_users_by_age(age):
    """Print users whose age equals the provided integer age."""
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    """Print users whose email matches (case-insensitive)."""
    users = load_users()
    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    print_users(filtered_users)


def main():
    prompt = (
        "What would you like to filter by? "
        "(Currently, 'name', 'age', and 'email' are supported): "
    )
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        if not name_to_search:
            print("No name provided.")
            return
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_raw = input("Enter an age to filter users: ").strip()
        if not age_raw:
            print("No age provided.")
            return
        try:
            age_to_search = int(age_raw)
        except ValueError:
            print("Age must be an integer.")
            return
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        if not email_to_search:
            print("No email provided.")
            return
        filter_users_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()

