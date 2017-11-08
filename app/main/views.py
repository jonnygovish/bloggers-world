from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Role
from .forms import BlogForm,CommentForm,DeleteBlog
from .. import db
import markdown2


@main.route('/')
def index():

  blogs = Blog.get_blog()
  title ="Blogs World"
  return render_template('index.html', title=title,blogs=blogs)

# @main.route('/admin/dashboard')
# @login_required
# def admin_dashboard():
#   #prevents non-admin from accessing the page
#   if not current_user.is_admin:
#     abort(403)
#   else:
#     blogs = Blog.get_blog()

#   title = 'Dashboard'
#   return render_template('admin/admin_dashboard.html',title = title,blogs =blogs)

@main.route('/blog/<int:id>')
def blog(id):
  blogs = Blog.query.get(id)
  comments = Comment.get_comments(id)
  form = CommentForm()
  title ="Blogs"

  return render_template('blog.html', title =title, blogs=blogs,comments=comments,comment_form= form)



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

@main.route('/blog/comment/<int:id>')
def single_comment(id):
  
  comment = Comment.query.get(id)

  if comment is None:
    abort(404)

  format_comment = markdown2.markdown(comment.content,extras=["code-friendly", "fenced-code-blocks"])
  return render_template('comment.html', comment= comment, format_comment= format_comment)

@main.route('/blog/comment/delete/<int:id>')
def delete_comment(id):
  
  comment = Comment.query.get(id)
  comment.delete_comments(id)

  return redirect(url_for('.index'))

@main.route('/blog/delete/<int:id>')
def delete_blog(id):
  
  blog = Blog.query.get(id)
  blog.delete_blog(id)

  return redirect(url_for('.index'))

  

