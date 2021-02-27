# The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.
import os
from dotenv import load_dotenv

class Config:
    load_dotenv()
    ZIPCODE_API_KEY = os.environ.get('ZIPCODE_API_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True 
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False 
    TESTING = False 

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
