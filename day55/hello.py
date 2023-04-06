from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  res = '<h1 style="text-align:center">Hello, World! This is our first Flask app.</h1>'\
  '<p> This is a paraghraph</p>'\
    '<img src="https://64.media.tumblr.com/9a2378cb66a9985d2ca5d44ce5ee9c88/891af64ebd849525-eb/s500x750/5d3fecaae87b8f5fd0adea085d206f80a2d1ab3a.gif" width=200>'
  return res

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
  res = "bye ..."
  return res

@app.route("/<name>/<int:number>")
def greet(name, number):
  return f"hello, {name}, you are {number} years old!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)