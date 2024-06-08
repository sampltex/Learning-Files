from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # new import this is what is used for databases in flask
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' # this is just the path to where the database is storred
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # connects db to our app

# this class is a "model" for the database
class BlogPost(db.Model): # each column is a class variabe and a row would be a blog post
    id = db.Column(db.Integer, primary_key=True) # primary_key=True means that it is going to be the main distinguisher of each blog post
    title = db.Column(db.String(100), nullable=False) # basically the title is required and has a max number of characters of 100
    content = db.Column(db.Text, nullable=False) # text goes on as long as it wants basically no limit to length
    author = db.Column(db.String(20), nullable=False, default="N/A") # author is required but if its not there just fill it in as N/A
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # its literally just the date and time, i needed to import datetime to use it

    def __repr__(self): # prints when a new blog post is created, basically displays to the screen 
        return f"Blog Post {self.id}"

all_posts = [ 
    {
        "title": "Post 1",
        "content": "This is the content of post1.",
        "author": "Aaron"
    },
    {
        "title": "Post 2",
        "content": "This is the content of post2."
    }
]

@app.route('/')
def index(): 
    return render_template("index.html") 

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts) 

@app.route('/users/<string:name>/post/<int:id>')
def hello(name, id): 
    return f"Hello, {name}, your id is {id}" 

@app.route('/onlyget', methods=['GET']) 
def onlyget():
    return "You can only get on this webpage"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 