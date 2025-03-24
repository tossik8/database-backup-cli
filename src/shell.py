from cmd import Cmd
import argparse
from .dbms.mysql import MySQL


class DBBackupShell(Cmd):

    prompt = "dbbackup> "
    intro = "Welcome to dbbackup. Type 'help' for commands."

    def __init__(self):
        super().__init__()
        self._dbms = None


    def _get_connect_parser(self):
        parser = argparse.ArgumentParser(
            prog="connect",
            description="Connect to a database.",
        )
        parser.add_argument("dbms", help="Database Management System")
        parser.add_argument("user")
        parser.add_argument("password")
        parser.add_argument("host")
        parser.add_argument("db", help="Name of the database")
        return parser
    

    def _set_dbms(self, dbms: str):
        if dbms == "mysql":
            self._dbms = MySQL()
        else:
            raise NotImplementedError(f"'{dbms}' is not supported")


    def do_connect(self, arg: str):
        """Connect to a database. For more info, use connect -h"""
        parser = self._get_connect_parser()
        args = arg.split()
        if "-h" in args or "--help" in args:
            parser.print_help()
            return
        try:
            args = vars(parser.parse_args(args))
        except SystemExit:
            return
        try:
            self._set_dbms(args["dbms"])
        except NotImplementedError as e:
            print(e)
            return
        try:
            self._dbms.connect(args["user"], args["password"], args["host"], args["db"])
        except ConnectionError as e:
            print(e)
            return
        

    def do_full_backup(self, arg: str):
        self._dbms.do_full_backup()


def main():
    DBBackupShell().cmdloop()


if __name__ == "__main__":
    main()