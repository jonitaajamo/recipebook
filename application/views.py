from flask import render_template
from application import app
from flask_login import current_user

from application.auth.models import User

@app.route("/")
def index():
    if current_user.is_authenticated:
        commentcount_on_own_recipes = User.get_commentcount_on_own_recipes()
        user_commentcount = User.get_user_commentcount()
    else:
        commentcount_on_own_recipes = 0
        user_commentcount = 0

    return render_template("index.html", commentcount_on_own_recipes=commentcount_on_own_recipes, user_commentcount=user_commentcount)