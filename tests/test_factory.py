from flask import json


def test_response_type(client):
    response = client.get('/')
    assert response.content_type == 'application/json'

def test_response_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index(client):
    response = client.get('/')
    data = json.loads(response.get_data(as_text=True))
    #assert response.get_json()["message"] == "Hello, World!"   # from v1.0
    assert 'Hello, World!' in data['message']
