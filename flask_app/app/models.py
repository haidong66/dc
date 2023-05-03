from flask_login import UserMixin

class User(UserMixin):
    id = 1
    username = "haidong"

    @classmethod
    def get(cls, user_id):
        if int(user_id) == cls.id:
            return cls()
        return None

    @classmethod
    def get_by_username(cls, username):
        if username == cls.username:
            return cls()
        return None
