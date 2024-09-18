from tkinter import Tk


class Window(Tk):
    """
    A black, full-screen window that is always on the top
    """

    def __init__(self, x, y, close_key):
        Tk.__init__(self)

        self.geometry("+%i+%i" % (x, y))
        self.update()
        self.state('zoomed')
        self.overrideredirect(True)
        self.attributes("-topmost", 1)

        self.config(bg="black", cursor="none")
        self.title("Screen Burn Stopper")

        self.bind("<Key-" + close_key + ">", lambda e: self.destroy())
        self.bind("<Key>", lambda e: self.hide(), add="+")
        self.bind("<Button>", lambda e: self.hide())
        self.bind("<Motion>", lambda e: self.hide())
        self.protocol("WM_DELETE_WINDOW", lambda: self.hide())

        self.hide()

    def hide(self):
        """Hides this window"""

        self.withdraw()

    def show(self):
        """Shows this window"""

        self.deiconify()
        self.focus_force()
