import pyodbc

@staticmethod
def get_connection():
    server = 'DESKTOP-70M95V5'
    database = 'prism'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database)
    print("connection to SQL was successfully")
    return conn
