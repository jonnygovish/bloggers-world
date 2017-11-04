from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
  title =StringField('Blog title', validators = [Required()])
  content= TextAreaField('Content')
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about yourself', validators = [Required()])
  submit = SubmitField('submit')