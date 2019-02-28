from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.recipes.models import Recipe, Vote, RecipeCategory
from application.comments.models import Comment
from application.recipes.forms import RecipeForm
from application.comments.forms import CommentForm
from application.categories.models import Category

from application.auth.models import User

@app.route("/recipes", methods=["GET"])
def recipes_index():
    recipes = Recipe.query.all()
    votes = Vote.query.all()
    votecount = dict()
    votedOn = []
    comments = Comment.query.all()
    commentcount = dict()

    for vote in votes:
        if not vote.recipe_id in votecount:
            votecount[vote.recipe_id] = 1
        else:
            votecount[vote.recipe_id] += 1

    for comment in comments:
        if not comment.recipe_id in commentcount:
            commentcount[comment.recipe_id] = 1
        else:
            commentcount[comment.recipe_id] += 1

    if current_user.is_authenticated:
        votedOnQuery = Vote.query.filter(Vote.account_id == current_user.id).all()
        for vote in votedOnQuery:
            votedOn.append(vote.recipe_id)

    users = User.query.all()
    return render_template("recipes/list.html", recipes = recipes, users = users, votes=votecount, votedOn=votedOn, commentcount=commentcount)

@app.route("/recipes/category/<category_id>", methods=["GET"])
def recipes_by_categories(category_id):
    recipes = Recipe.get_recipes_by_category(category_id)
    votes = Vote.query.all()
    votecount = dict()
    votedOn = []
    comments = Comment.query.all()
    commentcount = dict()
    print("resepti " + str(recipes[0]))

    for vote in votes:
        if not vote.recipe_id in votecount:
            votecount[vote.recipe_id] = 1
        else:
            votecount[vote.recipe_id] += 1

    for comment in comments:
        if not comment.recipe_id in commentcount:
            commentcount[comment.recipe_id] = 1
        else:
            commentcount[comment.recipe_id] += 1

    if current_user.is_authenticated:
        votedOnQuery = Vote.query.filter(Vote.account_id == current_user.id).all()
        for vote in votedOnQuery:
            votedOn.append(vote.recipe_id)

    users = User.query.all()
    return render_template("recipes/list.html", recipes = recipes, users = users, votes=votecount, votedOn=votedOn, commentcount=commentcount)

@app.route("/recipes/newrecipe/")
@login_required(role="ANY")
def recipe_form():
    return render_template("recipes/newrecipe.html", form = RecipeForm())

@app.route("/recipes/", methods=["POST"])
@login_required(role="ANY")
def recipe_create():
    form = RecipeForm(request.form)
    if not form.validate():
        return render_template("recipes/newrecipe.html", form = form)

    r = Recipe(form.name.data, form.ingredients.data, form.recipetext.data, form.tips.data)


    r.account_id = current_user.id

    db.session().add(r)
    db.session.commit()

    for category in form.categories.data:
        rc = RecipeCategory(r.id, category.id)
        db.session.add(rc)
    
    db.session.commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/update/<recipe_id>/", methods=["GET", "POST"])
@login_required(role="ANY")
def recipe_update(recipe_id):
    rToUpdate = Recipe.query.get(recipe_id)

    if rToUpdate.account_id != current_user.id:
        return login_manager.unauthorized()

    form = RecipeForm(request.form)
    form.name.data = rToUpdate.name
    form.ingredients.data = rToUpdate.ingredients
    form.recipetext.data = rToUpdate.recipe_text
    form.tips.data = rToUpdate.tips

    if request.method == "GET":
        return render_template("recipes/editrecipe.html", form=form, recipe=rToUpdate)
    
    if not form.validate():
        return render_template("recipes/editrecipe.html", form = form)


    form = RecipeForm(request.form)
    rToUpdate.name = form.name.data
    rToUpdate.ingredients = form.ingredients.data
    rToUpdate.recipe_text = form.recipetext.data
    rToUpdate.tips = form.tips.data

    db.session().add(rToUpdate)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required(role="ANY")
def recipe_vote(recipe_id):
    v = Vote.query.filter(Vote.account_id == current_user.id).filter(Vote.recipe_id == recipe_id).all()
    if v:
        return render_template('error.html'), 403
    
    newv = Vote(current_user.id, recipe_id)
    db.session().add(newv)
    db.session().commit()

    return redirect(request.referrer)

@app.route("/delete/<recipe_id>/", methods=["GET"])
@login_required(role="ANY")
def recipe_delete(recipe_id):
    recipeToDelete = Recipe.query.get(recipe_id)
    if recipeToDelete.account_id != current_user.id:
        return login_manager.unauthorized()
    deletevotes = Vote.__table__.delete().where(Vote.recipe_id == recipe_id)
    deletecomments = Comment.__table__.delete().where(Comment.recipe_id == recipe_id)
    deletecategories = RecipeCategory.__table__.delete().where(RecipeCategory.recipe_id == recipe_id)
    db.session.execute(deletevotes)
    db.session.execute(deletecomments)
    db.session.execute(deletecategories)
    db.session.delete(recipeToDelete)
    db.session().commit()

    return redirect(url_for("recipes_index"))

@app.route("/recipes/<recipe_id>/", methods=["GET"])
def recipe_get(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    comments = Comment.query.filter_by(recipe_id = recipe_id).all()
    username = User.query.get(recipe.account_id).username
    users = User.query.all()
    voted = False
    votes = Vote.query.filter_by(recipe_id = recipe_id).count()
    recipeCategories = RecipeCategory.query.filter_by(recipe_id = recipe_id).all()
    categories = []

    for recipeCategory in recipeCategories:
        category = Category.query.filter_by(id = recipeCategory.category_id).all()
        for item in category:
            categories.append(item.name)

    if current_user.is_authenticated:
        votedOnQuery = Vote.query.filter(Vote.account_id == current_user.id).all()
        for vote in votedOnQuery:
            if vote.recipe_id == recipe.id:
                voted = True

    form = CommentForm(request.form)
    return render_template("recipes/recipe.html", recipe=recipe, username=username, comments=comments, form=form, users=users, voted=voted, votes=votes, categories=categories)

@app.route("/comment/<recipe_id>/", methods=["POST"])
@login_required(role="ANY")
def comment_create(recipe_id):
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("recipes/<recipe_id>/", form = form)

    c = Comment(form.text.data)
    c.account_id = current_user.id
    c.recipe_id = recipe_id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for('recipe_get', recipe_id=recipe_id))

@app.route("/delete/comment/<comment_id>/", methods=["GET"])
@login_required(role="ANY")
def comment_delete(comment_id):
    commentToDelete = Comment.query.get(comment_id)
    if commentToDelete.account_id != current_user.id:
        return login_manager.unauthorized()
    db.session.delete(commentToDelete)
    db.session().commit()

    return redirect(url_for('recipe_get', recipe_id=commentToDelete.recipe_id))