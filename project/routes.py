from project import app, db

@app.route('/')
def home():
    return "Flask app is running"