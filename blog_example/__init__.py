import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e1487f9bb26793dcdf3a8350295aa8c1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bc = Bcrypt(app)
log = LoginManager(app)
log.login_view = 'login'
log.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'takejakescake'
app.config['MAIL_PASSWORD'] = 'zffhpcpaxoadfzyy'
mail = Mail(app)

from blog_example import routes