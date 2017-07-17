#!/usr/bin/python

import time, sys, os
from epsonprinter import EpsonPrinter
from PIL import Image, ImageEnhance
from utils import is_grey_scale, brightness, init_printer
import functools
from escpos.printer import Usb

BASE_WIDTH = 512

p = Usb(0x04b8, 0x0e15)
p.text("lol");

printer = init_printer(0x04b8, 0x0e15, 1)

printer.linefeed(2)
img = Image.open('DSC_0043.JPG')
 wpercent = (BASE_WIDTH / float(img.size[0]))
 hsize = int((float(img.size[1]) * float(wpercent)))
 img = img.resize((BASE_WIDTH, hsize), PIL.Image.ANTIALIAS)
printer.print_image_from_file(img)

printer.linefeed(3)
printer.cut()
