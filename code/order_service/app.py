
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([
        {'order_id': 1, 'product': 'Product 1', 'quantity': 2},
        {'order_id': 2, 'product': 'Product 2', 'quantity': 1},
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
