from access_control import AccessControl
from users.administrator import Administrator
from users.regular_user import RegularUser

# Tests for add_user
def test_add_user_success():
    system = AccessControl()
    user = RegularUser("ivan", "1234")

    system.add_user(user)

    assert "ivan" in system.users

def test_add_user_overwrite():
    system = AccessControl()
    user1 = RegularUser("ivan", "1234")
    user2 = RegularUser("ivan", "abcd")

    system.add_user(user1)
    system.add_user(user2)

    assert system.users["ivan"] == user2


# Tests for authenticate_user
def test_authenticate_user_success():
    system = AccessControl()
    user = Administrator("admin", "admin123")

    system.add_user(user)
    result = system.authenticate_user("admin", "admin123")

    assert result == user

def test_authenticate_user_wrong_password():
    system = AccessControl()
    user = Administrator("admin", "admin123")

    system.add_user(user)
    result = system.authenticate_user("admin", "wrong")

    assert result is None

def test_authenticate_user_inactive():
    system = AccessControl()
    user = Administrator("admin", "admin123", is_active=False)

    system.add_user(user)
    result = system.authenticate_user("admin", "admin123")

    assert result is None
