import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://polafri_user:mypassword@localhost/Pol_Afri'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")