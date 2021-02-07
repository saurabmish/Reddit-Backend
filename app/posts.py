from flask import request, jsonify
from app import app

posts = []

@app.route('/api/v2/post/create', methods=['POST'])
def create():
    json_data = request.get_json()
    posts.append(json_data)
    return {'message': "Post created successfully!", 'status': 202}


@app.route('/api/v2/post/delete/<int:postid>', methods=['DELETE'])
def delete(postid):
    for index, post in enumerate(posts):
        if post["postid"] == postid:
            posts.pop(index)
            return {'message': "Post deleted successfully!", 'status': 202}
    return {'message': "Post could not be deleted because it was not found", 'status': 402}


@app.route('/api/v2/post/retrieve/<int:postid>', methods=['GET'])
def retrieve(postid):
    for post in posts:
        if post["postid"] == postid:
            return post, 203
    return {'message': "Unable to retrieve post ...", 'status': 402}


@app.route('/api/v2/post/retrieve', methods=['GET'])
def recent_posts():
    """Multi-parameter Route

    Retrieves *n* most recent posts from a particular community
    curl -i "localhost:6500/api/v2/post/retrieve?community=art&top=5"  
    """
    community = request.args.get('community', type=str)
    top       = request.args.get('top', type=int)
    filtered_posts = []
    if community:
        for post in posts:
            if post['community'] == community:
                filtered_posts.append(post)
    
    if len(filtered_posts) == 0:
        return {'message': 'Community does not exist ...', 'status': 402}
    return jsonify({
        'data': filtered_posts[:top],
        'message': "Filtered data based on community",
        'status': 203
    })


@app.route('/api/v2/posts/all', methods=['GET'])
def get_all_posts():
    """Aids in testing."""
    return jsonify(posts), 201
