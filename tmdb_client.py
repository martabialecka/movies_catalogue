import requests
import random

API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDRmOTFjNTNjY2Q0ZTZmZmEyYmRhNjliODQxMGJjNyIsInN1YiI6IjYzZjliM2QzOTZlMzBiMDBiZTU5NTgzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5QE7Xpq92nIyP1jcJJ_qLO_RS_44e08M9SK8JD8jiGY'

def get_headers(api_token):
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }
    return headers

def get_movies_list(list_type):
    endpoint = f'https://api.themoviedb.org/3/movie/{list_type}'
    headers = get_headers(API_TOKEN)
    response = requests.get(endpoint, headers = headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size='w342'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    top = data['results'][:how_many]
    random.shuffle(top)
    return top

def get_single_movie(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}'
    headers = get_headers(API_TOKEN)
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    headers = get_headers(API_TOKEN)
    response = requests.get(endpoint, headers = headers)
    return response.json()['cast']

def get_movie_images(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    headers = get_headers(API_TOKEN)
    response = requests.get(endpoint, headers = headers)
    return response.json()
