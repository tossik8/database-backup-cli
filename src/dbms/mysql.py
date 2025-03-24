from mysql.connector import MySQLConnection, connect, Error

class MySQL:

    def __init__(self):
        self._con: MySQLConnection = None

    def connect(self, user: str, password: str, host: str, database: str):
        try:
            self._con = connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
        except Error as e:
            raise ConnectionError(e) from e
        