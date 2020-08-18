import pyautogui
import re
from PIL import Image, ImageEnhance, ImageFilter
import time
import pytesseract
from os import system, name 


health = 100
last_time = time.time()

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def compFunc(helth):
    global health
    print(helth)
    if helth<health:
        health = helth
        print("Hit")
    else:
        health = helth
        clear()
        print(helth)
    



def loop():
    while(1):
        global last_time
        # print("loop took {} seconds" ,format(time.time()-last_time))
        # last_time=time.time()
        # time.sleep(1)
        im = pyautogui.screenshot("ss1.png",region=(577,1000,75,50))
        im = Image.open("ss1.png")
        thresh = 150

        im = im.convert('L')

        try:
            text = pytesseract.image_to_string(im,config= '--psm 11')
            text = x = re.findall('[0-9]+', text)
            compFunc(int(text[0]))
        except:
            print("Can't read any number")
            # break
if __name__ == '__main__':
    loop()