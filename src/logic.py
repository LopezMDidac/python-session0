from typing import List
from src.user import User


def create_new_user() -> User:
    name: str = ""
    age: int = -1
    is_avenger: bool = False

    name = input("What is your name? ")

    raw_age = input("What is your age? ")
    age = int(raw_age)

    raw_avenger = input("Are you an avenger? (Y/N)")
    if raw_avenger.upper() == "Y":
        is_avenger = True

    user = User(name, age, is_avenger)

    return user


def list_avengers(users: List[User]) -> List[User]:
    return filter_users(users, True, False)


def list_civilian(users: List[User]) -> List[User]:
    return filter_users(users, False, True)


def filter_users(
    users: List[User], show_avengers: bool = True, show_civilians: bool = True
) -> List[User]:
    filtered_users: List[User] = []
    for user in users:
        if show_avengers and user.is_avenger:
            filtered_users.append(user)
        elif show_civilians and not user.is_avenger:
            filtered_users.append(user)
        else:
            continue
        print(user.name)
    return filtered_users
