#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from console import HBNBCommand
import MySQLdb
import os
from models.engine.db_storage import DBStorage

os.environ["HBNB_MYSQL_USER"] = 'hbnb_test'
os.environ["HBNB_MYSQL_PWD"] = 'hbnb_test_pwd'
os.environ["HBNB_MYSQL_HOST"] = 'localhost'
os.environ["HBNB_MYSQL_DB"] = 'hbnb_test_db'
os.environ["HBNB_TYPE_STORAGE"] = 'db'
os.environ["HBNB_ENV"] = 'test'

storage = DBStorage()
storage.reload()

db = MySQLdb.connect(
    host="localhost",
    user="hbnb_test",
    port=3306,
    password="hbnb_test_pwd",
    database="hbnb_test_db"
)

c = db.cursor()

class test_dbStorage(unittest.TestCase):
    """Test the db storage"""

    def setUp(self):
        """ Set up test environment """
        pass

    def tearDown(self):
        """ Remove storage file at end of tests """
        pass
    
    def test_tables_exists(self):
        print(storage)
        state = State(name="California")
        c.execute("select * from states")
        for s in c.fetchall():
            print(s)
