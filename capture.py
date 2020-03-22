'''
docstring
This program captures the screenshots based on the time given by the user
input -> file path,start time, sleep_time
output -> Images
Author -> Sairam Subramaniam C
'''
import pyautogui
import time
import os

file_path = input('Enter the File path in which you need to store: ')
file_name = input('Enter the model file names: ')
print('Enter the run time in minutes')
minutes = int(input("Run Time: "))
time_end = time.time() + 60 * minutes  
print("Enter the sleep time in Seconds!") 
time_sleep = int(input("Enter the sleep time: "))
file_path.replace("\\","/")

start = True

while time.time() < time_end:
	if start:
		x = 1
	pyautogui.screenshot(file_path+file_name+'_'+str(x)+'.png')
	x += 1
	time.sleep(2)
	start = False

print('Amuku dumuku damal damal')
