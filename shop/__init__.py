from flask import Flask
from flask.wrappers import Response
from .models import db, migrate
from .auth import login_manager
from .config import get_config
from .admin import bp as admin_bp


def create_app(config_name):
	app = Flask(__name__)

	config = get_config(config_name)
	app.config.from_object(config)

	db.init_app(app)
	migrate.init_app(app, db)

	login_manager.init_app(app)

	app.register_blueprint(admin_bp, url_prefix='/admin')

	@app.route('/health')
	def health():
		return Response('', 204)

	return app
