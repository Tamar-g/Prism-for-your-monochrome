import pyodbc
from flask import Flask, jsonify, request

from BL.classes.image import My_image
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

@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    gray_image = My_image(user_id=data['user_id'], image_data=data['image_data'].encode('utf-8'))
    ##colorful_image =gray_image.send_to_process(gray_image.image_data)
    #get_image_after_processing(colorful_image)
    #image.save()
    if gray_image:
        return jsonify({'message': 'Image added successfully'}), 200
    else:
        return jsonify({'error': 'error!!!'}), 401


@app.route('/api/get_image_after_processing', methods=['GET'])
def get_image_after_processing(colorful_image):
    if colorful_image:
        return jsonify({'message': 'Image added successfully'}), 200
    else:
        return jsonify({'error': 'error!!!'}), 401

