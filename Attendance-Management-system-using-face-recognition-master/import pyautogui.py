from urllib.request import HTTPBasicAuthHandler
import pyautogui as spam
import time
limit =int(input("Enter your limit:"))
msg=input("enter the msg:")
i=0
time.sleep(10)
while i<limit:
    spam.typewrite(msg)
    spam.press('Enter')
i=i+1
