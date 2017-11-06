from flask import render_template, request, redirect, url_for, abort
from . import admin
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Role
from .forms import BlogForm,CommentForm,DeleteBlog
from .. import db
import markdown2

def check_admin():
  """
  Prevents non-admins from accessing the page
  """
  if not current_user.is_admin:
    abort(403)

@admin.route('/admin_dashboard')
def admin_dashboard():
  check_admin()
  
  blogs = Blog.get_blog()
  print(blogs)
  title ="Blogs World"
  return render_template('admin/admin_dashboard.html', title=title,blogs=blogs)


@admin.route('/admin/blog/<int:id>')
def blog(id):
  
  check_admin()

  blogs = Blog.query.get(id)
  comments = Comment.get_comments(id)
  form = CommentForm()
  title ="Blogs"

  return render_template('admin/blog_post.html', title =title, blogs=blogs,comments=comments,comment_form= form)

@admin.route('/blog/new', methods = ["GET", "POST"])
def new_blog():
  
  check_admin()

  form = BlogForm()

  if form.validate_on_submit():
    title = form.title.data
    content = form.content.data

    new_blog = Blog(title =title, content=content, user_id = current_user.id)

    new_blog.save_blog()

    return redirect(url_for('.admin_dashboard'))

  title = "New Blog"

  return render_template('admin/new_blog.html',title = title, blog_form = form) 

# @admin.route('/comment/<int:id>')
# def single_comment(id):
  
#   check_admin()
#   comment = Comment.query.get(id)

#   if comment is None:
#     abort(404)

#   format_comment = markdown2.markdown(comment.content,extras=["code-friendly", "fenced-code-blocks"])
#   return render_template('comment.html', comment= comment, format_comment= format_comment) 