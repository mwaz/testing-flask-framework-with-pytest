import pytest
import json
from api import app


# test the root route
# @pytest.mark.one
def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_books_request():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list


def test_books_id():
    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode('utf-8')).get("Book")
    print(res)
    assert res['id'] == 1
    assert res['author'] == 'Havard'
    assert res['title'] == 'CS50'
    assert response.status_code == 200
