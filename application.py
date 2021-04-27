from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
	return '<h1>Oi Marina, tudo bem? Sdds</h1>'