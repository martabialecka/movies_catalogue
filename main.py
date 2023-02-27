import tmdb_client
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many = 8)
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}
