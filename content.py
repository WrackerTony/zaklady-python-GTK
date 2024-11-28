import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class Content(Adw.Bin):
    def __init__(self):
        super().__init__()

       
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_child(main_box)
        main_box.set_vexpand(True)
        main_box.set_valign(Gtk.Align.CENTER)
        main_box.set_halign(Gtk.Align.CENTER)

        
        nested_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        main_box.append(nested_box)

       
        self.result_label = Gtk.Label(label="")
        self.result_label.set_markup("<b>Zde se ti zobrazi vysledek(asi)</b>")
        nested_box.append(self.result_label)

        
        self.text_field1 = Gtk.Entry()
        self.text_field1.set_placeholder_text("Zadej prvni cislo")
        nested_box.append(self.text_field1)

        
        self.combo_box = Gtk.ComboBoxText()
        self.combo_box.append_text("+")
        self.combo_box.append_text("-")
        self.combo_box.append_text("*")
        self.combo_box.append_text("/")
        self.combo_box.set_active(-1)  
        nested_box.append(self.combo_box)

        
        self.text_field2 = Gtk.Entry()
        self.text_field2.set_placeholder_text("Zadej druhe cislo")
        nested_box.append(self.text_field2)

        
        result_button = Gtk.Button(label="Vysledek")
        result_button.connect("clicked", self.on_button_clicked)
        nested_box.append(result_button)

    def on_button_clicked(self, result_button):
        
        operation = self.combo_box.get_active_text()

        
        try:
            cislo1 = float(self.text_field1.get_text())
            cislo2 = float(self.text_field2.get_text())
        except ValueError:
            self.result_label.set_text("Neplatne cislo")
            return

        
        if operation == "+":
            result = cislo1 + cislo2
        elif operation == "-":
            result = cislo1 - cislo2
        elif operation == "*":
            result = cislo1 * cislo2
        elif operation == "/":
            if cislo2 != 0:
                result = cislo1 / cislo2
            else:
                self.result_label.set_text("Error")
                return
        else:
            self.result_label.set_text("Vyberte operaci.")
            return

        
        self.result_label.set_text(f"Výsledek: {result}")


