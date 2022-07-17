import pyautogui as tk
from time import sleep
import os







def timer():
	x = 2
	for i in range(5):
		print(x)
		sleep(1)
		x = x - 1
print("open the discord server that you want to massban")
sleep(3)

print("you have to put your mouse in the current position")
sleep(2)
os.startfile("references\\right_click.png")
input("press enter when you're ready")
timer()

a = str(tk.position())
a = a.replace("Point(","")
a = a.replace(" y=","")
a = a.replace("x=","")
a = a.split(",")

print("now here")
sleep(2)
os.startfile("references\\left_click.png")
input("press enter when you're ready")
timer()

b = str(tk.position())
b = b.replace("Point(","")
b = b.replace(" y=","")
b = b.replace("x=","")
b = b.split(",")

print("you have to put your mouse in the current position")
sleep(2)
os.startfile("references\\confirm.png")
input("press enter when you're ready")
timer()
c = str(tk.position())
c = c.replace("Point(","")
c = c.replace(" y=","")
c = c.replace("x=","")
c = c.split(",")



try:
	os.remove("config.txt")
	f = open('config.txt', "a")
	f.writelines(f"{a} \n")
	f.writelines(f"{b} \n")
	f.writelines(f"{c} \n")
except:
	f = open('config.txt', "a")
	f.writelines(f"{a} \n")
	f.writelines(f"{b} \n")
	f.writelines(f"{c} \n")