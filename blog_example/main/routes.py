# main
from flask import render_template, request, Blueprint
from blog_example.models import Post

m = Blueprint('main', __name__)

@m.route('/')
@m.route('/home')
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
	return  render_template('home.html', posts=posts)

@m.route('/about')
def about():
	return render_template('about.html', title='About Page')