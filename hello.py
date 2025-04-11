import wx

class HelloFrame(wx.Frame):

    def __init__ (self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)

        pnl = wx.Panel(self)

        # Initialize UI (form and labels)
        self.InitUI(pnl)

        # Create a menu bar
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxpython. Ab ye saanp lega maze!!")

        self.SetSize((400, 350))
        self.Center()

    def InitUI(self, pnl):   
        # title text
        st = wx.StaticText(pnl, label="Hellooo Duniya!!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # form elements
        name_label = wx.StaticText(pnl, label = "Name: ")
        self.name_input = wx.TextCtrl(pnl)

        email_label = wx.StaticText(pnl, label = "Email: ")
        self.email_input = wx.TextCtrl(pnl)

        submit_btn = wx.Button(pnl, label = "Submit")
        submit_btn.Bind(wx.EVT_BUTTON, self.onSubmit)        

        # Layout boxsizer, along with form elements
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))

        # adding design in the name and email of the form
        sizer.Add(name_label, flag = wx.LEFT, border = 10)
        sizer.Add(self.name_input, flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)

        sizer.Add(email_label, flag = wx.LEFT, border = 10)
        sizer.Add(self.email_input, flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 10)

        sizer.Add(submit_btn, flag = wx.ALL|wx.ALIGN_CENTER, border = 10)

        pnl.SetSizer(sizer)

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.AppendSeparator()

        # creating a submenu under Import
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import bookmarks')
        imp.Append(wx.ID_ANY, 'Import favorites')
        imp.Append(wx.ID_ANY, 'Import data')
        fileMenu.AppendSubMenu(imp, 'I&mport')

        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl+H","Help string shown in the status bar for this menu item")
        fileMenu.AppendSeparator()

        exitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit \tCtrl+W')
        fileMenu.Append(exitItem)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def onSubmit(self, event):
        name = self.name_input.GetValue()
        email = self.email_input.GetValue()
        wx.MessageBox(f"Name: {name} \nEmail: {email}", "Form is submitted successfully!!")

    def OnExit(self, event):
        self.Close(True)

    def OnHello(self, event):
        wx.MessageBox("Waps aa gya hello bolne main hehe!!")

    def OnAbout(self, event):
        wx.MessageBox("This is your Captain speaking.")

if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Hello Rupert!')
    frm.Show()
    app.MainLoop()