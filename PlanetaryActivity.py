
#gtk
from gi.repository import Gtk

#pygame
import pygame

#sugar
import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton


import Planetary


class PlanetaryActivity(sugar3.activity.activity.Activity):
    def __init__(self, handle):
        super(PlanetaryActivity, self).__init__(handle)

        # Create the game instance.
        self.game = Planetary.Planetary()

        # Build the activity toolbar.
        self.build_toolbar()


    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        # Blank space (separator) and Stop button at the end:

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

    def read_file(self, file_path):
        self.game.read_file(file_path)

    def write_file(self, file_path):
        self.game.write_file(file_path)
