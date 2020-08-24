import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from webcamHandler import *

class dialogWindow(Gtk.Dialog):
    # TODO: make this a parameter!
    dev = "/dev/video2"

    def __init__(self):
        Gtk.Dialog.__init__(self)
        self.set_default_size(400, 100)

        self.exp_limits = get_limits(self.dev, "exposure_absolute")

        self.adj = Gtk.Adjustment(0, self.exp_limits[0], self.exp_limits[1], 5, 10, 0)
        self.exp = Gtk.HScale(adjustment=self.adj)
        self.exp.set_digits(1)
        self.exp.set_draw_value(True)
        self.exp.connect("value-changed", self.set_exposure)

        self.exp_check = Gtk.CheckButton(self, label= "Manual exposure")
        self.exp_check.connect("toggled", self.manual_exposure)

        contentArea = Gtk.Dialog.get_content_area(self)
        contentArea.add(self.exp_check)
        contentArea.add(self.exp)

    def manual_exposure(self, btn):
        self.exp.set_sensitive(btn.get_active())
        if btn.get_active():
            set_property(self.dev, "exposure_auto", 1)
        else:
            set_property(self.dev, "exposure_auto", 3)
    def set_exposure(self, scale):
        set_property(self.dev, "exposure_absolute", min(self.exp_limits[1], max(self.exp_limits[0], scale.get_value())))

