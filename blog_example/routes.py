import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from blog_example import app, db, bc
from blog_example.forms import RegistrationForm, LoginForm, UpdateAccountForm
from blog_example.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

post = [
	{
		'author': 'Butt Head',
		'title': 'We all dead',
		'content': 'Things are getting bad!',
		'date': 'April 20, 1969'
	},
	{
		'author': 'Fart Face',
		'title': 'who is asking',
		'content': 'I don\'t trust this guy at all!',
		'date': 'June 9, 1985'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return  render_template('home.html', post=post)

@app.route('/about')
def about():
	return render_template('about.html', title='About Page')

@app. route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		flash(f'You\'re already logged in!', 'danger')
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hsh = bc.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hsh)
		db.session.add(user)
		db.session.commit()
		flash(f'New account created.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		flash(f'You\'re already logged in!', 'danger')
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		u = User.query.filter_by(email=form.email.data).first()
		print(u)
		if u and bc.check_password_hash(u.password, form.password.data):
			login_user(u, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('You don\'t belong here.', 'danger')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	print(current_user.image_file)
	if form.validate_on_submit():
		f = form.picture.data
		if f:
			picture_file = save_picture(f)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Changes saved.', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
		form.picture.data = current_user.image_file
	image_file = url_for('static', filename='img/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)