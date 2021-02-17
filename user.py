class User:
    user_count = 0

    def __init__(self, username, password, email):
        self.user_id = User.generate_user_id()
        self.username = username
        self.password = password
        self.email = email
        self.user_count += 1
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = True

    
    def generate_user_id():
        return User.user_count + 1

    def create_user(username, password, email):
        new_user = User(username, password, email
        )
    
    def get_id():
        return self.user_id

