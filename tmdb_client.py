import requests
import random

def get_popular_movies():
    endpoint = 'https://api.themoviedb.org/3/movie/popular'
    api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMDRmOTFjNTNjY2Q0ZTZmZmEyYmRhNjliODQxMGJjNyIsInN1YiI6IjYzZjliM2QzOTZlMzBiMDBiZTU5NTgzYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5QE7Xpq92nIyP1jcJJ_qLO_RS_44e08M9SK8JD8jiGY'
    headers = {
        'Authorization': f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size='w342'):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'

def get_movies(how_many):
    data = get_popular_movies()
    random.shuffle(data['results'])
    return data['results'][:how_many]
