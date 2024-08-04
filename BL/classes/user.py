import pyodbc

import BL.classes.user


class User:
    def __init__(self, user_id=None, user_name=None, user_password=None, is_admin=False):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.is_admin = is_admin

    @staticmethod
    def get_connection():
        server = 'DESKTOP-70M95V5'
        database = 'prism'
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)
        return conn

    def save(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
               INSERT INTO users (user_name, uesr_password, is_admin)
               VALUES (?, ?, ?)
           ''', (self.user_name, self.user_password, self.is_admin))
        conn.commit()
        cursor.close()
        conn.close()
        print("successfully save in SQL")

    @staticmethod
    def get_all_users():
        conn = User.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [User(row[0], row[1], row[2], row[3]) for row in rows]



    @staticmethod
    def get_user_by_id(user_id):
        conn = User.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_ID = ?', (user_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return User(row[0], row[1], row[2], row[3])
        return None

    def update(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users
            SET user_name = ?, uesr_password = ?, is_admin = ?
            WHERE user_ID = ?
        ''', (self.user_name, self.user_password, self.is_admin, self.user_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(user_id):
        conn = User.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE user_ID = ?', (user_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_name_and_password(user_name, user_password):
        conn = User.get_connection()
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM users WHERE user_name = ? and uesr_password = ?', (user_name,user_password))
        conn.commit()
        cursor.close()
        conn.close()
        return res