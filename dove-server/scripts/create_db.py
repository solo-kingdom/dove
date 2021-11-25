# coding: utf-8
# create database

import pymysql

from conf.config import *

cfg = database()
assert cfg[K_ENGINE] == V_MYSQL_ENGINE, 'unsupported engine. [engine=%s]' % cfg[K_ENGINE]
conn = pymysql.connect(host=cfg[K_HOST], user=cfg[K_USER], password=cfg[K_PASSWORD])
db = cfg[K_DB_NAME]
cursor = conn.cursor()
cursor.execute('SHOW DATABASES')
databases = [i[0] for i in cursor.fetchall()]
if db in databases:
    logging.info('databased is exists, skip creating operation. [database=%s]' % db)
else:
    cursor.execute('CREATE SCHEMA `dove` DEFAULT CHARACTER SET utf8mb4')
    logging.info('create database. [database=%s]' % db)
conn.close()
