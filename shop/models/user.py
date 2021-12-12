import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from ._base import ModelMixin


class User(ModelMixin, db.Model):
	__tablename__ = 'users'

	username = sa.Column(sa.String(50), nullable=False, unique=True, index=True)
	email = sa.Column(sa.String(50), nullable=False, unique=True, index=True)
	role = sa.Column(sa.String(10), nullable=False, default='normal')
	password_hash = sa.Column(sa.String(128), nullable=False)

	@property
	def password(self):
		raise ValueError('Read-only attribute')

	@password.setter
	def password(self, pwd):
		self.password_hash = generate_password_hash(pwd)

	def is_verify(self, pwd):
		return check_password_hash(pwd, self.password_hash)