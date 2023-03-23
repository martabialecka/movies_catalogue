import requests
import random

API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDRmOTFjNTNjY2Q0ZTZmZmEyYmRhNjliODQxMGJjNyIsInN1YiI6IjYzZjliM2QzOTZlMzBiMDBiZTU5NTgzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5QE7Xpq92nIyP1jcJJ_qLO_RS_44e08M9SK8JD8jiGY'

def call_tmdb_api(endpoint):
   full_url = f'https://api.themoviedb.org/3/movie/{endpoint}'
   headers = {
       "Authorization": f'Bearer {API_TOKEN}'
   }
   response = requests.get(full_url, headers = headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f'{list_type}')

def get_poster_url(poster_api_path, size = 'w342'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    top = data['results'][:how_many]
    random.shuffle(top)
    return top

def get_single_movie(movie_id):
    return call_tmdb_api(f'{movie_id}')

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f'{movie_id}/credits')['cast']

def get_movie_images(movie_id):
    return call_tmdb_api(f'{movie_id}/images')
