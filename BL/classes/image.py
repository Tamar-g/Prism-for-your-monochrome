import base64

import pyodbc
from matplotlib import pyplot as plt

from BL.classes.user import User
#from my_code.main import flow
from my_code.constants import NET_GAN_PATH, MODEL_PATH, SIZE


class My_image:
    def __init__(self, user_id=None, image_data=None):
        self.user_id = user_id
        self.image_data = image_data


    @staticmethod
    def get_connection():
        server = 'DESKTOP-70M95V5'
        database = 'prism'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)
        return conn

    def save(self):
        users = User.get_all_users()
        if any(user.user_id == self.user_id for user in users):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute('''
                    INSERT INTO images (user_ID, image)
                     VALUES (?, ?)
                 ''', (self.user_id, self.image_data))
            conn.commit()
            cursor.close()
            conn.close()
        else:
            print("User ID does not exist")
        print("successfully save in SQL!!")

    @staticmethod
    def get_all_images():
        conn = My_image.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM images')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [My_image(row[1], row[2]) for row in rows]  # Adjust the indices based on your table structure

    @staticmethod
    def get_image_by_id(image_id):
        conn = My_image.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM images WHERE image_ID = ?', (image_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return My_image(row[1], row[2])  # Adjust the indices based on your table structure
        return None

    #def send_image(image_path, mimetype='image/jpeg'):


    @staticmethod
    def get_last():
        conn = My_image.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT TOP 1 * FROM images ORDER BY image_ID DESC')
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return My_image(row[1], row[2])  # Adjust the indices based on your table structure
        return None

    def send_to_process(self, image):
        """
        colorful = flow(image)
        plt.imshow(colorful)
        plt.axis('off')
        plt.show()
        return colorful
        """
    def update(self, image_id):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
                UPDATE images
                SET user_ID = ?, image = ?
                WHERE image_ID = ?
            ''', (self.user_id, self.image_data, image_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(image_id):
        conn = My_image.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM images WHERE image_ID = ?', (image_id,))
        conn.commit()
        cursor.close()
        conn.close()


def encode_image(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
    return base64_image