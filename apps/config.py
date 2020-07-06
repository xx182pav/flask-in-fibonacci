import os
from distutils.util import strtobool

HOST = str(os.environ.get('HOST', '127.0.0.1'))
PORT = int(os.environ.get('PORT', '5000'))
DEBUG = strtobool(os.environ.get('DEBUG', 'True'))
CACHE_DEFAULT_TIMEOUT = 300
