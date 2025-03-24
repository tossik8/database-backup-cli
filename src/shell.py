from cmd import Cmd
import argparse
import logging
import mysql.connector


class DBBackupShell(Cmd):

    prompt = "dbbackup> "
    intro = "Welcome to dbbackup. Type 'help' for commands."

    def __init__(self):
        super().__init__()
        self.connection = None
        self.logger = logging.getLogger()


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


    def do_connect(self, arg: str):
        """Connect to a database. For more info, use connect -h"""
        parser = self._get_connect_parser()
        args = arg.split()
        if "-h" in args or "--help" in args:
            parser.print_help()
            return
        try:
            args = vars(parser.parse_args(args))
        except SystemExit as e:
            return 
        self.logger.info("Connecting to database...")
        try:
            self.connection = mysql.connector.connect(
                user=args["user"],
                password=args["password"],
                host=args["host"],
                database=args["db"]
            )
        except mysql.connector.Error as e:
            self.logger.error(e)
            return
        self.logger.info("Connected")


def main():
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    DBBackupShell().cmdloop()


if __name__ == "__main__":
    main()