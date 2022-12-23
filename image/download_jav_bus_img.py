import json
import sys
import requests
import os
from bs4 import BeautifulSoup
import pymongo
import redis

r_path = 'L:\chromedown'

if __name__ == '__main__':
    for i in os.listdir(r_path):
        if str(i).startswith("Watch"):
            print(i)
