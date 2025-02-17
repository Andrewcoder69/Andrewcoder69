from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.setBackgroundColor(0, 0, 0)  # Set background color to black

app = MyApp()
app.run()
