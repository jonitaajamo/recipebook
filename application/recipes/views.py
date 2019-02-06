from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

from application.auth.models import User

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all(), users = User.query.all())

@app.route("/recipes/newrecipe/")
@login_required
def recipe_form():
    return render_template("recipes/newrecipe.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipe_create():
    form = RecipeForm(request.form)
    if not form.validate() or form.confirm_password != form.password:
        return render_template("recipes/newrecipe.html", form = form)

    r = Recipe(form.name.data, form.recipetext.data, form.tips.data)
    r.account_id = current_user.id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def recipe_vote(recipe_id):
    r = Recipe.query.get(recipe_id)
    r.votes += 1
    db.session().commit()

    return redirect(url_for("recipes_index"))
