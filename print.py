#!/usr/bin/python

import time, sys, os
from epsonprinter import EpsonPrinter
from PIL import Image, ImageEnhance
from utils import is_grey_scale, brightness, init_printer
import functools

printer = init_printer(0x04b8, 0x0e15, 1)

printer.linefeed(2)
img = Image.open('images/test.png')
printer.print_image_from_file(img)

printer.linefeed(3)
printer.cut()
