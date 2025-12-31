from users.user import User
from users.administrator import Administrator
from users.regular_user import RegularUser
from users.guest_user import GuestUser

# Tests for User
def test_verify_password_correct():
    user = User("test", "1234")
    assert user.verify_password("1234") is True

def test_verify_password_wrong():
    user = User("test", "1234")
    assert user.verify_password("wrong") is False

# Tests for Administrator
def test_admin_add_permission():
    admin = Administrator("admin", "admin123")
    admin.add_permission("manage_users")
    assert "manage_users" in admin.permissions

def test_admin_permissions_initially_empty():
    admin = Administrator("admin", "admin123")
    assert admin.permissions == []

# Tests for RegularUser
def test_regular_user_last_login_default():
    user = RegularUser("ivan", "qwerty")
    assert user.last_login is None

def test_regular_user_is_active():
    user = RegularUser("ivan", "qwerty")
    assert user.is_active is True

# Tests for GuestUser
def test_guest_user_limited_access():
    guest = GuestUser("guest")
    assert guest.limited_access is True

def test_guest_user_default_password():
    guest = GuestUser("guest")
    assert guest.verify_password("guest") is True
