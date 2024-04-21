import pytest
from user import UserManager, User

@pytest.fixture
def user_manager():
    return UserManager()

def test_generate_id(user_manager):
    id_set = set()
    for _ in range(10):
        new_id = user_manager.generate_id()
        assert new_id not in id_set
        id_set.add(new_id)

def test_create_a_user(user_manager):
    user_manager.create_a_user("Rataj", "password", "student")
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == "Rataj"
    assert user_manager.user_list[0].password == "password"
    assert user_manager.user_list[0].user_type == "student"

def test_find_users(user_manager):
    user_manager.create_a_user("Jiang", "password1", "teacher")
    user_manager.create_a_user("Ammar", "password2", "student")
    user_manager.create_a_user("Rami", "password3", "admin")

    users_found = user_manager.find_users([1, 3])
    assert len(users_found) == 2
    assert users_found[0].name == "Jiang"
    assert users_found[1].name == "Rami"

    users_found = user_manager.find_users([4])
    assert len(users_found) == 0

    users_found = user_manager.find_users([])
    assert len(users_found) == 0

