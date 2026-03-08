from project import app
from project import db

@app.route('/')
def home():
    return "Flask app is running"