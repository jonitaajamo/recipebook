from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from application import db
from application.categories.models import Category


class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, max=144)])
    ingredients = TextAreaField("Ingredients", [validators.Length(min=2, max=500)])
    recipetext = TextAreaField("Recipe", [validators.Length(min=2, max=1000)])
    tips = TextAreaField("Extra tips", [validators.Length(max=500)])
    categories = QuerySelectMultipleField(
        'Categories',
        query_factory=lambda: Category.query.all(),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        get_label=lambda item: item.name
    )

    class Meta:
        csrf = False
