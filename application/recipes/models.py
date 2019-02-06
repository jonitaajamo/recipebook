from application import db

# TODO: all tables

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False)
    recipe_text = db.Column(db.String(1000), nullable=False)
    tips = db.Column(db.String(500), nullable=True)
    public = db.Column(db.Boolean, nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, recipe_text, tips):
        self.name = name
        self.recipe_text = recipe_text
        self.tips = tips
        self.votes = 0
        self.public = True