#!/usr/bin/env python3
"""
Write a function called filter_datum that
returns the log message obfuscated
"""
from typing import List
import re
import logging
from mysql import connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'password', 'ssn')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """__return__"""
    for msg in message.split(separator)[:]:
        message = re.sub(msg.split('=')[1], redaction,
                         message) if msg.split('=')[0] in fields else message
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialization"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """formatter"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """get logger function"""

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> connector.connection.MySQLConnection:
    """database connection"""
    params = {
        'host': os.environ.get('PERSONAL_DATA_DB_HOST', "localhost"),
        'user': os.environ.get('PERSONAL_DATA_DB_USERNAME', "root"),
        'password': os.environ.get('PERSONAL_DATA_DB_PASSWORD', ""),
        'database': os.environ.get('PERSONAL_DATA_DB_NAME')
    }
    return connector.connect(**params)


def main() -> None:
    """main function"""
    db = get_db()
    cursor = db.cursor()
    cursor.executr(
        "SELECT * FROM users \
         ORDER BY name, email, phone, ssn, password;"
        )
    for row in cursor:
        msg = "name={}; email={}; ssn={}; password={}; ip={}; \
            last_login={}; user_agent={}" \
        .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        print(msg)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
