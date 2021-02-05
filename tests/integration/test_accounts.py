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


def test_upvote_user_message_and_status(client):
    response = client.patch('/api/v2/user/Jennifer/karma/increment')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202  and 'Karma incremented successfully' in data["message"]


def test_upvote_user_not_found_message_and_status(client):
    response = client.patch('/api/v2/user/Testing/karma/increment')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 402  and 'User karma not incremented, user not found' in data["message"]


def test_downvote_user_message_and_status(client):
    response = client.patch('/api/v2/user/Adam/karma/decrement')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202  and 'Karma decremented successfully' in data["message"] 


def test_downvote_user_not_found_message_and_status(client):
    response = client.patch('/api/v2/user/TesUser123/karma/decrement')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 402  and 'User karma not decremented, user not found' in data["message"]


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


def test_update_email_user_not_found_message(client):
    url = '/api/v2/user/update/Testuser'
    user_data = {
        "userid": 2,
        "username": "Testuser",
        "email": "testuser@gmail.com",
        "karma": 1
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert "Email not updated, user not found" in data['message']


def test_update_email_user_not_found_status(client):
    url = '/api/v2/user/update/Testuser'
    user_data = {
        "userid": 2,
        "username": "Testuser",
        "email": "testuser@gmail.com",
        "karma": 1
    }
    response = client.patch(url, data=json.dumps(user_data),
                            content_type='application/json')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 402


def test_delete_user_message_and_status(client):
    response = client.delete('/api/v2/user/delete/Adam')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == 202  and 'User deleted successfully' in data["message"]


def test_delete_user_not_found_message_and_status(client):
    response = client.delete('/api/v2/user/delete/Saurabh')
    data = json.loads(response.get_data(as_text=True))
    assert data['status'] == 402 and 'User not deactivated, user not found' in data['message']


def test_get_all_users_content_type(client):
    response = client.get('/api/v2/users/all')
    assert response.content_type == 'application/json'


def test_get_all_users_status(client):
    response = client.get('/api/v2/users/all')
    assert response.status_code == 201
