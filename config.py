import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'my precious'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False # to be absolutely sure that it will be False on Prod.