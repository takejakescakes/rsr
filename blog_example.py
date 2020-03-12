from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e1487f9bb26793dcdf3a8350295aa8c1'

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
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}.', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'fake@email.com' and form.password.data == '12':
			flash('You are now logged in.', 'success')
			return redirect(url_for('home'))
		else:
			flash('You don\'t belong here.', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
	app.run(debug=True)