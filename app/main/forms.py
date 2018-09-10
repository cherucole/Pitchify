from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = TextAreaField('Your comment...',validators = [Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category = SelectField(u'Pitch Category', choices=[('brainy', 'brainy'), ('poetry', 'poetry'), ('funny', 'funny'),('pickup_lines', 'pickup_lines')])
    content = TextAreaField('Pitch Body')
    submit = SubmitField('Submit')

