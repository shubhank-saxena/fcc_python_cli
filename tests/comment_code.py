import sys
import os

cwd = os.getcwd()
file_location = cwd+'/'+sys.argv[1]

from . import file_location
print("Hello World")