from flask import Flask
from models import *
from main import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:qwerty@localhost:5433/twainlab"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()


