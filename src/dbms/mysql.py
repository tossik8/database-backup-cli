from mysql.connector import MySQLConnection, connect, Error
import subprocess

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

    
    def do_full_backup(self):
        cmd = [
            "mysqldump",
            "-u", self._con.user,
            f"-p",
            "-h", self._con._host,
            self._con.database
        ]
        with open("dump.sql", "w") as f:
            subprocess.run(cmd, stdout=f, text=True, encoding="utf-8")
        