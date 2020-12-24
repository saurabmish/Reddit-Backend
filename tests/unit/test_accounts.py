from flask import json


def test_user_signup_message(client):
    url = '/api/v1/user/create'
    user = {
        "name": "Hannah",
        "location": "Fullerton",
        "gender": "F"
    }
    response = client.post(url, data=json.dumps(user), 
                           content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "User created successfully" in data['message']


def test_user_signup_status(client):
    url = '/api/v1/user/create'
    user = {
        "name": "Jennifer",
        "location": "Anaheim",
        "gender": "F"
    }
    response = client.post(url, data=json.dumps(user), 
                           content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert 201 == data['status']


def test_get_all_users_content_type(client):
    response = client.get('/api/v1/user/get-all')
    assert response.content_type == 'application/json'


def test_get_all_users_status(client):
    response = client.get('/api/v1/user/get-all')
    assert response.status_code == 201


def test_get_user_name(client):
    response = client.get('/api/v1/user/get/Jennifer')
    data = json.loads(response.get_data(as_text=True))
    assert "Jennifer" in data["name"]


def test_get_user_location(client):
    response = client.get('/api/v1/user/get/Jennifer')
    data = json.loads(response.get_data(as_text=True))
    assert "Anaheim" in data["location"]


def test_get_user_gender(client):
    response = client.get('/api/v1/user/get/Jennifer')
    data = json.loads(response.get_data(as_text=True))
    assert "F" in data["gender"]


def test_get_user_status(client):
    response = client.get('/api/v1/user/get/Jennifer')
    assert response.status_code == 201


def test_update_user_location(client):
    """TODO."""
    pass


def test_update_user_location_status(client):
    """TODO."""
    pass


def test_delete_user_status(client):
    """TODO."""
    pass