
import pyautogui
import time
timeset=pyautogui.prompt(text="enter the duration",title="meeting duration",default='')
meeting=pyautogui.prompt(text="enter the meeting id",title="meeting id",default='')
print(meeting)
pyautogui.press('win',interval=0.5)
pyautogui.write('microsoft edge',interval=0.5)
pyautogui.press('enter',interval=0.5)
pyautogui.write(meeting)
pyautogui.press('enter')

time.sleep(5)
pyautogui.hotkey('ctrl','d')
pyautogui.press('enter')
time.sleep(2)
#pyautogui.click(x=575,y=752)#to off the mic
pyautogui.hotkey('ctrl','e')
pyautogui.press('enter')
#pyautogui.click(x=679,y=759)#to off the cam

pyautogui.click(x=1321,y=565,interval=30)#to click join button
time.sleep(timeset)
pyautogui.click(x=1148,y=966,interval=0.5)#to close the meeting
pyautogui.click(x=1889,y=15)#to close the tab

