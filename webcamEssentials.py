#!/bin/env python3
import gi
import argparse
from webcamHandler import *
import sys

# Set as your usual webcam device
default_dev="/dev/video2"

parser = argparse.ArgumentParser(description="Essential webcam control interfaces")
parser.add_argument("-d", default=default_dev, help="Video Device to control", dest="device", action="store")
parser.add_argument("-l", default=False, help="List all video devices", dest="list", action="store_true")



args = parser.parse_args()
if args.list:
    print("List of devices on the system:")
    for d in get_devs():
        print(d, get_name(d))
    sys.exit(0)
else:
    dev = args.device

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from mainwindow import *
from webcamHandler import *

d = dialogWindow(dev)
d.connect("destroy", Gtk.main_quit)
d.show_all()
Gtk.main()

