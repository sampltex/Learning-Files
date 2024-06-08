from flask import Flask

app = Flask(__name__)

@app.route('/') # you put your domain here for example sample.netlify.com right before the forward slash
@app.route('/higuys') # you can also make other sites work in the url path
def hello(): # this code is what will run when we get to the url
    return "Hello, World!" 

if __name__ == "__main__":
    app.run(debug=True) # actually gives errors instead of a 404 error