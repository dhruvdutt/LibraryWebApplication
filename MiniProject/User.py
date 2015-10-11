from flask_login import LoginManager,UserMixin,current_user,login_user,logout_user
from werkzeug.security import check_password_hash,generate_password_hash
from MiniProject import login_manager,client

db = client.calibrary

class UserNotFoundError(Exception):
    pass
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    @classmethod
    def get(self_class,id):
        user = db.users.find_one({"username":id})
        if not user:
            return None
        return self_class(id)
        
    @staticmethod
    def validate_login(password):
        if password == "admin":
            return True
        else:
            return False

@login_manager.user_loader
def load_user(id):
    user = db.users.find_one({"username":id})
    if not user:
        return None
    return User.get(id)

def is_authenticated(self):
    return True

def is_active(self):
    return True

def is_anonymous(self):
    return True

def get_id(self):
    return db.users.find_one({'username': self.username})['_id']