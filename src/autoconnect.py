import pyautogui as pyag
import time

pyag.hotkey('win','p')
WIDTH,HEIGHT = pyag.size()
print(WIDTH," ",HEIGHT);
pyag.moveTo(int(WIDTH*0.85),int(HEIGHT*0.58),0.2)
time.sleep(0.2)
pyag.click()
pyag.moveTo(int(WIDTH*0.85),int(HEIGHT*0.20))
time.sleep(3)
pyag.click()