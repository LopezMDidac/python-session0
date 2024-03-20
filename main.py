from typing import List
from src.logic import create_new_user, filter_users, list_avengers, user_already_exists

from src.user import User


menu_option: str = ""
users: List[User] = []

while menu_option != "4":
    print(
        """ What do you want to do?
            1. add user
            2. list all users
            3. List Avengers
            4. Exit
          """
    )
    menu_option = input()

    if menu_option == "1":
        user: User = create_new_user()
        print(user.greeting_message())
        if user_already_exists(users, user):
            print("You are already registered")
        else:
            users.append(user)
    elif menu_option == "2":
        filter_users(users)
    elif menu_option == "3":
        list_avengers(users)
    elif menu_option == "4":
        pass
    else:
        print("Invalid option")
