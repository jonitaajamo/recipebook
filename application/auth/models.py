from application import db
from application.models import Base
from flask_login import current_user

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    email = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    recipes = db.relationship("Recipe", backref='account', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def is_authenticated(self):
        return True

    @staticmethod
    def get_user_commentcount():
        stmt = text("SELECT COUNT(*) FROM comment"
                    " WHERE account_id = :account")

        response = db.engine.execute(stmt, account = current_user.id)
        res = 0

        for row in response:
            res += row[0]

        return res

    @staticmethod
    def get_commentcount_on_own_recipes():
        stmt = text("SELECT COUNT(*) FROM account"
                    " LEFT JOIN recipe ON recipe.account_id = account.id"
                    " LEFT JOIN comment ON comment.recipe_id = recipe.id"
                    " WHERE account.id = :account")

        response = db.engine.execute(stmt, account = current_user.id)
        res = 0

        for row in response:
            res += row[0]

        return res
    

