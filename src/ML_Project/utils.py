import os
import sys
from src.ML_Project.exception import CustomException
from src.ML_Project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pyodbc

load_dotenv()

host = os.getenv('HOST')
db = os.getenv('DBNAME')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={host};'
            f'DATABASE={db};'
            f'Trusted_Connection=yes;'
        )
    
        logging.info("Connection established",mydb)
        df = pd.read_sql_query('Select * from Student',mydb)
        print(df.head())

        return df


    except Exception as e:
        raise CustomException(e)
