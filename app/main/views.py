from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Role
from .forms import BlogForm,CommentForm
from .. import db
import markdown2


@main.route('/')
def index():

  blogs = Blog.get_blog()
  title ="Blogs World"
  return render_template('index.html', title=title,blogs=blogs)

@main.route('/blog/<int:id>')
def blog(id):
  blogs = Blog.query.get(id)
  comments = Comment.get_comments(id)
  del_blog = Blog.delete_blog()
  title ="Blogs"

  return render_template('blog.html', title =title, blogs=blogs,comments=comments, comment_form = form, del_blog =del_blog)
@main.route('/blog/new', methods = ["GET", "POST"])
def new_blog():
  form = BlogForm()

  if form.validate_on_submit():
    title = form.title.data
    content = form.content.data

    new_blog = Blog(title =title, content=content, user_id = current_user.id)

    new_blog.save_blog()

    return redirect(url_for('.index'))

  title = "New Blog"

  return render_template('new_blog.html',title = title, blog_form = form)

@main.route('/blog/<int:id>',methods=["GET","POST"])
def new_comment(id):
  blog = Blog.query.filter_by(id=id).first()

  form = CommentForm()

  if form.validate_on_submit():
    content = form.content.data

    new_comment = Comment(content = content, blog_id = blog.id)
    new_comment.save_comment()

    return redirect(url_for('.blog', id = blog.id))

  return render_template('blog.html', comment_form =form)

@main.route('/comment/<int:id>')
def single_comment(id):
  comment = Comment.query.get(id)

  if comment is None:
    abort(404)

  format_comment = markdown2.markdown(comment.content,extras=["code-friendly", "fenced-code-blocks"])
  return render_template('comment.html', comment= comment, format_comment= format_comment)