from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['GET'])
def recommend():
    recommendations = ["Product A", "Product B"]
    return jsonify({"recommendations": recommendations})

@app.route('/update_model', methods=['POST'])
def update_model():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    amount = data.get('amount')
    print(f"Updating model for user {user_id} with product {product_id} and amount {amount}")
    return jsonify({'message': 'Model updated successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)