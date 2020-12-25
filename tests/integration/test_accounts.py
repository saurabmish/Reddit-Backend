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


def test_no_user_message(client):
    response = client.get('/api/v1/user/get/Saurabh')
    data = json.loads(response.get_data(as_text=True))
    assert 'User not found' in data['message']


def test_no_user_status(client):
    response = client.get('/api/v1/user/get/Saurabh')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 406


def test_update_user_location_status(client):
    url = '/api/v1/user/update-location/Hannah'
    user_data = {
        "name": "Hannah",
        "location": "Santa Ana",
        "gender": "F"
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    assert response.status_code == 205


def test_update_user_location_name(client):
    url = '/api/v1/user/update-location/Hannah'
    user_data = {
        "name": "Hannah",
        "location": "Santa Ana",
        "gender": "F"
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "Hannah" in data["name"]


def test_update_user_location(client):
    url = '/api/v1/user/update-location/Hannah'
    user_data = {
        "name": "Hannah",
        "location": "Santa Ana",
        "gender": "F"
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "Santa Ana" in data["location"]


def test_update_user_location_gender(client):
    url = '/api/v1/user/update-location/Hannah'
    user_data = {
        "name": "Hannah",
        "location": "Santa Ana",
        "gender": "F"
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "F" in data["gender"]


def test_delete_user_status(client):
    """TODO."""
    pass