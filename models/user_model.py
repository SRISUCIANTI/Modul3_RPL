import hashlib
import mysql.connector

class UserModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, username, password):
        hashed_password = self.hash_password(password)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, hashed_password))
        return self.cursor.fetchone()