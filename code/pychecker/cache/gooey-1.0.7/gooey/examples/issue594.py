import wx
from gooey import Gooey, GooeyParser

# @Gooey
# def main():
#     parser = GooeyParser(description="Gooey example")
#     parser.add_argument("-a", "--myargument",
#     #                     choices=['one', 'two', 'three'], gooey_options={
#     #                     'label_color': (255, 100, 100)
#     # }
#                         )
#     args = parser.parse_args()
#     print(args)
#     print(args.myargument)
#     print(type(args.myargument))
#
#
# if __name__=="__main__":
#     main()

import wx

class PromptingComboBox(wx.ComboBox) :
    def __init__(self, parent, choices=[], style=0, **par):
        wx.ComboBox.__init__(self, parent, wx.ID_ANY, style=style|wx.CB_DROPDOWN, choices=choices, **par)
        self.choices = choices
        self.Bind(wx.EVT_TEXT, self.OnText)
        self.Bind(wx.EVT_KEY_DOWN, self.OnPress)
        self.ignoreEvtText = False
        self.deleteKey = False

    def OnPress(self, event):
        if event.GetKeyCode() == 8:
            self.deleteKey = True
        event.Skip()

    def OnText(self, event):
        currentText = event.GetString()
        if self.ignoreEvtText:
            self.ignoreEvtText = False
            return
        if self.deleteKey:
            self.deleteKey = False
            if self.preFound:
                currentText =  currentText[:-1]

        self.preFound = False
        for choice in self.choices :
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetTextSelection(len(currentText), len(choice))
                self.preFound = True
                break

class TrialPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        choices = ['grandmother', 'grandfather', 'cousin', 'aunt', 'uncle', 'grandson', 'granddaughter']
        for relative in ['mother', 'father', 'sister', 'brother', 'daughter', 'son']:
            choices.extend(self.derivedRelatives(relative))
        self.choices = choices = sorted(choices)

        mainSizer = wx.FlexGridSizer(2, 2, 5, 10)
        self.SetSizer(mainSizer)

        mainSizer.Add(wx.StaticText(
            self, -1, "Worked in Mac - python 3 - wx phoenix"))
        cb1 = PromptingComboBox(self, choices=choices)
        mainSizer.Add(cb1)

        mainSizer.Add(wx.StaticText(self, -1, "Work arround in Linux-gtk"))
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(sizer2)
        filterCtrl = wx.TextCtrl(self, -1, size=(150, -1))
        filterCtrl.Bind(wx.EVT_TEXT, self.OnFilter)
        sizer2.Add(filterCtrl)
        self.cb2 = wx.ComboBox(self, -1, size=(150, -1), choices=choices)
        sizer2.Add(self.cb2)


    def derivedRelatives(self, relative):
        return [relative, 'step' + relative, relative + '-in-law']

    def OnFilter(self, event):
        currentText = event.GetString().upper()
        tmpChoices = [c for c in self.choices if c.startswith(currentText)]
        if tmpChoices != []:
            self.cb2.SetItems(tmpChoices)
            self.cb2.SetValue(tmpChoices[0])
        else:
            self.cb2.SetValue('')
            self.cb2.SetItems([])

if __name__ == '__main__':
    app = wx.App(False)
    frame = wx.Frame (None, -1, 'Demo PromptingComboBox Control and Work around',
                      size=(700, 400))
    TrialPanel(frame)
    frame.Show()
    app.MainLoop()