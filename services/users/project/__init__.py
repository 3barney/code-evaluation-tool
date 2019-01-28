import os
import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Instantiate app
app = Flask(__name__)

# Read env vars from compose dev file
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

# Database Model
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False)
  active = db.Column(db.Boolean(), default=True, nullable=False)

  def __init__(self, username, email):
    self.username = username
    self.email = email


# Routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'success',
    'message': 'ping pong'
  })