from flask import Flask

def create_app():
	app = Flask(__name__)

	from basic_web_app.main.routes import main
	app.register_blueprint(main)

	return app