
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
GPIO.setup(20, GPIO.OUT)

input = 1
os.system('fswebcam --set brightness=100% --set "Exposure"="Manual Mode" --set "Exposure (Absolute)"="100%" ')

while True:
	GPIO.output(20, 1)  
	input = GPIO.input(21)
	if (input == 0):
		GPIO.output(20, 0)
		printer.linefeed(3)

                now = str(int(time.time()*1000))


                os.system('fswebcam -r 500x500 --no-banner --rotate 180 images/archives/image1-'+now+'.jpg  ')
          	time.sleep(0.5)                
		os.system('fswebcam -r 500x500 --no-banner --rotate 180 images/archives/image2-'+now+'.jpg   ')
	        time.sleep(0.5)
                os.system('fswebcam -r 500x500 --no-banner --rotate 180 images/archives/image3-'+now+'.jpg   ')
        	time.sleep(0.5)
                os.system('fswebcam -r 500x500 --no-banner --rotate 180 images/archives/image4-'+now+'.jpg   ')
		
		logo = Image.open("images/logo.jpg")
		img1 = Image.open('images/archives/image1-' + now + '.jpg')
                img2 = Image.open('images/archives/image2-' + now + '.jpg')
                img3 = Image.open('images/archives/image3-' + now + '.jpg')
                img4 = Image.open('images/archives/image4-' + now + '.jpg')
		
                printer.print_image_from_file(logo)
                printer.linefeed(2)
		printer.print_image_from_file(img1)
                printer.linefeed(2)
                printer.print_image_from_file(img2)
                printer.linefeed(2)
                printer.print_image_from_file(img3)
                printer.linefeed(2)
                printer.print_image_from_file(img4)
		printer.linefeed(5)
		
		printer.cut()
		printer.linefeed(3)

		time.sleep(1)
		input = 1
	        print "Ready for capture"
