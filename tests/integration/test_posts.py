from datetime import datetime
from flask import json, jsonify

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


def test_retrieve_recent_posts_from_existing_community(client):
    post1 = {
        "postid": 2,
        "title": "Heading 2",
        "text": "Content of post 2",
        "published": datetime.utcnow(),
        "community": "tech"
    }
    post2 = {
        "postid": 3,
        "title": "Heading 3",
        "text": "Content of post 3",
        "published": datetime.utcnow(),
        "community": "tech"
    }
    post3 = {
        "postid": 4,
        "title": "Heading 4",
        "text": "Content of post 4",
        "published": datetime.utcnow(),
        "community": "tech"
    }
    client.post('/api/v2/post/create', data=json.dumps(post1), content_type='application/json')
    client.post('/api/v2/post/create', data=json.dumps(post2), content_type='application/json')
    client.post('/api/v2/post/create', data=json.dumps(post3), content_type='application/json')

    response = client.get('/api/v2/post/retrieve?community=tech&top=2')
    data = json.loads(response.get_data(as_text=True))
    assert "Filtered data" in data["message"] and data["status"] == 203


def test_retrieve_recent_posts_from_non_existent_community(client):
    response= client.get('/api/v2/post/retrieve?community=testcomm&top=2')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 402 and 'Community does not exist' in data["message"]
