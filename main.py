import tmdb_client
from flask import Flask, render_template, request
import random

app = Flask(__name__)

MOVIE_LIST_TYPES = [
    'popular',
    'now_playing',
    'top_rated',
    'upcoming'
]

DEFAULT_LIST_TYPE_INDEX = 0

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if not selected_list in MOVIE_LIST_TYPES:
        selected_list = MOVIE_LIST_TYPES[DEFAULT_LIST_TYPE_INDEX]
    movies = tmdb_client.get_movies(how_many = 8, list_type = selected_list)
    return render_template('homepage.html', movie_list_types = MOVIE_LIST_TYPES, movies = movies, current_list = selected_list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {'tmdb_image_url': tmdb_image_url}

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template('movie_details.html', movie = details, cast = cast, selected_backdrop = selected_backdrop)
