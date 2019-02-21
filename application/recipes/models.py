from application import db
from application.models import Base
from application.categories.models import Category
from application.comments.models import Comment

class RecipeCategory(db.Model):
    __table_args__ = (db.PrimaryKeyConstraint('recipe_id', 'category_id'),)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Vote(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __init__(self, account_id, recipe_id):
        self.account_id = account_id
        self.recipe_id = recipe_id

class Recipe(Base):
    name = db.Column(db.String(144), nullable=False)
    recipe_text = db.Column(db.String(1000), nullable=False)
    tips = db.Column(db.String(500), nullable=True)
    public = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    categories = db.relationship("RecipeCategory", backref='category', lazy=True)
    comments = db.relationship("Comment", backref='comment', lazy=True)
    votes = db.relationship("Vote", backref='vote', lazy=True)

    def __init__(self, name, recipe_text, tips):
        self.name = name
        self.recipe_text = recipe_text
        self.tips = tips
        self.votes = 0
        self.public = True
