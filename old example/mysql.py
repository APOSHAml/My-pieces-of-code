from time import sleep
import mysql.connector as mysql
import pytest
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from urllib import request, error
import json


db = mysql.connect(
        host='database-1.cqpxsublkhcn.eu-central-1.rds.amazonaws.com',
        port=3306,
        user='user1',
        passwd='1Passw0rd1',
        database='QAP-05'
    )

# cursor = db.cursor()
# cursor.execute('select * from students')
# print(cursor.fetchall())
# db.close()

cursor = db.cursor(dictionary=True)
cursor.execute('select * from students')
# print(cursor.fetchall())
result = cursor.fetchone()
print(['name'])



# query = 'insert into students (name, surname) values (%s, %s)'
# values = [
#     ('Vasia', 'Pupkin'),
#     ('Sania', 'Popkin')
#     ]
# cursor.execute(query, values)
# db.commit()

# cursor = db.cursor(dictionary=True)
# query1 = '''Select *
# From students
# Where name = "George"
# and surname'''
# cursor.execute(query1)
