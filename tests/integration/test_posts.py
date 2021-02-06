from datetime import datetime
from flask import json


def test_create_post_message(client):
    post1 = {
        "postid": 1,
        "title": "Heading 1",
        "text": "Content of post 1",
        "published": datetime.utcnow(),
        "community": "tech"
    }
    url = '/api/v2/post/create'
    response = client.post(url, data=json.dumps(post1),
                           content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202 and "Post created successfully" in data['message']


def test_retrieve_existing_post(client):
    response = client.get('/api/v2/post/retrieve/1')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 203


def test_retrieve_non_existing_post(client):
    response = client.get('/api/v2/post/retrieve/101')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 402 and 'Unable to retrieve post' in data['message']


def test_delete_existing_post(client):
    response = client.delete('/api/v2/post/delete/1')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202  and 'Post deleted successfully' in data["message"]


def test_delete_non_existing_post(client):
    response = client.delete('/api/v2/post/delete/101')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 402  and 'Post could not be deleted because it was not found' in data["message"]
