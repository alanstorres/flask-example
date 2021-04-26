from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
	return '<h1>Sup! Now we have more text.</h1>'