from pymongo import MongoClient
import sys, os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
from config.database import get_database_dict_info

def get_connected_database():
    db_config = get_database_dict_info()
    connection = MongoClient(db_config['host'], db_config['port'])
    database = connection[db_config['database']]
    if (db_config['host'] != '127.0.0.1' and db_config['host'] != 'localhost'):
        database.authenticate(db_config['user'], db_config['password'])
    return database
