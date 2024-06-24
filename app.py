from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# ダミーデータ
PRODUCTS = [
    {'id': 1, 'name': 'Product A', 'description': 'Description of Product A'},
    {'id': 2, 'name': 'Product B', 'description': 'Description of Product B'}
]

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = data['user_id']

    # ユーザーに基づいた推薦ロジック（ここではダミーのロジックを使用）
    recommended_products = {
        'products': PRODUCTS  # 実際のロジックではユーザーに適した商品を選定する
    }

    return jsonify(recommended_products), 200

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