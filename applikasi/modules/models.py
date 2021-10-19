from flask_sqlalchemy import SQLAlchemy
from applikasi import app

db = SQLAlchemy(app)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nim = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    jurusan = db.Column(db.String,nullable=False)

    def __repr__(self):
        return "<Name: {}>".format(self.name)
