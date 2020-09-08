import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from webcamHandler import *

class dialogWindow(Gtk.Dialog):

    def __init__(self, dev):
        self.dev = dev
        Gtk.Dialog.__init__(self)
        self.connect("key-press-event",self.on_key)
        self.set_default_size(400, 100)

        self.exp_limits = get_limits(self.dev, "exposure_absolute")

        self.adj = Gtk.Adjustment(0, self.exp_limits[0], self.exp_limits[1], 5, 10, 0)
        self.exp = Gtk.HScale(adjustment=self.adj)
        self.exp.set_digits(1)
        self.exp.set_draw_value(True)
        self.exp.connect("value-changed", self.set_exposure)

        self.exp_check = Gtk.CheckButton(self, label= "Manual exposure")
        self.exp_check.connect("toggled", self.manual_exposure)

        self.expand = Gtk.CheckButton(self, label= "Advanced")
        self.expand.connect("toggled", self.toggle_advanced)
        self.expand.set_active(True)

        self.contentArea = Gtk.Dialog.get_content_area(self)

        self.box = Gtk.Box(spacing=6)
        self.contentArea.add(self.box)
        self.box.pack_start(self.exp_check, False, True, 0)
        self.box.pack_start(self.exp, True, True, 0)
        self.box.pack_end(self.expand, False, True, 0)


        
        self.brightness = Gtk.HScale(adjustment=Gtk.Adjustment( int(get_property(self.dev, "brightness")), 1, 255, 5, 10, 0))
        self.brightness.set_digits(1)
        self.brightness.set_draw_value(True)
        self.brightness.connect("value-changed", self.set_brightness)

        self.contrast = Gtk.HScale(adjustment=Gtk.Adjustment( int(get_property(self.dev, "contrast")), 1, 255, 5, 10, 0))
        self.contrast.set_digits(1)
        self.contrast.set_draw_value(True)
        self.contrast.connect("value-changed", self.set_contrast)
        self.contrast.set_hexpand(True)

        brightness_lbl= Gtk.Label("Brightness")
        contrast_lbl= Gtk.Label("Contrast")


        self.advanced = Gtk.Grid()
        self.advanced.attach_next_to(brightness_lbl, None, Gtk.PositionType.RIGHT, 1, 1)
        self.advanced.attach_next_to(self.brightness, brightness_lbl, Gtk.PositionType.RIGHT, 1, 1)

        self.advanced.attach_next_to(contrast_lbl, None, Gtk.PositionType.BOTTOM, 1, 1)
        self.advanced.attach_next_to(self.contrast, contrast_lbl, Gtk.PositionType.RIGHT, 1, 1)
       
        
        self.contentArea.add(self.advanced)

    def manual_exposure(self, btn):
        self.exp.set_sensitive(btn.get_active())
        if btn.get_active():
            set_property(self.dev, "exposure_auto", 1)
        else:
            set_property(self.dev, "exposure_auto", 3)
    def set_exposure(self, scale):
        set_property(self.dev, "exposure_absolute", min(self.exp_limits[1], max(self.exp_limits[0], scale.get_value())))

    def set_brightness(self, scale):
        set_property(self.dev, "brightness", scale.get_value())

    def set_contrast(self, scale):
        set_property(self.dev, "exposure_absolute", scale.get_value())
    
    def toggle_advanced(self, btn):
        # TODO: RESIZE
        if btn.get_active():
            self.advanced.show()
        else:
            self.advanced.hide()
            w,h = self.get_default_size()
            w,_ = self.get_size()
            #h-=self.advanced.height
            h-=60
            self.resize(w,h)

    def on_key(self, u, e):
        # Ignore ESC button
        return e.keyval == Gdk.KEY_Escape
