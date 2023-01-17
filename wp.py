import pywhatkit
import pyautogui
import time

from datetime import datetime

contatos = ['+351',]

while len(contatos) >= 1:

       pywhatkit.sendwhatmsg(contatos[0], '/oi', datetime.now().hour,datetime.now(). minute + 2)

pyautogui.press('ctrl', 'w')
del contatos [0]
time.sleep (35)
