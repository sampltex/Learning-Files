from flask import Flask

app = Flask(__name__)

@app.route('/') # you can receive a variable in the url by using 
@app.route('/users/<string:name>/<int:id>') # <{type}:{var name}> like this <string:name>
def hello(name, id): 
    return f"Hello, {name}, your id is {id}" 

@app.route('/onlyget', methods=['GET']) # if you wanted to post you can add 'POST' to the list in methods=[]
def onlyget():
    return "You can only get on this webpage"
# when visiting a webpage you have to GET/receive whats on there, if you can only post it wont work
if __name__ == "__main__":
    app.run(debug=True)