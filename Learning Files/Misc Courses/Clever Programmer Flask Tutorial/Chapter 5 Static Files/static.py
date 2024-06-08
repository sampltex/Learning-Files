from flask import Flask, render_template 

app = Flask(__name__)

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
    app.run(debug=True) 