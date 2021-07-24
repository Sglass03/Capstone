from flask_sqlalchemy import SQLAlchemy
import json

  ############################################################
  ################# Create models ############################
  ############################################################

database_path = 'postgres://axkaekoqbfsmbg:7b328ee6d10a372b310f28fe9cff5a5c66a6a90b5dd99e6cfb4a85a9b7a0a402@ec2-54-236-137-173.compute-1.amazonaws.com:5432/delkbr8dkblsk1'

db = SQLAlchemy()

''' Binds flask app and SQLAlchemy service for testing
setup_db(app)
'''

# Set-up DB 
def setup_db(app, database_path=database_path):
  app.config['SQLALCHEMY_DATABASE_URI'] = database_path
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.app = app
  db.init_app(app)
  db.create_all()


# Create association table between movies and actors
movie_actors = db.Table('movie_actors', 
  db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True), 
  db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True))

# Create Movie model
class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String())
  release_date = db.Column(db.Integer)
  actors = db.relationship('Actor', secondary=movie_actors, backref=db.backref('movies', lazy=True))

class Actor(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  age = db.Column(db.Integer)
  gender = db.Column(db.String)