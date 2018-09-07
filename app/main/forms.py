from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):

    # title = StringField('Review title',validators=[Required()])
    comment = TextAreaField('Your Comment')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category = SelectField(u'Pitch Category', choices=[('brainy', 'brainy'), ('poetry', 'poetry'), ('funny', 'funny'),('pickup_lines', 'pickup_lines')])
    content = TextAreaField('Pitch Body')
    submit = SubmitField('Submit')
