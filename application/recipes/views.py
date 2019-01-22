from application import app, db
from flask import redirect, render_template, request, url_for
from application.recipes.models import Recipe

@app.route("/recipes", methods=["GET"])
def recipes_index():
    return render_template("recipes/list.html", recipes = Recipe.query.all())

@app.route("/recipes/newrecipe/")
def recipe_form():
    return render_template("recipes/newrecipe.html")

@app.route("/recipes/", methods=["POST"])
def recipe_create():
    r = Recipe(request.form.get("name"), request.form.get("recipe_text"), request.form.get("tips"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
def recipe_vote(recipe_id):
    r = Recipe.query.get(recipe_id)
    r.votes += 1
    db.session().commit()

    return redirect(url_for("recipes_index"))
