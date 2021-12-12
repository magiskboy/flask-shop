from flask import session
from flask_login import UserMixin, LoginManager
from .models import User


class CurrentUser(User, UserMixin):
	pass


login_manager = LoginManager()


@login_manager.request_loader
def request_loader(request):
	username = session.get('username')
	if username:
		user = CurrentUser.query.filter_by(username=username).first()
		return user
	return None


@login_manager.unauthorized_handler
def unauthorized_handler():
	return 'unauthorized_handler'