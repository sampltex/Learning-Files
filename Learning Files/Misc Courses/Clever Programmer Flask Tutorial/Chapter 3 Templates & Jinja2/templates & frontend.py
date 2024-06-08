from flask import Flask, render_template # new import

app = Flask(__name__)

@app.route('/')
def index(): # your templates folder HAS TO BE "templates" like how the base html file is index.html
    return render_template("index.html") # you can return a string as the html you want

@app.route('/users/<string:name>/post/<int:id>')
def hello(name, id): 
    return f"Hello, {name}, your id is {id}" 

@app.route('/onlyget', methods=['GET']) 
def onlyget():
    return "You can only get on this webpage"

if __name__ == "__main__":
    app.run(debug=True) 