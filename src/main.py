import argparse
import mysql.connector
import logging


def main():
    logger = logging.getLogger()
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    parser = argparse.ArgumentParser(description="Database backup tool")
    args = parser.parse_args()

    try:
        logger.info("Connecting to database...")
        con = mysql.connector.connect(user="root", password="mysecretpassword", host="127.0.0.1", database="mydatabase")
    except mysql.connector.Error as e:
        logger.error(e)
    else:
        logger.info("Connected")
        print(con.cmd_statistics())
        con.close()

if __name__ == "main":
    main()