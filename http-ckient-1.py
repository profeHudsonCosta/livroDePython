""" import urllib.request

emByte = urllib.request.urlopen("https://www.python.org").read()
emString = emByte.decode('utf-8')
print(emString) """

import mysql