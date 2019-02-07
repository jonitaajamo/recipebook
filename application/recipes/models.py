from application import db
from application.models import Base

junction_table = db.Table('RecipeCategory', Base.metadata, 
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')), 
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

class Recipe(Base):
    
    name = db.Column(db.String(144), nullable=False)
    recipe_text = db.Column(db.String(1000), nullable=False)
    tips = db.Column(db.String(500), nullable=True)
    public = db.Column(db.Boolean, nullable=False)
    votes = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    category = db.relationship("Category", secondary=junction_table)

    def __init__(self, name, recipe_text, tips):
        self.name = name
        self.recipe_text = recipe_text
        self.tips = tips
        self.votes = 0
        self.public = True

class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    recipe = db.relationship("Recipe", secondary=junction_table)
