"""Models for Pet."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet available for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                    autoincrement=True, 
                    primary_key=True)

    name = db.Column(db.String(25), 
                        nullable=False)

    species = db.Column(db.Text, 
                            nullable=False)

    photo_url = db.Column(db.Text, 
                            nullable=False, 
                            default='')

    age = db.Column(db.Text, 
                        nullable=False)

    notes = db.Column(db.Text, 
                        nullable=False, 
                        default='')

    available = db.Column(db.Boolean, 
                            nullable=False, 
                            default=True)



