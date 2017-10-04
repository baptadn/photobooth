#!/usr/bin/python

import time, sys, os, subprocess, logging, datetime
from epsonprinter import EpsonPrinter
from PIL import Image, ImageEnhance
from utils import is_grey_scale, brightness, init_printer
import functools
from escpos.printer import Usb
import gphoto2 as gp
from stat import S_ISREG, ST_CTIME, ST_MODE


BASE_WIDTH = 512

p = Usb(0x04b8, 0x0e15)
printer = init_printer(0x04b8, 0x0e15, 1)

context = gp.gp_context_new()
camera = gp.check_result(gp.gp_camera_new())
gp.check_result(gp.gp_camera_init(camera, context))

printer.linefeed(3)
printer.cut()

def take_photo(dateDirectory, index):
  if not os.path.exists('./files/' + dateDirectory):
    os.makedirs('./files/' + dateDirectory)

  file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE, context))
  filePathName = index + '_' + dateDirectory + file_path.name

  target = os.path.join('./files/' + dateDirectory + '/', filePathName)
  camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL, context))
  gp.check_result(gp.gp_file_save(camera_file, target))

while True:
  raw_input("Hit keys for starting the photobooth")

  dateDirectory = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  imgTitle = Image.open('/home/pi/photobooth/title.png')
  printer.print_image_from_file(imgTitle)
  printer.linefeed(1)

  take_photo(dateDirectory, '1')
  take_photo(dateDirectory, '2')
  take_photo(dateDirectory, '3')
  take_photo(dateDirectory, '4')


  dirpath = "./files/" + dateDirectory

  entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
  entries = ((os.stat(path), path) for path in entries)
  entries = ((stat[ST_CTIME], path)
  for stat, path in entries if S_ISREG(stat[ST_MODE]))
  i = 0

  for cdate, path in sorted(entries):
    picturePath = dirpath + '/' + os.path.basename(path)
    img = Image.open(picturePath)
    wpercent = (BASE_WIDTH / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((BASE_WIDTH, hsize), PIL.Image.ANTIALIAS)
    enhencer = ImageEnhance.Contrast(img)
    img = enhencer.enhance(3.0)
    printer.print_image_from_file(img)
    printer.linefeed(1)

  printer.linefeed(4)
  printer.cut()
