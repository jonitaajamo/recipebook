from application import db

from sqlalchemy.sql import text

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    recipes = db.relationship("RecipeCategory")

    @staticmethod
    def get_recipe_count_in_categories():
        stmt = text("SELECT category.id, COUNT(recipe_category.category_id) FROM category"
                    " LEFT JOIN recipe_category ON recipe_category.category_id = category.id"
                    " GROUP BY category.id")

        res = db.engine.execute(stmt)
        response = dict()

        for row in res:
            response[row[0]] = row[1]

        return response