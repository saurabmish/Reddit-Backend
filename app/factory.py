from app import app

@app.route('/')
def index():
    data = {'message': 'Hello, World!'}
    return data
