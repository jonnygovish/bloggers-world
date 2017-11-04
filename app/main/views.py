from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Role
from .forms import BlogForm 
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
  title ="Blogs"

  return render_template('blog.html', title =title, blogs=blogs,comments=comments)
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