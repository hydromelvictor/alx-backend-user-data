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

PII_FIELDS = ['name', 'email', 'phone', 'password', 'ip']


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    parameters
    ===========
    fields: List
    redaction: str
    message: str
    separator: str

    __return__:
    """
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
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """get logger function"""

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logger.setStreamHandler()
    handler.setFormater(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> connector.connection.MySQLConnection:
    """database connection"""
    params = {
        'host': os.environ.get('PERSONAL_DATA_DB_HOST', "localhost"),
        'user': os.environ('PERSONAL_DATA_DB_USERNAME', "root"),
        'password': os.environ('PERSONAL_DATA_DB_PASSWORD', ""),
        'database': os.environ('PERSONAL_DATA_DB_NAME')
    }
    return mysql.connector.connect(**params)


def main():
    """main function"""
    db = get_db()
    cursor = db.cursor()
    cursor.executr(
        "SELECT * FROM users \
         ORDER BY name, email, phone, ssn, password;"
        )
    for row in cursor:
        print(row)
    cursor.close()
    db.close()
