from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Your Comment')
    submit = SubmitField('Submit')
