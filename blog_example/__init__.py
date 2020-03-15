from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e1487f9bb26793dcdf3a8350295aa8c1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bc = Bcrypt(app)
log = LoginManager(app)
log.login_view = 'login'
log.login_message_category = 'info'

from blog_example import routes