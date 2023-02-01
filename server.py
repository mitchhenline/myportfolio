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

skills = "kjghvkuvkubv"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)