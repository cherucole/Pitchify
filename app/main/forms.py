from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Your Comment')
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    review = TextAreaField('Pitch Body')
    submit = SubmitField('Submit')