from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.recipes.models import Recipe
from application.comments.models import Comment
from application.recipes.forms import RecipeForm
from application.comments.forms import CommentForm

from application.auth.models import User

@app.route("/recipes", methods=["GET"])
def recipes_index():
    recipes = Recipe.query.all()
    return render_template("recipes/list.html", recipes = recipes, users = User.query.all())

@app.route("/recipes/newrecipe/")
@login_required
def recipe_form():
    return render_template("recipes/newrecipe.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required
def recipe_create():
    form = RecipeForm(request.form)
    if not form.validate():
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

@app.route("/delete/<recipe_id>/", methods=["GET"])
def recipe_delete(recipe_id):
    recipeToDelete = Recipe.query.get(recipe_id)
    db.session.delete(recipeToDelete)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipe_get(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    comments = Comment.query.filter_by(recipe_id = recipe_id).all()
    username = User.query.get(recipe.account_id).username
    users = User.query.all()
    form = CommentForm(request.form)
    return render_template("recipes/recipe.html", recipe=recipe, username=username, comments=comments, form=form, users=users)

@app.route("/comment/<recipe_id>/", methods=["POST"])
@login_required
def comment_create(recipe_id):
    form = CommentForm(request.form)
    print("saatiin kommentti " + form.text.data)
    if not form.validate():
        return render_template("recipes/<recipe_id>/", form = form)

    c = Comment(form.text.data)
    c.account_id = current_user.id
    c.recipe_id = recipe_id

    db.session().add(c)
    db.session().commit()

    return recipe_get(recipe_id)