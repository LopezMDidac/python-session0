from typing import List
from src.logic import create_new_user, filter_users, list_avengers

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
        ## check if user name already exists
        ## if true. Dont create a new one. Prompt the user that it is already registered
        ## make the unit test
        users.append(user)
    elif menu_option == "2":
        filter_users(users)
    elif menu_option == "3":
        list_avengers(users)
    elif menu_option == "4":
        pass
    else:
        print("Invalid option")
