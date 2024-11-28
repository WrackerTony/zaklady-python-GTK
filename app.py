import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

from win import Win

class Aplikace(Adw.Application):
    def __init__(self):
        super().__init__()
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        window = Win(app)
        window.present()