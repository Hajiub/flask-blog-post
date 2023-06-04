from flask_wtf import FlaskForm
from wtforms import StringField, FileField, EmailField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired, Email


class PostForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=99), DataRequired()])
    email    = EmailField('Email', validators=[Email()])
    content  = TextAreaField('Content', validators=[DataRequired()])
    picture  = FileField('Picture', validators=[DataRequired()])
    submit   = SubmitField('Create')

