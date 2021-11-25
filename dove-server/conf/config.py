# coding: utf-8
import json
import logging
import os

DOVE_CONFIG_VAR = 'DOVE_CONFIG'

K_DB = 'database'
K_LOG = 'log'
K_DB_NAME = 'NAME'
K_HOST = 'HOST'
K_USER = 'USER'
K_PASSWORD = 'PASSWORD'
K_ENGINE = 'ENGINE'
V_MYSQL_ENGINE = 'django.db.backends.mysql'


def load(pt: str = 'asserts/config/config.json'):
    with open(pt, 'r') as f:
        return json.load(f)


def database():
    config_file = os.getenv(DOVE_CONFIG_VAR)
    assert config_file, 'environment variable not set. [variable_name=%s]' % DOVE_CONFIG_VAR
    cp = load(config_file)[K_DB]
    logging.info('database config loaded. [config=%s]' % cp)
    return cp


def log():
    config_file = os.getenv(DOVE_CONFIG_VAR)
    return load(config_file)[K_LOG]
