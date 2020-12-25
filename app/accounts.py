from flask import request, jsonify
from app import app

users = []

@app.route('/api/v1/user/create', methods=['POST'])
def signup():
    data = request.get_json()
    print(data)
    name = data["name"]
    location = data["location"]
    gender = data["gender"]
    
    new_user = {
        "name":  name,
        "location":  location,
        "gender":  gender
    }
    users.append(new_user)

    return {'message': "User created successfully!", 'status': 201}


@app.route('/api/v1/user/get-all', methods=['GET'])
def get_all():
    return jsonify(users), 201


@app.route('/api/v1/user/get/<string:name>', methods=['GET'])
def get_user(name):
    for user in users:
        if user["name"] == name:
            return jsonify(user), 201    
    return {'message': 'User not found ...', 'status': 406}


@app.route('/api/v1/user/update-location/<string:name>', methods=['PATCH'])
def update_location(name):
    data = request.get_json()
    for user in users:
        if user["name"] == name:
            user["location"] = data["location"]
            updated_user = {
                "name":  user["name"],
                "location": user["location"],
                "gender": user["gender"]
            }
            return jsonify(updated_user), 205


@app.route('/api/v1/user/delete/<string:name>', methods=['DELETE'])
def delete_user(name):
    for index, user in enumerate(users):
        if user["name"] == name:
            users.pop(index)
            return jsonify(users), 202