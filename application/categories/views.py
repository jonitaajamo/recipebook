from application import app, db
from flask import redirect, render_template, request, url_for

from application.categories.models import Category

@app.route("/categories", methods=["GET"])
def categories_index():
    categories = Category.query.all()
    category_count = Category.get_recipe_count_in_categories()

    return render_template("categories/categories.html", categories=categories, category_count=category_count)