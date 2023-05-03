from flask import Flask
from flask_login import LoginManager
from .api import api
from .auth import auth
from .models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hd_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(api)
auth.login_manager = login_manager
app.register_blueprint(auth)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
