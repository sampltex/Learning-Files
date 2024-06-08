from flask import Flask, render_template 

app = Flask(__name__)

all_posts = [ # you want to make your databases a list if dictionaries ig
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
    return render_template('posts.html', posts=all_posts) # posts is a variable and you are passing all_posts to it(the database)
# "posts=all_posts" gives posts.html access to the all_posts list of dictionaries

@app.route('/users/<string:name>/post/<int:id>')
def hello(name, id): 
    return f"Hello, {name}, your id is {id}" 

@app.route('/onlyget', methods=['GET']) 
def onlyget():
    return "You can only get on this webpage"

if __name__ == "__main__":
    app.run(debug=True) 