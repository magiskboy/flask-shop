import os


class BaseConfig:
	ROOT_DIR = os.getcwd()

	DEBUG = True

	TESTING = False

	SECRET_KEY = 'this is a secret key'

	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

	SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'


class TestingConfig(BaseConfig):
	DEBUG = False

	TESTING = True


class ProductionConfig(BaseConfig):
	DEBUG = False

	TESTING = False

	SECRET_KEY = os.urandom(32)


def get_config(config_name):
	return {
		'development': DevelopmentConfig,
		'testing': TestingConfig,
		'production': ProductionConfig
	}.get(config_name, 'production')