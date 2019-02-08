from application import db
from application.models import Base


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
