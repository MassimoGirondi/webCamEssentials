import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from mainwindow import *
from webcamHandler import *

d = dialogWindow()
d.connect("destroy", Gtk.main_quit)
d.show_all()
Gtk.main()

