import wx
import warnings

wx.Log.SetLogLevel(wx.LOG_Debug)

app = wx.App()

frame = wx.Frame(None, title='Simple application')
sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(wx.StaticText(frame, -1, "foo"), 1, wx.ALIGN_CENTER_HORIZONTAL)

frame.Show()
app.MainLoop()