# The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.
import os

class Config:
    ZIP_CODE_API_KEY = os.environ.get('ZIP_CODE_API_KEY')
