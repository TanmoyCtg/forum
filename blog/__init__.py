# this file contain the application factory
# this file tells python that blog folder treated as package

import os

from flask import Flask 

def create_app(test_config=None):
	# create and configure the app

	app = Flask(__name__, instance_relative_config=True) # creates Flask class instance/object
	app.config.from_mapping(SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try: 
		# Flask doesn’t create the instance folder automatically, 
		# but it needs to be created because your project will create the SQLite database file there.
		os.makedirs(app.instance_path)
	except OSError:
		pass

	@app.route('/hello')
	def hello():
		return "Hello, World!"

	from . import db 
	from . import auth

	db.init_app(app)
	app.register_blueprint(auth.bp)
	
	return app 




















