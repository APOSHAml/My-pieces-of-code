from time import sleep

import pytest
from urllib import request, error
import json
import requests



@pytest.fixture(scope="function")
def base_url():
    yield 'https://jsonplaceholder.typicode.com'

def test_get_request_post(base_url):
    req = request.Request(f'{base_url}/posts/1')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert len(response) == 4
    assert response['id'] == 1



def test_created_post(base_url):
    req = request.Request(f'{base_url}/posts', method='POST')
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "My cool title",
            "body": "My cool text",
            "userId": 136
        }
    ).encode('ascii')
    response = request.urlopen(req).read().decode('utf-8')
    response = json.loads(response)
    assert response['title'] == "My cool title"


def test_update_put(base_url):
    req = request.Request(f'{base_url}/posts/1')
    req.method = 'PUT'
    req.add_header('Content-Type', 'application/json')
    req.data = json.dumps(
        {
            "title": "My cool title update",
            "body": "My cool text",
            "userId": 1
        }
    ).encode('ascii')
    response = json.loads((request.urlopen(req).read().decode('utf-8')))


def test_delete(base_url):
    post_id = '101'
    req = request.Request(f'{base_url}/posts/{post_id}')
    req.method = 'DELETE'
    request.urlopen(req)
    req = request.Request(f'{base_url}/posts/{post_id}')
    try:
        request.urlopen(req)
    except error.HTTPError as err:
        assert err.code == 404
        return
    assert False


def test_request(base_url):
    url = f'{base_url}/posts'
    response = requests.request('get', f'{base_url}/posts')
    headers = {
        'fdsfds': 'sdfdsf'
    }
    data = json.dumps({"name": "Siarhei"})
    response = requests.request('POST', url, headers=headers, data=data)