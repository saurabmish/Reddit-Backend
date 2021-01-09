from flask import json


def test_user_signup_message(client):
    url = '/api/v2/user/create'
    user = {
        "userid": 1,
        "username": "Adam",
        "email": "adam@gmail.com",
        "karma": 1
    }
    response = client.post(url, data=json.dumps(user),
                           content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "User created successfully" in data['message']


def test_user_signup_status(client):
    url = '/api/v2/user/create'
    user = {
        "userid": 2,
        "username": "Jennifer",
        "email": "jennifer@gmail.com",
        "karma": 1
    }
    response = client.post(url, data=json.dumps(user),
                           content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert 202 == data['status']


def test_update_user_email_status(client):
    url = '/api/v2/user/update/Jennifer'
    user_data = {
        "userid": 2,
        "username": "Jennifer",
        "email": "jennifer_g@gmail.com",
        "karma": 1
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 202


def test_update_user_email_message(client):
    url = '/api/v2/user/update/Jennifer'
    user_data = {
        "userid": 2,
        "username": "Jennifer",
        "email": "jennifer_g@gmail.com",
        "karma": 1
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "Email updated successfully" in data['message']


def test_delete_user_status_and_message(client):
    response = client.delete('/api/v2/user/delete/Adam')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202  and 'User deleted successfully' in data["message"]


def test_delete_user_not_found_status(client):
    response = client.delete('/api/v2/user/delete/Saurabh')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 402


def test_delete_user_not_found_message(client):
    response = client.delete('/api/v2/user/delete/Saurabh')
    data = json.loads(response.get_data(as_text=True))
    assert 'User not deactivated, user not found' in data['message']


def test_get_all_users_content_type(client):
    response = client.get('/api/v2/users/all')
    assert response.content_type == 'application/json'


def test_get_all_users_status(client):
    response = client.get('/api/v2/users/all')
    assert response.status_code == 201
