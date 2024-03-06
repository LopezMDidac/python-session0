from typing import List
import pytest

from src.user import User


@pytest.fixture
def with_multiple_users() -> List[User]:
    users: List[User] = []
    users.append(User("IronMan", 40, True))
    users.append(User("Thanos", 400, False))
    users.append(User("BlackWidow", 30, True))
    return users
