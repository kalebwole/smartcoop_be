import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
            except Error as e:
                print(f"Error connecting to MySQL: {e}")
                self.connection = None

    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def create(self, query, params):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error executing CREATE operation: {e}")
        finally:
            cursor.close()

    def read(self, query, params=None):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing READ operation: {e}")
        finally:
            cursor.close()

    def update(self, query, params):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error executing UPDATE operation: {e}")
        finally:
            cursor.close()

    def delete(self, query, params):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error executing DELETE operation: {e}")
        finally:
            cursor.close()
