import sqlite3

def get_connection(db_path="files.db"):
    return sqlite3.connect(db_path)