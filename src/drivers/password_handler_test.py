from .password_handler import PasswordHandler

def test_encrypt():
    my_password = "1234R"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(my_password)
    password_checked = password_handler.check_password(my_password, hashed_password)

    assert password_checked
