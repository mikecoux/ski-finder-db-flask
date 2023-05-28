from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# import json

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

ski_user = db.Table(
    'ski_users',
    db.metadata,
    db.Column('ski_id', db.ForeignKey('skis.id'), primary_key=True),
    db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
    extend_existing=True,
)

class Ski(db.Model):
    __tablename__ = 'skis'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    name = db.Column(db.String)
    dimensions = db.Column(db.String)
    lengths = db.Column(db.String)
    year = db.Column(db.String)
    weight = db.Column(db.Integer)
    image = db.Column(db.String)
    content = db.Column(db.String)
    stoke_profile = db.Column(db.String)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    users = db.relationship('User', secondary=ski_user, back_populates='skis')
    
    def __repr__(self):
        return f"<Ski: {self.brand} {self.name}, Stoke Profile: {self.stoke_profile}>"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    stoke_profile = db.Column(db.String)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    skis = db.relationship('Ski', secondary=ski_user, back_populates='users')
    
    def __repr__(self):
        return f"<User: {self.username}, Stoke Profile: {self.stoke_profile}"
