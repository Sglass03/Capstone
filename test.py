from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from auth import AuthError, get_token_auth_header, verify_decode_jwt, check_permissions, requires_auth 
from flask_cors import CORS
from app import create_app, setup_db

import unittest
import json
import os

from app import Actor, Movie, create_app, setup_db

class AppNameTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://postgres:root@localhost:5432/capstone_test"
        setup_db(self.app, self.database_path)

        # Roles
        self.exec_producer = os.environ['EXEC_PRODUCER']
        self.casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlkZmp1RjdEXzQtVFI0cGJxMkVIYyJ9.eyJpc3MiOiJodHRwczovL2ZzY291cnNlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDMyNmQyMWFmNTA0NjAwNjk2Mjk4NTQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyNzE0NTYzOCwiZXhwIjoxNjI3MjMyMDM4LCJhenAiOiJ3aU11Y1JuallZS0dsQUZ1UXE4enhKSkQycjhST1VKcCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Oy1gQNE81I8NS52GwdUgSvRfE5UExeMlJc0GqvIFLJct-q2VR4G6VN4eqZHxIjD7zyP-3wGNXqvTnR0FUty-3FT1NNftrqwURm6z39_FkZITNJ7s_u1-oeqv-wjoiiZUqjNIzN4GL8WuSFl2gfEpbhpci5-dR-uoNlOQZL386_CfJ0hohl7LLErHHyLXNVnGqzxrqs22wCDGeQqX9W-SWPQRLiM7fQVYNhiENv-CA_wY5kJkpxGKjApPVw7XtwnEEYU0Hz-burKidWcBzdlZZCc5L_IcvJ2_UuqVMsohpFU7647S4nxnu4CjlfyhpXFKvjDE7krIC3An5CFwrrU63A'
        self.casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlkZmp1RjdEXzQtVFI0cGJxMkVIYyJ9.eyJpc3MiOiJodHRwczovL2ZzY291cnNlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDMyNmQyMWFmNTA0NjAwNjk2Mjk4NTQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyNzE0NTU1NiwiZXhwIjoxNjI3MjMxOTU2LCJhenAiOiJ3aU11Y1JuallZS0dsQUZ1UXE4enhKSkQycjhST1VKcCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.illDJ_g2rwyl32dd1MH0pkFobqtcBYhe24PLI_ZASpWRlVdyQyMIQJHpJIVD0kwYJatmfrHscBKcviClpNy8gZ6qEvSHmazP7iNz0bCRTJc55qdVvYYueW4Sr57VmJ1vsSPj_cXe8CqlqH1BeirJsi4YzGmr5giEUVokojR6p4KGstX4p0QVtBIRQx6akkTrYW4XOJr5srvWnFWkqD4bwlLreqy_ThUSy4Wo7_4EAU-gxTJE2EmtBIPTUDf_0fREVAKRyTrTO8pM4UjessAml9VSh2dk8O8ukjHQduxovT_tZhiMcB-YAgru0e6ALdJt1dQsCdvQQmT4GZDK1WqpbQ'

        # Json for adding to test db
        self.new_movie = {
          'id': 1,
          'title': 'Test Movie', 
          'release_date': 2020
        }

        self.update_movie = {
          'title': 'Updated Movie'
        }

        self.new_actor = {
          'id': 1,
          'name': 'New Actor', 
          'age': 100, 
          'gender': 'Female'
        }

        self.update_actor = {
          'name': 'Updated Actor'
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    # add movie #

    def test_add_movie(self):
      """Test post request to add movie """
      res = self.client().post('/add_movie',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)}, 
        json=self.new_movie
        )

      self.assertEqual(res.status_code, 201)

    def test_add_movie_unauthorized(self):
      """Test post request to add movie as casting assistant """
      res = self.client().post('/add_movie',
        headers={
          "Authorization": "Bearer {}".format(self.casting_assistant)}, 
        json=self.new_movie
        )

      self.assertEqual(res.status_code, 403)

    # add actor
    def test_add_actor(self):
      """Test post request to add actor as casting director"""
      res = self.client().post('/add_actor',
        headers={
          "Authorization": "Bearer {}".format(self.casting_director)}, 
        json=self.new_actor
        )

      self.assertEqual(res.status_code, 201)

    def test_add_actor_unauthorized(self):
      """Test post request to add actor as casting assistant """
      res = self.client().post('/add_actor',
        headers={
          "Authorization": "Bearer {}".format(self.casting_assistant)}, 
        json=self.new_actor
        )

      self.assertEqual(res.status_code, 403)

    # get actors
    def test_get_actors_success(self):
      """Test get request for actors with exec producer """
      res = self.client().get('/actors',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        })

      self.assertEqual(res.status_code, 200)

    def test_get_actors_unauthorized(self):
      """Test get request for actors with bad token """
      res = self.client().get('/actors',
        headers={
          "Authorization": "Bearer {}".format('bs_token')
        })

      self.assertEqual(res.status_code, 401)
    
    # get movies
    def test_get_movies_success(self):
      """Test get request for actors with exec producer """
      res = self.client().get('/movies',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        })

      self.assertEqual(res.status_code, 200)

    def test_get_movies_unauthorized(self):
      """Test get request for movies with bad token """
      res = self.client().get('/movies',
        headers={
          "Authorization": "Bearer {}".format('bs_token')
        })

      self.assertEqual(res.status_code, 401)

    # update movie
    def test_update_movie_success(self):
      """Test PATCH request to update movie as exec producer """
      res = self.client().patch('/update_movie/1',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        }, 
        json=self.update_movie)

      self.assertEqual(res.status_code, 201)

    def test_update_movie_fail(self):
      """Test PATCH request to update movie as casting assistant """
      res = self.client().patch('/update_movie/1',
        headers={
          "Authorization": "Bearer {}".format(self.casting_assistant)
        }, 
        json=self.update_movie)

      self.assertEqual(res.status_code, 403)
    
    # update actor
    def test_update_actor_success(self):
      """Test PATCH request to update actor as exec producer """
      res = self.client().patch('/update_actor/1',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        }, 
        json=self.update_actor)

      self.assertEqual(res.status_code, 201)

    def test_update_actor_fail(self):
      """Test PATCH request to update actor as casting assistant """
      res = self.client().patch('/update_actor/1',
        headers={
          "Authorization": "Bearer {}".format(self.casting_assistant)
        }, 
        json=self.update_actor)

      self.assertEqual(res.status_code, 403)

    # delete movie
    def test_delete_movie_fail(self):
      """Test DELETE request to delete movie as casting director """
      res = self.client().delete('/delete_movie/1',
        headers={
          "Authorization": "Bearer {}".format(self.casting_director)
        })

      self.assertEqual(res.status_code, 403)

    def test_delete_movie_success(self):
      """Test DELETE request to delete movie as exec producer """
      res = self.client().delete('/delete_movie/1',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        })

      self.assertEqual(res.status_code, 200)


    # delete actor
    def test_delete_actor_fail(self):
      """Test DELETE request for actor as casting assistant """
      res = self.client().delete('/delete_actor/1',
        headers={
          "Authorization": "Bearer {}".format(self.casting_assistant)
        })

      self.assertEqual(res.status_code, 403)

    def test_delete_actor_success(self):
      """Test DELETE request to delete actor as exec producer """
      res = self.client().delete('/delete_actor/1',
        headers={
          "Authorization": "Bearer {}".format(self.exec_producer)
        })

      self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()