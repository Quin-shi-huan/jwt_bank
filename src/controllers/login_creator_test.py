import pytest
from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator

USERNAME = "myUsername"
PASSWORD = "myPassword"

hashed_password = PasswordHandler().encrypt_password(PASSWORD)

class MockUserRepository:
    def get_user_by_username(self, username):
        return(10, username, hashed_password)

def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(USERNAME, PASSWORD)

    assert response["access"] is True
    assert response["username"] == USERNAME
    assert response["token"] is not None

def test_create_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(USERNAME, "Incorrect Password")
