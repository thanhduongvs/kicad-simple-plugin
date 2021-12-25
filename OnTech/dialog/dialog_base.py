# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class DialogBase
###########################################################################

class DialogBase(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__ (
            self, parent, id = wx.ID_ANY, title = u"OnTech",
            pos = wx.DefaultPosition, size = wx.Size(320, 320),
            style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP|wx.BORDER_DEFAULT
        )

        sizerMain = wx.BoxSizer(wx.VERTICAL)

        self.labelName = wx.StaticText(self, wx.ID_ANY, u"Board Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelName.Wrap(-1)

        sizerMain.Add(self.labelName, 0, wx.ALL, 8)

        self.textInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sizerMain.Add(self.textInput, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 8)

        self.buttonShow = wx.Button(self, wx.ID_ANY, u"Shown", wx.DefaultPosition, wx.DefaultSize, 0)
        sizerMain.Add(self.buttonShow, 0, wx.ALL, 8)

        self.labelStatus = wx.StaticText(self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0)
        self.labelStatus.Wrap(-1)

        sizerMain.Add(self.labelStatus, 0, wx.ALL, 8)

        self.SetSizer(sizerMain)
        self.Layout()

        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)
        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_INIT_DIALOG, self.OnInitDialog)
        self.buttonShow.Bind(wx.EVT_BUTTON, self.OnShowClick)

    def __del__(self):
        pass

    def SetSizeHints(self, a, b, c=None):
        if c is not None:
            super(wx.Dialog, self).SetSizeHints(a,b,c)
        else:
            super(wx.Dialog, self).SetSizeHintsSz(a,b)

    # Virtual event handlers, override them in your derived class
    def OnInitDialog(self, event):
        event.Skip()

    def OnShowClick(self, event):
        event.Skip()