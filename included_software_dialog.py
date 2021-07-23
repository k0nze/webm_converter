"""
Author: Konstantin (k0nze) Lübeck
License: BSD 3-Clause License
Copyright (c) 2021 Konstantin (k0nze) Lübeck
"""

try:
    import Tkinter as Tk
    from Tkinter import ttk
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import ttk

class IncludedSoftwareDialog(Tk.Toplevel):
    def __init__(self, master):
        Tk.Toplevel.__init__(self, master)

        self.minsize(180, 100)

        self.resizable(False, False)

        self.title("Included Software")

        wrapper_frame = ttk.Frame(self)

        # Version
        python_label = ttk.Label(wrapper_frame, text="Python 3.9.6 - PSF License")
        python_label.grid(row=0, column=0, columnspan=2)

        ffmpeg_label = ttk.Label(wrapper_frame, text="FFmpeg n4.4 - GPLv3 License")
        ffmpeg_label.grid(row=1, column=0, columnspan=2)

        pillow_label = ttk.Label(wrapper_frame, text="Pillow - HPND License")
        pillow_label.grid(row=2, column=0, columnspan=2)

        # Close button
        close_button = ttk.Button(wrapper_frame, text="Close", command=self.on_close).grid(row=3, column=0, columnspan=2, pady=10)

        wrapper_frame.grid(row=0, column=0, padx=10)

        #self.update()
        #print(self.winfo_height())
        #print(self.winfo_width())

    def on_close(self):
        self.destroy()


