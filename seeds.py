"""Seed file to make sample data for adopt db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="Dog", age="baby")
bowser = Pet(name='Bowser', species="Pug", age="young")
spike = Pet(name='Spike', species="Porcupine", age="adult")

# Add pets to session
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit
db.session.commit()