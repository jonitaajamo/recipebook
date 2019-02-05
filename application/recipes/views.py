from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe
from application.recipes.forms import RecipeForm

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/newrecipe/")
def recipe_form():
    return render_template("recipes/newrecipe.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
def recipe_create():
    form = RecipeForm(request.form)
    if not form.validate():
        return render_template("recipes/newrecipe.html", form = form)

    r = Recipe(form.name.data, form.recipetext.data, form.tips.data)

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipe_vote(recipe_id):
    r = Recipe.query.get(recipe_id)
    r.votes += 1
    db.session().commit()

    return redirect(url_for("recipes_index"))
