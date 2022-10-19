try:
  import os
  from tkinter import Scale
  import pyqrcode
  import png
  from pyqrcode import QRCode
  import sys
  import time
except:
  os.system('pip install pyqrcode')
  os.system('pip install QRCode')


def maneno(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.2)

usr = input("Enter Your Url Link To convert: ")

hili = pyqrcode.create(usr)

hapa = hili.png("Code.png", scale = 9)

maneno("Operation Succesfull!!!")