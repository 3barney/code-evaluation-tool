from flask import Flask, jsonify

app = Flask(__name__) # Instantiate app

@app.route('/users/ping', methods=['GET'])
def ping_pong():
  return jsonify({
    'status': 'success',
    'message': 'ping pong'
  })