from flask import request, jsonify
from app import app

users = []

@app.route('/api/v2/user/create', methods=['POST'])
def signup():
    data = request.get_json()
    userid = data["userid"]
    username = data["username"]
    email = data["email"]
    karma = data["karma"]

    new_user = {
        "userid": userid,
        "username":  username,
        "email":  email,
        "karma":  karma
    }
    users.append(new_user)
    return {'message': "User created successfully!", 'status': 202}


@app.route('/api/v2/user/<string:username>/karma/increment', methods=['PATCH'])
def upvote_user(username):
    for user in users:
        if user["username"] == username:
            user["karma"] += 1
            updated_user = {
                "userid": user["userid"],
                "username":  user["username"],
                "email": user["email"],
                "karma": user["karma"]
            }
            return {'message': 'Karma incremented successfully!', 'status': 202}
    return {'message': 'User karma not incremented, user not found ...', 'status': 402}


@app.route('/api/v2/user/<string:username>/karma/decrement', methods=['PATCH'])
def downvote_user(username):
    for user in users:
        if user["username"] == username:
            user["karma"] -= 1
            updated_user = {
                "userid": user["userid"],
                "username":  user["username"],
                "email": user["email"],
                "karma": user["karma"]
            }
            return {'message': 'Karma decremented successfully!', 'status': 202}
    return {'message': 'User karma not decremented, user not found ...', 'status': 402}


@app.route('/api/v2/user/update/<string:username>', methods=['PATCH'])
def update_email(username):
    data = request.get_json()
    for user in users:
        if user["username"] == username:
            user["email"] = data["email"]
            updated_user = {
                "userid": user["userid"],
                "username":  user["username"],
                "email": user["email"],
                "karma": user["karma"]
            }
            return {'message': 'Email updated successfully!', 'status': 202}
    return {'message': 'Email not updated, user not found ...', 'status': 402}


@app.route('/api/v2/user/delete/<string:username>', methods=['DELETE'])
def deactivate(username):
    for index, user in enumerate(users):
        if user["username"] == username:
            users.pop(index)
            return {'message': "User deleted successfully!", 'status': 202}
    return {'message': 'User not deactivated, user not found ...', 'status': 402}


@app.route('/api/v2/users/all', methods=['GET'])
def get_all_accounts():
    """Aids in testing."""
    return jsonify(users), 201
