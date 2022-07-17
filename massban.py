import pyautogui as tk
from time import sleep
import os

def timer():
	x = 10
	for i in range(10):
		print(x)
		sleep(1)
		x = x - 1


lines = open('config.txt', 'r')
l_1 = []
l_2 = []
l_3 = []
x = "a"
times = input("how many persons would you like to ban ? \n")
times = times.rstrip()
times = times.strip()
if times == "":
		print("you should put a number")
		sleep(3)
		exit()
else:
	try:
		times = int(times)
	except:
		print("you should put a number")
		sleep(3)
		exit()
for line in lines:
	line = line.replace("['","")
	line = line.replace(" '","")
	line = line.replace(")']","")
	line = line.replace("',",",")
	line = line.rstrip()
	if x == "a":
		l_1 = line

		x = "b"

	elif x == "b":
		l_2 = line
		x = "c"

	elif x == "c":
		l_3 = line


l_1 = l_1.split(",")
l_2 = l_2.split(",")
l_3 = l_3.split(",")
print("prepare yourself and open your discord server")
input("press enter when you're ready")
timer()

for i in range(times):
	sleep(0.2)
	tk.click(x=int(l_1[0]),y=int(l_1[1]),button="right")
	sleep(0.2)
	tk.click(x=int(l_2[0]),y=int(l_2[1]))
	sleep(0.2)
	tk.click(x=int(l_3[0]),y=int(l_3[1]))