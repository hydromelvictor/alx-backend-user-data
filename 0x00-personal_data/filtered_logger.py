#!/usr/bin/env python3
"""
Write a function called filter_datum that
returns the log message obfuscated
"""
from typing import List
import re
import logging


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
    msgs = message
    for msg in message.split(separator):
        msgs = re.sub(msg.split('=')[1], redaction,
                      msgs) if msg.split('=')[0] in fields else msgs
    return msgs


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