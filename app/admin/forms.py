from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
  title =StringField('Blog title', validators = [Required()])
  content= TextAreaField('Content')
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  content = TextAreaField('Comment')
  submit = SubmitField('submit')

class DeleteBlog(FlaskForm):
  submit =SubmitField('Delete Blog')