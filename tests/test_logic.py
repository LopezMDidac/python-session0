from typing import List
from src.logic import filter_users, list_avengers, list_civilian, user_already_exists

from src.user import User


def test_list_all_users_empty():
    users: List[User] = []

    listed = filter_users(users)

    assert listed is not None
    assert len(listed) == 0


def test_list_all_users_multiple(with_multiple_users: List[User]):
    listed = filter_users(with_multiple_users)

    assert listed is not None
    assert len(listed) == 3


def test_list_avengers_users_multiple(with_multiple_users):

    listed = list_avengers(with_multiple_users)

    assert listed is not None
    assert len(listed) == 2


def test_list_civilians_users_multiple(with_multiple_users):

    listed = list_civilian(with_multiple_users)

    assert listed is not None
    assert len(listed) == 1


def test_user_already_exists(with_multiple_users):

    new_user = User("new user", 22, False)
    exists = user_already_exists(with_multiple_users, new_user)

    assert exists is False


def test_user_already_exists_exsting(with_multiple_users):

    exists = user_already_exists(with_multiple_users, with_multiple_users[0])

    assert exists is True
