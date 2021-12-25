import wx
import wx.grid

from . import dialog_base

class DialogMain(dialog_base.DialogBase):
    def __init__(self, parent, data):
        dialog_base.DialogBase.__init__(self, parent)
        self.SetTitle('OnTech v1.0')
        self.board = data.board
    
    def SetSizeHints(self, a, b, c=None):
        if c is not None:
            super(wx.Dialog, self).SetSizeHints(a,b,c)
        else:
            super(wx.Dialog, self).SetSizeHintsSz(a,b)

    def OnInitDialog(self, event):
        file_name = str(self.board.GetFileName())
        index = file_name.rfind('/')
        name = file_name[index+1:]
        self.labelName.LabelText = name 

    def OnShowClick(self, event):
        txt = self.textInput.GetValue()
        if txt == '':
            self.labelStatus.LabelText = 'Please input text'
        else:
            self.labelStatus.LabelText = txt

