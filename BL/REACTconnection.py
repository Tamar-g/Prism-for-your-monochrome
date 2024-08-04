import base64
import json
import os

import PIL.Image

from BL.classes.user import User
from my_code.constants import GRAY_CURRENT_IMAGE_PATH, COLORFUL_CURRENT_IMAGE_PATH
from PIL import Image
import io
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from BL.SQLconnetction import get_connection
from BL.classes.image import My_image
from BL.classes.user import User
from my_code.main import flow
import requests


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'
conn = get_connection()

save_path = "../gray_images/"


def send_image(image_path, mimetype='image/jpeg'):
    with open(image_path, 'rb') as img_file:
        files = {'file': (image_path, img_file, mimetype)}
        response = requests.post('http://localhost:5000/api/upload_image', files=files)  # Replace with your endpoint URL
        return response


@app.route('/api/upload_image', methods=['POST'])
@cross_origin("*")
def upload_image():
    try:
        my_image = GRAY_CURRENT_IMAGE_PATH
        image_bytes = my_image.read()
        response = jsonify({'image': image_bytes.decode('utf-8')}),200
        response.headers['Content-Type'] = 'image/jpeg'
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/api/get_all_users', methods=['GET'])
@cross_origin("*")
def get_users():
    users = User.get_all_users()
    return jsonify([user.__dict__ for user in users])


@app.route('/api/login', methods=['POST'])
@cross_origin("*")
def login():
    data = request.get_json()
    userName = data.get('userName')
    password = data.get('password')
    res = User.get_by_name_and_password(userName,password)
    if res:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "no in the db"}), 401


if __name__ == '__main__':
    app.run(port=5000, debug=True)
