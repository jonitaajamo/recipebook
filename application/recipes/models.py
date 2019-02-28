from application import db
from application.models import Base
from application.categories.models import Category
from application.comments.models import Comment

from sqlalchemy.sql import text

class RecipeCategory(db.Model):
    __table_args__ = (db.PrimaryKeyConstraint('recipe_id', 'category_id'),)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __init__(self, recipe_id, category_id):
        self.recipe_id = recipe_id
        self.category_id = category_id

class Vote(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __init__(self, account_id, recipe_id):
        self.account_id = account_id
        self.recipe_id = recipe_id

class Recipe(Base):
    name = db.Column(db.String(144), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    recipe_text = db.Column(db.String(1000), nullable=False)
    tips = db.Column(db.String(500), nullable=True)
    public = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    categories = db.relationship("RecipeCategory", backref='category', lazy=True)
    comments = db.relationship("Comment", backref='comment', lazy=True)
    votes = db.relationship("Vote", backref='vote', lazy=True)

    def __init__(self, name, ingredients, recipe_text, tips):
        self.name = name
        self.recipe_text = recipe_text
        self.ingredients = ingredients
        self.tips = tips
        self.public = True

    @staticmethod
    def get_recipes_by_category(category_id):
        stmt = text("SELECT recipe.id, recipe.name, recipe.account_id FROM recipe"
                    " LEFT JOIN recipe_category ON recipe_category.recipe_id = recipe.id"
                    " LEFT JOIN category ON category.id = recipe_category.category_id"
                    " WHERE category.id = :categoryid ")

        response = db.engine.execute(stmt, categoryid = category_id)
        res = []

        for row in response:
            res.append(row)

        return res
