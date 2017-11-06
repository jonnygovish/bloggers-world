import os

class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# simple mde  configurations
	SIMPLEMDE_JS_IIFE = True
	SIMPLEMDE_USE_CDN = True	

  

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  


class DevConfig(Config):
	DEBUG =True
	SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://puppah:zanpakutou@localhost/blogworld'

config_options={
	'development':DevConfig,
	'production':ProdConfig,
}

