import os
from datetime import datetime

import pcbnew
from ..core import core

class SimplePlugin(pcbnew.ActionPlugin, object):

    def __init__(self):
        super(SimplePlugin, self).__init__()
        self.name = "Simple Plugin"
        self.category = "Read PCB"
        self.pcbnew_icon_support = hasattr(self, "show_toolbar_button")
        self.show_toolbar_button = True
        icon_dir = os.path.dirname(os.path.dirname(__file__))
        self.icon_file_name = os.path.join(icon_dir, 'icon.png')
        self.description = "Simple Plugin"

    def defaults(self):
        pass

    def Run(self):
        board = pcbnew.GetBoard()
        pcb_file_name = board.GetFileName()

        logger = core.Logger()
        if not pcb_file_name:
            logger.error('Please save the board file before generating Simple Plugin.')
            return

        try:
            core.run_with_dialog(logger)
        except ParsingException as e:
            logger.error(str(e))
