"""
Eric Zorn Module 7 Week 7 - 2/5/18 - Connecting and Using SQLite Databases
"""
# Database Connection
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Creates a connection to SQLite3 Database (Not MySQL)
    :param db_file: file to connect
    :return: none
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_db_table(conn, create_table_sql):
    """
    Creates a table from the SQL Statement
    :param conn: The database connection
    :param create_table: SQL create table statement
    :return: None
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_db_data(conn, query):
    """
    This function accepts a database and a query which will inser the data into one of the three database tables
    :param conn: Database Connection
    :param query: Query String of SQLite Code
    :return: None
    """
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

    return None


