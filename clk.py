from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
from datetime import datetime, timedelta


class Clk(plugins.Plugin):
    __author__ = 'https://github.com/renaudgweb'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'Example Clock for pwnagotchi'

    def on_loaded(self):
        logging.info("Clk Plugin loaded.")

    # called to setup the ui elements
    def on_ui_setup(self, ui):
        # add custom UI elements
        ui.add_element('clk', LabeledValue(color=BLACK, label='', value='-/--:--', position=(175, 110), label_font=fonts.Small, text_font=fonts.Small))

    # called when the ui is updated
    def on_ui_update(self, ui):
        # update those elements
        time = datetime.now() + timedelta(hours=1)
        time_line = time.strftime("%d/%H:%M")
        ui.set('clk', time_line)
        