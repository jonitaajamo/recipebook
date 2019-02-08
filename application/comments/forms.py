from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CommentForm(FlaskForm):
    text = TextAreaField("Recipe", [validators.Length(min=2, max=500)])

    class Meta:
        csrf = False