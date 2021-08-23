from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Type User Bio:',validators = [Required()])
    submit = SubmitField('Save Bio')

class PitchForm(FlaskForm):
    title = StringField('Title Of Pitch:', validators=[Required()])
    category = SelectField('Category of Pitch:', choices=[('work','work  '),('educational','educational'),('entertainment','entertainment')],validators=[Required()])
    post = TextAreaField('Enter Your Pitch:', validators=[Required()])
    submit = SubmitField('Submit Pitch:')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment On Pitch:',validators=[Required()])
    submit = SubmitField('Comment:')