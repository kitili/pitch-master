import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mourine:shena2308~@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='mbula'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
  
    MAIL_USERNAME = 'mourinekitilimourine@gmail.com'
    MAIL_PASSWORD = 'shena2308~'
   


    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mourine:shena2308~@localhost/pitches_test'    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mourine:shena2308~@localhost/pitches'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}