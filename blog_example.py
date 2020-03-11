from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == "__main__":
	app.run(debug=True)