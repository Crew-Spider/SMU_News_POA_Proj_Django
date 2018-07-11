import requests
from bs4 import BeautifulSoup
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import get_database_dict_info
from crawler_news import *






if __name__ == '__main__':

    print("main crawler begins......")
    save_newslist_to_db()