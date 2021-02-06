from flask import request, jsonify
from app import app

posts = []

@app.route('/api/v2/post/create', methods=['POST'])
def create():
    data = request.get_json()
    postid = data['postid']
    title = data['title']
    text = data['text']
    published = data['published']
    community = data['community']

    new_post = {
        'postid': postid,
        'title': title,
        'text': text,
        'published': published,
        'community': community
    }
    posts.append(new_post)
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
            return jsonify(post), 201
    return {'message': "Unable to retrieve post ...", 'status': 402}


@app.route('/api/v2/post/retrieve/')
def recent_community_posts(community=None, top=0):
    """Multi-parameter route

    Retrieves *n* most recent posts from a particular community
    curl -i "localhost:6500/api/v2/post/retrieve?community=art&top=5"  
    """
    if community:
        filtered_posts = []
        community = request.args.get('community')
        top = request.args.get('top')
        for post in posts:
            if post['community'] == community:
                filtered_posts.append(post)
        return filtered_posts[:top]
    return {'message': "Community does not exist ...", 'status': 402}


@app.route('/api/v2/post/retrieve/<string:community>/<int:top>')
def recent_posts(community=None, top=0):
    """Multi-query parameter
    
    Retrieve *n* most recent posts from any community
    Almost the same as the above route, except 
    """
    if community:
        filtered_posts = []
        community = request.args.get('community')
        top = request.args.get('top')
        for post in posts:
            if post['community'] == community:
                filtered_posts.append(post)
        return filtered_posts[:top]
    return {'message': "Community does not exist ...", 'status': 402}    
