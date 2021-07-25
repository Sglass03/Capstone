from flask import (
  Flask,
  render_template,
  request,
  Response,
  flash,
  redirect,
  url_for,
  jsonify,
  abort)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from auth import (
  AuthError,
  get_token_auth_header,
  verify_decode_jwt,
  check_permissions,
  requires_auth)

from models import setup_db, db, Actor, Movie, database_path


# Run Flask app
def create_app(test_config=None):
    app = Flask(__name__)

    setup_db(app, database_path)

    # app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)

    migrate = Migrate(app, db)

    CORS(app)

    # CREATE ROUTES

    # GET REQUESTS

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actor_list = Actor.query.all()
            actors = []

            for actor in actor_list:
                actors.append(actor.format())
        except:
            abort(500)
        finally:
            db.session.close()

        return jsonify(actors)

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            movie_list = Movie.query.all()
            movies = []

            # Use helper method to format movie records
            for movie in movie_list:
                movies.append(movie.format())
        except:
            abort(500)
        finally:
            db.session.close()

        return jsonify(movies)

    # Add POST requests

    @app.route('/movies', methods=["POST"])
    @requires_auth('add:movie')
    def add_movie(jwt):
        try:
            movie_data = request.get_json()

            new_movie = Movie(
                title=movie_data['title'],
                release_date=movie_data['release_date']
                )

            new_movie.insert()

        except:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

        return "Success", 201

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actor')
    def add_actor(jwt):
        try:
            actor_data = request.get_json()

            new_actor = Actor(
                name=actor_data['name'],
                age=actor_data['age'],
                gender=actor_data['gender'])

            new_actor.insert()

        except:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

        return "Success", 201

    # Add Patch requests

    # Add actor update
    # Casting diretor + Executive producer

    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('update:actor')
    def update_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor_data = request.get_json()

            for field in ['name', 'age', 'gender']:
                if field in actor_data:
                    setattr(actor, field, actor_data[field])

            actor.update()

        except:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

        return "Success", 201

    # PATCH Update movies
    # Casting diretor + Executive producer
    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('update:movie')
    def update_movie(jwt, movie_id):

        try:
            movie = Movie.query.filter_by(id=movie_id).one_or_none()
            movie_data = request.get_json()

            if movie is None:
                abort(404)

            for field in ['title', 'release_date']:
                if field in movie_data:
                    setattr(movie, field, movie_data[field])

            movie.update()

        except:
            db.session.rollback()
            abort(500)
        finally:
            db.session.close()

        return "Success", 201

    # Create DELETE request to delete an actor
    # Executive Producer role

    @app.route('/actors/<actor_id>', methods=["DELETE"])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()

            if actor is None:
                abort(402)

            actor.delete()

        except:
            abort(500)
        finally:
            db.session.close()

        return "Success", 200

    # Create DELETE request to delete an movie
    # Executive Producer role

    @app.route('/movies/<movie_id>', methods=["DELETE"])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):

        try:
            movie = Movie.query.filter_by(id=movie_id).one_or_none()

            if movie is None:
                abort(402)

            movie.delete()

        except:
            abort(500)
        finally:
            db.session.close()

        return "Success", 200

    return app

app = create_app()

# Add error handlers


# 400
@app.errorhandler(400)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Unauthorized - Add Proper Credentials"
    }), 400


# 401
@app.errorhandler(401)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Bad request"
    }), 401


# 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404


# 403
@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Forbidden"
    }), 403


# 500
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500


# 405
@app.errorhandler(405)
def bad_method(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method Not Allowed"
    }), 405
