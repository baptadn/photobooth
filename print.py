#!/usr/bin/python

import time, sys, os
from epsonprinter import EpsonPrinter
from PIL import Image, ImageEnhance
from utils import is_grey_scale, brightness, init_printer
import functools
import RPi.GPIO as GPIO
import time

printer = init_printer(0x04b8, 0x0e15, 1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)
input = 0
while True:
	input = GPIO.input(21)
	if (input == 0):
		printer.linefeed(2)
		os.system('fswebcam --set brightness=100% --set "Exposure"="Manual Mode" --set "Exposure (Absolute)"="100%" ')
                os.system('fswebcam -r 500x500 --no-banner cheese.jpg  ')

		img = Image.open('cheese.jpg')
		enhancer = ImageEnhance.Brightness(img)
		enhancer.enhance(0.9).save("cheese2", "JPEG")



		printer.print_image_from_file(img)	
		printer.linefeed(3)
		printer.cut()
		if (brightness(img) > 0):
                        now = str(int(time.time()))
			img.save("images/image-"+now, "JPEG")
		print brightness(img)
		print "wait"
		time.sleep(1)
		input = 1
		print "go"
