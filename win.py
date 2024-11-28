import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

from content import Content

class Win(Adw.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application = app, title = "Zaklady")
        self.set_default_size(600,400)
        
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.set_content(box)
        
        
        header = Adw.HeaderBar()
        box.append(header)
        
        
        content = Content()
        box.append(content)