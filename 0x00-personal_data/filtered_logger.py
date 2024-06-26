#!/usr/bin/env python3
"""
PII (Personally Identifiable Information) & PD (Personal Data)
This is a module for handling personal data
Learning about PII, nonPII and Personal Data
"""
import logging
import mysql.connector
import re
from os import environ as env
from typing import List


# These are PII fields listed to be obfuscated
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
                 fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """This is a function that obfuscate sensitive or personal data
    This is a function that gets personal data of users and obfuscate
    sensitive ones and return a string with obfuscated personal data.

    Args:
        fields (List[str]): A list of strings holding the different fields
        redaction (str): The text/character to redact and obfuscate data
        message (str): The message to filter
        separator (str): The separator to separate fields

    Returns:
        (str): A string with the obfuscated data
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """This is a function that get records and logged a Logger object with
    logging level set to INFO and formatting the log with RedactingFormatter

    Returns:
         logging.Logger object with PII fields obfuscated
    """
    # Setting the logger to get records from user_data.csv file
    # Sets the logger level to log only INFO
    user_data_log = logging.getLogger('user_data')
    user_data_log.setLevel(logging.INFO)
    user_data_log.propagate = False

    # Set logger to log to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    user_data_log.addHandler(stream_handler)

    return user_data_log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    This is a function to establish a connection with a MySQL Database

    Returns:
        MySQLConnection object
    """
    db_host = env.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = env.get('PERSONAL_DATA_DB_NAME')
    db_user = env.get('PERSONAL_DATA_DB_USERNAME', 'root')
    db_pass = env.get('PERSONAL_DATA_DB_PASSWORD', '')

    db_con = mysql.connector.connection.MySQLConnection(host=db_host,
                                                        user=db_user,
                                                        password=db_pass,
                                                        database=db_name)
    return db_con


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Class Constructor
        This is the Initializer for the RedactingFormatter class

        Args:
            fields (List[str]): A list of string specifying the fields to
                                Obfuscate in log file
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        This is a method that formats an incoming log record

        Args:
            record (List[str]): A list of string

        Returns:
            (str): string of formatted log record
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(),
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def main():
    """This is a function that acts as a program runner.
    This is a function that does not take an argument nor returns a value.
    It retrieves data from the MySQL database and logs to the console.
    """
    db_con = get_db()
    cursor = db_con.cursor()
    query = "SELECT * FROM `users`;"
    cursor.execute(query)
    # fields = []
    # for field in cursor.description:
    #     fields.append(field[0])
    fields = [field[0] for field in cursor.description]

    user_logger = get_logger()

    for itm_row in cursor:
        row = ''.join(f'{f}={str(idx)}; ' for idx, f in zip(itm_row, fields))
        user_logger.info(row.strip())

    cursor.close()
    db_con.close()


if __name__ == '__main__':
    main()
