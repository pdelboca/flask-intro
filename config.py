import os

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = ',\xadF\x9b\xa2"\x9e\xd6\xb8\x87-&\xd7\xe4\xdb\x17\x8d\x1e`\x8c\xcdt\r\xe8'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	print SQLALCHEMY_DATABASE_URI

class TestConfig(BaseConfig):
	DEBUG = True
	Testing = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False # to be absolutely sure that it will be False on Prod.