class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.username] = user

    def authenticate_user(self, username, password):
        user = self.users.get(username)

        if user and user.verify_password(password) and user.is_active:
            return user
        return None
