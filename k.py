from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'products.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            price REAL NOT NULL
                        )''')
        conn.commit()

@app.route('/products', methods=['GET'])
def get_products():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT name, price FROM products")
        products = [{'name': row[0], 'price': row[1]} for row in cursor.fetchall()]
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (data['name'], data['price']))
        conn.commit()
    return jsonify({'status': 'Product added'}), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

