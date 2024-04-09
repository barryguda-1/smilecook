class Config:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smilecookadm:mysecretpassword@localhost/smilecook'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = '<KEY>'

    JWT_ERROR_MESSAGE_KEY = '<MESSAGE>'

