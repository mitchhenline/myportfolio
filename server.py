"""My portfolio server."""

from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key= "starship"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage"""
    return render_template("home.html")

@app.route('/projects')
def projects():
    """view projects page"""
    return render_template("projects.html")

@app.route('/about_me')
def about_me():
    """view about me page"""
    return render_template("about_me.html")

@app.route('/games')
def games():
    "view games page"
    return render_template("games.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)