import pyodbc
from flask import Flask, jsonify, request
from flask_cors import cross_origin

from BL.classes.user import User
#from  import app
#from  BL.local_main import conn

app = Flask(__name__)

server = 'DESKTOP-70M95V5'
database = 'prism'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)

@staticmethod
def get_connection():
    server = 'DESKTOP-70M95V5'
    database = 'prism'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)
    print("connection to SQL was successfully")
    return conn

@app.route('/api/get_all_users', methods=['GET'])
@cross_origin("*")
def get_users():
    users = User.get_all_users()
    return jsonify([user.__dict__ for user in users])



@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401


# Endpoint to add a new user
@app.route('/api/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (user_name, uesr_password, is_admin)
        VALUES (?, ?, ?)
    ''', (data['user_name'], data['uesr_password'], data['is_admin']))
    conn.commit()
    return jsonify({'message': 'User added successfully'}), 201


@app.route('/api/get_all_users', methods=['GET'])
def get_users():
    users = User.get_all_users()
    return jsonify([user.__dict__ for user in users])

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify(user.__dict__)
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.get_user_by_id(user_id)
    if user:
        user.user_name = data['user_name']
        user.user_password = data['uesr_password']
        user.is_admin = data['is_admin']
        user.update()
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        User.delete(user_id)
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

