## Overview

Project created for the Udacity Full Stack Nanodegree Program's Capstone.

The project provides an API for a fictitious casting agency that manages a list of actors and movies.

URL hosted at: https://udacity-fs-capstone.herokuapp.com/

## API endpoints

GET /actors

- Returns a list of actors with id, name, age, and gender

GET /movies

- Returns a list of movies with id, title, and release data

POST /actors

- Creates a new actor using the submited name, age, and gender
- Returns "Success" and 201 status code if successful

POST /movies

- Creates a new movie using the submited id, title, and release data
- Returns "Success" and 201 status code if successful

PATCH /actors/{actor_id}

- Updates the provided attributes for an actor based on actor_id
- Returns "Success" and 201 status code if successful

PATCH /movies/{movie_id}

- Updates the provided attributes for a movie based on movie_id
- Returns "Success" and 201 status code if successful

DELETE /actors/{actor_id}

- DELETES the actor with the specified actor_id
- Returns "Success" and 201 status code if successful

DELETE /movies/{movie_id}

- DELETES the movie with the specified movie_id
- Returns "Success" and 201 status code if successful

## Project dependencies

Project built using Flask, SQLAlchemy, and a PostgreSQL database. For a full list of dependencies, please see the requirements.txt file

## Uploading to Heroku

To deploy to Heroku, use the Heroku CLI to deploy the API
For more information, see deploying on Heroku: https://devcenter.heroku.com/categories/deployment

## Authentication instructions

To login, use the following login screen from Auth0:
https://fscourse.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=wiMucRnjYYKGlAFuQq8zxJJD2r8ROUJp&redirect_uri=https://127.0.0.1:5000/

There are three roles with different levels of permissions:

1. Casting Assistant: Can use GET request for actors and movies
2. Casting Director: Casting Assitant and:

- PATCH request for updating actors and movies
- POST request to add an actor
- DELETE request to delete an actor

3. Executive Producer: Casting Director and:

- POST request to add a movie
- DELETE request to delete a movie

There are three roles with the following tokens:

- Executive Producer: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlkZmp1RjdEXzQtVFI0cGJxMkVIYyJ9.eyJpc3MiOiJodHRwczovL2ZzY291cnNlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDMyNmQyMWFmNTA0NjAwNjk2Mjk4NTQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyNzE3NzUyMiwiZXhwIjoxNjI3MjYzOTIyLCJhenAiOiJ3aU11Y1JuallZS0dsQUZ1UXE4enhKSkQycjhST1VKcCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiYWRkOm1vdmllIiwiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.Zyaere6rwxt7VhxVEtl5zO9jwvwezT1-XlhTRgouOCX0FnUEgdtxOB3qggECAJom3CdQktQW2P3MWh7NnJSVbRjWDeplPUyOtv8gZIobmYuXDVklFaH9Aoh2jcLXCqhQjxuSXnw_dTAsMXkzxAjKD_Z4I6O-QmuOCVPZSAUQdeIRAtO8AGD1QL-lT3KmfzG9bpZinVNinyYUV6bnE3BTIyHwJ3rxP7w860BzfR9lF50W4tt0eOqnB4Z5N1PMmnAwOhiBEMa7lx_sZas8kzPuJmf3XwioOtt1nZNec8DDDYvZZjw0P4H-pVv-PCQWVo_3i5-xfXgCq13e4g36Mnwmaw
- Casting Director: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlkZmp1RjdEXzQtVFI0cGJxMkVIYyJ9.eyJpc3MiOiJodHRwczovL2ZzY291cnNlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDMyNmQyMWFmNTA0NjAwNjk2Mjk4NTQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyNzE0NTU1NiwiZXhwIjoxNjI3MjMxOTU2LCJhenAiOiJ3aU11Y1JuallZS0dsQUZ1UXE4enhKSkQycjhST1VKcCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9yIiwiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3IiLCJ1cGRhdGU6bW92aWUiXX0.illDJ_g2rwyl32dd1MH0pkFobqtcBYhe24PLI_ZASpWRlVdyQyMIQJHpJIVD0kwYJatmfrHscBKcviClpNy8gZ6qEvSHmazP7iNz0bCRTJc55qdVvYYueW4Sr57VmJ1vsSPj_cXe8CqlqH1BeirJsi4YzGmr5giEUVokojR6p4KGstX4p0QVtBIRQx6akkTrYW4XOJr5srvWnFWkqD4bwlLreqy_ThUSy4Wo7_4EAU-gxTJE2EmtBIPTUDf_0fREVAKRyTrTO8pM4UjessAml9VSh2dk8O8ukjHQduxovT_tZhiMcB-YAgru0e6ALdJt1dQsCdvQQmT4GZDK1WqpbQ
- Casting Assistant: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InlkZmp1RjdEXzQtVFI0cGJxMkVIYyJ9.eyJpc3MiOiJodHRwczovL2ZzY291cnNlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDMyNmQyMWFmNTA0NjAwNjk2Mjk4NTQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTYyNzE0NTYzOCwiZXhwIjoxNjI3MjMyMDM4LCJhenAiOiJ3aU11Y1JuallZS0dsQUZ1UXE4enhKSkQycjhST1VKcCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Oy1gQNE81I8NS52GwdUgSvRfE5UExeMlJc0GqvIFLJct-q2VR4G6VN4eqZHxIjD7zyP-3wGNXqvTnR0FUty-3FT1NNftrqwURm6z39_FkZITNJ7s_u1-oeqv-wjoiiZUqjNIzN4GL8WuSFl2gfEpbhpci5-dR-uoNlOQZL386_CfJ0hohl7LLErHHyLXNVnGqzxrqs22wCDGeQqX9W-SWPQRLiM7fQVYNhiENv-CA_wY5kJkpxGKjApPVw7XtwnEEYU0Hz-burKidWcBzdlZZCc5L_IcvJ2_UuqVMsohpFU7647S4nxnu4CjlfyhpXFKvjDE7krIC3An5CFwrrU63A
