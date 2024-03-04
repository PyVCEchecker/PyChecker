import wx


class PromptingComboBox(wx.ComboBox):
    def __init__(self, parent, value, choices=[], style=0, **par):
        wx.ComboBox.__init__(self, parent, wx.ID_ANY, value, style=style | wx.CB_DROPDOWN,
                             choices=choices, **par)
        self.choices = choices
        self.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox)
        self.ignoreEvtText = False

    def EvtCombobox(self, event):
        self.ignoreEvtText = True
        event.Skip()

    def EvtChar(self, event):
        if event.GetKeyCode() == 8:
            self.ignoreEvtText = True
        event.Skip()

    def EvtText(self, event):
        if self.ignoreEvtText:
            self.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.choices:
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetMark(len(currentText), len(choice))
                found = True
                break
        if not found:
            event.Skip()


class TrialPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        choices = ['grandmother', 'grandfather', 'cousin', 'aunt', 'uncle', 'grandson',
                   'granddaughter']
        for relative in ['mother', 'father', 'sister', 'brother', 'daughter', 'son']:
            choices.extend(self.derivedRelatives(relative))

        cb = PromptingComboBox(self, "default value", choices, style=wx.CB_SORT)

    def derivedRelatives(self, relative):
        return [relative, 'step' + relative, relative + '-in-law']


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, -1, 'Demo PromptingComboBox Control', size=(400, 50))
    TrialPanel(frame)
    frame.Show()
    app.MainLoop()