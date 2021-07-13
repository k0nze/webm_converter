"""
Author: Konstantin (k0nze) Lübeck
Copyright (c) 2021 Konstantin (k0nze) Lübeck
"""

try:
    import Tkinter as Tk
    import Tkinter.font as TkFont
except ModuleNotFoundError:
    import tkinter as Tk
    import tkinter.font as TkFont

from PIL import ImageTk, Image
from consts import *

import webbrowser

class AboutDialog(Tk.Toplevel):
    def __init__(self, master):
        Tk.Toplevel.__init__(self, master)

        self.minsize(309, 400)
        self.resizable(False, False)

        self.title("About " + NAME)

        wrapper_frame = Tk.Frame(self)

        # Logo
        logo = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "/logo_120x120.png"))
        logo_label = Tk.Label(wrapper_frame)
        logo_label.image = logo
        logo_label.configure(image=logo)
        logo_label.grid(row=0, column=0, columnspan=2, pady=15)
      
        # Name
        name_font_style = TkFont.Font(family="TkDefaultFont", size=12)
        name_label = Tk.Label(wrapper_frame, text=NAME, font=name_font_style)
        name_label.grid(row=1, column=0, columnspan=2)

        # Version
        version_label = Tk.Label(wrapper_frame, text="Version: " + VERSION)
        version_label.grid(row=2, column=0, columnspan=2)

        # Created by
        konze_frame = Tk.Frame(wrapper_frame) 

        k_logo = ImageTk.PhotoImage(Image.open(IMAGES_DIR + "/k_logo_30x30.png"))
        k_logo_label = Tk.Label(konze_frame)
        k_logo_label.image = k_logo
        k_logo_label.configure(image=k_logo, cursor="hand2")
        k_logo_label.bind("<Button-1>", lambda e: self.open_browser("https://linktree.k0nze.gg"))
        k_logo_label.pack(side=Tk.LEFT)

        konze_name_label = Tk.Label(konze_frame, text="Created by Konstantin (Konze) Lübeck", cursor="hand2")
        konze_name_label.bind("<Button-1>", lambda e: self.open_browser("https://linktree.k0nze.gg"))
        konze_name_label.pack(side=Tk.RIGHT)

        konze_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # Links  
        # Discord
        patreon_label = Tk.Label(wrapper_frame, text="Patreon:")
        patreon_label.grid(row=5, column=0, columnspan=1, sticky=Tk.W)

        patreon_link_label = Tk.Label(wrapper_frame, text="https://patreon.com/k0nze", fg="blue", cursor="hand2")
        patreon_link_label.grid(row=5, column=1, columnspan=1, sticky=Tk.W)
        patreon_link_label.bind("<Button-1>", lambda e: self.open_browser("https://patreon.com/k0nze"))

        # Twitch
        twitch_label = Tk.Label(wrapper_frame, text="Twitch:")
        twitch_label.grid(row=6, column=0, columnspan=1, sticky=Tk.W)

        twitch_link_label = Tk.Label(wrapper_frame, text="https://twitch.tv/k0nze", fg="blue", cursor="hand2")
        twitch_link_label.grid(row=6, column=1, columnspan=1, sticky=Tk.W)
        twitch_link_label.bind("<Button-1>", lambda e: self.open_browser("https://twitch.tv/k0nze"))

        # Youtube
        youtube_label = Tk.Label(wrapper_frame, text="Youtube:")
        youtube_label.grid(row=7, column=0, columnspan=1, sticky=Tk.W)

        youtube_link_label = Tk.Label(wrapper_frame, text="https://youtube.com/k0nze", fg="blue", cursor="hand2")
        youtube_link_label.grid(row=7, column=1, columnspan=1, sticky=Tk.W)
        youtube_link_label.bind("<Button-1>", lambda e: self.open_browser("https://youtube.com/k0nze"))

        # Twitter
        twitter_label = Tk.Label(wrapper_frame, text="Twitter:")
        twitter_label.grid(row=8, column=0, columnspan=1, sticky=Tk.W)

        twitter_link_label = Tk.Label(wrapper_frame, text="https://twitter.com/k0nze_gg", fg="blue", cursor="hand2")
        twitter_link_label.grid(row=8, column=1, columnspan=1, sticky=Tk.W)
        twitter_link_label.bind("<Button-1>", lambda e: self.open_browser("https://twitter.com/k0nze_gg"))

        # TikTok
        tiktok_label = Tk.Label(wrapper_frame, text="TikTok:")
        tiktok_label.grid(row=9, column=0, columnspan=1, sticky=Tk.W)

        tiktok_link_label = Tk.Label(wrapper_frame, text="https://tiktok.com/@k0nze.gg", fg="blue", cursor="hand2")
        tiktok_link_label.grid(row=9, column=1, columnspan=1, sticky=Tk.W)
        tiktok_link_label.bind("<Button-1>", lambda e: self.open_browser("https://tiktok.com/@k0nze.gg"))

        # Github 
        github_label = Tk.Label(wrapper_frame, text="GitHub:")
        github_label.grid(row=10, column=0, columnspan=1, sticky=Tk.W)

        github_link_label = Tk.Label(wrapper_frame, text="https://github.com/k0nze", fg="blue", cursor="hand2")
        github_link_label.grid(row=10, column=1, columnspan=1, sticky=Tk.W)
        github_link_label.bind("<Button-1>", lambda e: self.open_browser("https://github.com/k0nze/" + TODO))

        # Close button
        close_button = Tk.Button(wrapper_frame, text="Close", command=self.on_close).grid(row=11, column=0, columnspan=2, pady=10)

        wrapper_frame.grid(row=0, column=0, padx=10)

        #self.update()
        #print(self.winfo_height())
        #print(self.winfo_width())

    def open_browser(self, url):
        webbrowser.open_new(url)

    def on_close(self):
        self.destroy()


