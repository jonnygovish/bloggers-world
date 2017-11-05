import os

class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://puppah:zanpakutou@localhost/blogworld'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# simple mde  configurations
	SIMPLEMDE_JS_IIFE = True
	SIMPLEMDE_USE_CDN = True	

  

class ProdConfig(Config):
  	pass
  


class DevConfig(Config):
	DEBUG =True

config_options={
	'development':DevConfig,
	'production':ProdConfig,
}

