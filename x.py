from flask import Flask, render_template

x = Flask(__name__)

@x.route('/')

def home():
	#return 'Coronavirus Fan Club'
	return render_template('html/home.html')

if __name__ == '__main__':
	x.run(debug=True)