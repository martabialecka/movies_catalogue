import tmdb_client
from main import app
from main import MOVIE_LIST_TYPES, DEFAULT_LIST_TYPE_INDEX
from unittest.mock import Mock
import pytest

def test_call_tmdb_api(monkeypatch):
    some_endpoint = 'some_endpoint'
    mock_some_json = '{"some": "json"}'
    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_some_json
    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
    some_json = tmdb_client.call_tmdb_api(some_endpoint)

    assert some_json == mock_some_json
    assert some_endpoint in requests_mock.call_args[0][0]

def test_get_single_movie(monkeypatch):
    movie_id = 5
    call_tmdb_api_mock = Mock()
    monkeypatch.setattr('tmdb_client.call_tmdb_api', call_tmdb_api_mock)
    tmdb_client.get_single_movie(movie_id)
    assert f'{movie_id}' in call_tmdb_api_mock.call_args[0][0]

def test_get_movie_images(monkeypatch):
    movie_id = 53
    call_tmdb_api_mock = Mock()
    monkeypatch.setattr('tmdb_client.call_tmdb_api', call_tmdb_api_mock)
    tmdb_client.get_movie_images(movie_id)
    endpoint = call_tmdb_api_mock.call_args[0][0]
    assert f'{movie_id}' in endpoint
    assert 'images' in endpoint

def test_get_single_movie_cast(monkeypatch):
    movie_id = 534
    mock_cast = 'pass'
    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = {
        'cast': mock_cast
    }
    monkeypatch.setattr('tmdb_client.call_tmdb_api', call_tmdb_api_mock)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    endpoint = call_tmdb_api_mock.call_args[0][0]
    assert f'{movie_id}' in endpoint
    assert 'credits' in endpoint
    assert cast == mock_cast

# Test all movie list types and a default one with an empty string.
# sum trick flattens a list of lists.
@pytest.mark.parametrize('category', sum([[''], MOVIE_LIST_TYPES], []))
def test_homepage(monkeypatch, category):
    api_mock = Mock(return_value = {'results': []})
    monkeypatch.setattr('tmdb_client.call_tmdb_api', api_mock)

    if category:
        get = f'/?list_type={category}'
    else:
        get = '/'
        category = MOVIE_LIST_TYPES[DEFAULT_LIST_TYPE_INDEX]

    with app.test_client() as client:
        response = client.get(get)
        assert response.status_code == 200
        api_mock.assert_called_once_with(category)
