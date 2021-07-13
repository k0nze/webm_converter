"""
Author: Konstantin (k0nze) Lübeck
Copyright (c) 2021 Konstantin (k0nze) Lübeck
"""

try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk

from pathlib import Path
from consts import *

from view import View
from model import Model


class Controller:
    def __init__(self):
        user_dir = Path.home()
        data_path = Path.joinpath(user_dir, '.' + FILE_NAME)

        self.model = Model(data_path)

        self.root = Tk.Tk()
        self.view = View(self.model, self)

    def run(self):
        self.root.title(NAME)
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.quit()
