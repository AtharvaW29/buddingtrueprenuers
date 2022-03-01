from flask import Flask
from flask import app
from flask import session
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask("Register")
app.secret_key = "98920"

def login_is_required(function):
    def wrapper(*args, **kwargs):
       if "google_id" not in session:
           return abort(401)
       else:
           return function()
       return wrapper


@app.route("/login")
def login():
    session["google_id"] = "Test"
    return redirect("/mainpage")


@app.route("/index")
def index():
  #the main issue is hoe do i import the homepage.html here!!!

    return


@app.route("/mainpage")
@login_is_required
def mainpage():

    return


if __name__ == "__main__":
    app.run(debug=True)
