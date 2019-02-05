from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=2, max=144)])
    recipetext = TextAreaField("Recipe", [validators.Length(min=2, max=1000)])
    tips = TextAreaField("Extra tips", [validators.Length(max=500)])

    class Meta:
        csrf = False