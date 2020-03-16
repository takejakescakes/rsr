from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask_mail import Mail
# from blog_example.config import Config


_D = SQLAlchemy()
_E = Bcrypt()
_L = LoginManager()
#log.login_view = 'users.login'
#log.login_message_category = 'info'
#mail = Mail()


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bc.init_app(app)
	log.init_app(app)
	mail.init_app(app)

	from blog_example.users.routes import u
	from blog_example.posts.routes import p
	from blog_example.main.routes import m
	from blog_example.errors.handlers import errors
	app.register_blueprint(u)
	app.register_blueprint(p)
	app.register_blueprint(m)
	app.register_blueprint(errors)

	return app