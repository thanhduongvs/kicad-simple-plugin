from dialog.dialog_main import *
from ontech.ontech import OnTech

import wx

class MyApp(wx.App):
    def OnInit(self):

        #config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
        #config = FileConfig(localFilename=config_file)

        #print(config_file)
        self.frame = frame = DialogMain(None, OnTech(None))
        if frame.ShowModal() == wx.ID_OK:
            print("Graceful Exit")
        frame.Destroy()
        return True

app = MyApp()
app.MainLoop()

print("Done")
