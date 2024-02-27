
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([
        {'user_id': 1, 'name': 'User 1'},
        {'user_id': 2, 'name': 'User 2'},
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
