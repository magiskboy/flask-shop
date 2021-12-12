import sqlalchemy as sa
from . import db


class ModelMixin:
	id = sa.Column(sa.Integer(), primary_key=True, index=True, autoincrement=True)
	created_at = sa.Column(sa.TIMESTAMP, default=sa.sql.func.now())
	updated_at = sa.Column(sa.TIMESTAMP, onupdate=sa.sql.func.now())

	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.remove(self)
		db.session.commit()