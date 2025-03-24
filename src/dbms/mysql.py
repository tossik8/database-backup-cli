import mysql.connector

class MySQL:

    def __init__(self):
        self._con = None

    def connect(self, user, password, host, database):
        try:
            self._con = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
        except mysql.connector.Error as e:
            raise ConnectionError(e) from e
        