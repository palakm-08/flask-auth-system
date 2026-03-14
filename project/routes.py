from project import app, db

@app.route('/register')
def register_page():
    return "Flask app is running"

@app.route('/login')
def login_page():
    return "Flask is running"