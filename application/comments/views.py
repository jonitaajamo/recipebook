from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.comments.models import Comment
from application.comments.forms import CommentForm

@app.route("/recipes/<recipe_id>/", methods=["POST"])
@login_required
def comment_create(recipe_id):
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("recipes/<recipe_id>/", form = form)

    c = Comment(form.text.data)
    c.account_id = current_user.id
    c.recipe_id = recipe_id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("recipes/<recipe_id>/"))