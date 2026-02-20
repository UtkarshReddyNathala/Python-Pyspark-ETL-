"""
MySQL Connection Utility

Purpose:
Creates and returns a MySQL database connection.
Used across the project for read, write, and delete operations.
"""

import mysql.connector
from src.main.utility.logging_config import logger


def get_mysql_connection():
    """
    Establish and return a MySQL connection.

    Replace placeholder values with actual credentials
    in dev/qa/prod config files.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost"
            user="root"
            password="password"
            database="retail_sales_db"   
        )

        if connection.is_connected():
            logger.info("Connected to MySQL database successfully.")

        return connection

    except Exception as e:
        logger.error(f"Error connecting to MySQL: {str(e)}")
        raise e
