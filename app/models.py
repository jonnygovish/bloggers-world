from . import db

from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin
from . import  login_manager

from datetime import datetime 


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))



class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id =db.Column(db.Integer,primary_key =True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True,index = True)
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  password_hash =db.Column(db.String(255))
  blogs = db.relationship('Blog', backref='user', lazy ='dynamic')
  comments = db.relationship('Comment', backref='user', lazy='dynamic')
  

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
   
    self.password_hash = generate_password_hash(password)
    

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

  def __repr__(self):
    return 'User'

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User',backref ='role',lazy ="dynamic")
  

  def __repr__(self):
    return 'User{self.name}'

class Blog(db.Model):
  
  __tablename__ = 'blogs'
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(255))
  content = db.Column(db.String(255))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship('Comment',backref= 'blog', lazy='dynamic')
  date_posted = db.Column(db.DateTime, default= datetime.utcnow)

  def save_blog(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def delete_blog(cls,id):
    delete_blog = Blog.query.filter_by(id=id).delete()
    db.session.commit()
    return delete_blog

  @classmethod
  def get_blog(cls):
    blogs = Blog.query.all()
    return blogs

class Comment(db.Model):
  
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key=True)
  content =db.Column(db.String(255))
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  date_posted = db.Column(db.DateTime, default= datetime.utcnow)

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments = Comment.query.order_by(Comment.id.desc()).filter_by(blog_id =id)
    return comments

  @classmethod
  def delete_comments(cls,id):
    del_comments = Comment.query.filter_by(id=id).delete()
    return del_comments


  
