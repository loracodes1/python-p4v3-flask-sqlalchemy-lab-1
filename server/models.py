from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    __tablename__ ="earthquakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    magnitude =db.Column(db.Float)
    location =db.Column(db.String)
    year= db.column(db.Integer)