"""
Author: Konstantin (k0nze) Lübeck
Copyright (c) 2021 Konstantin (k0nze) Lübeck
"""

try:
    import Tkinter as Tk
    from Tkinter import messagebox
    from Tkinter.filedialog import askopenfilename, askdirectory
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import messagebox
    from tkinter.filedialog import askopenfilename, askdirectory


from tkinter.constants import DISABLED
from consts import *
from about_dialog import AboutDialog

import copy

class MainWindow(Tk.Frame):
    def __init__(self, model, root):

        self.model = model
        self.model.register_observer(self)

        self.root = root
        self.input_file_set = False
        self.output_directory_set = False

        #self.root.minsize(200, 300)

        Tk.Frame.__init__(self, self.root)

        self.pack(fill="both", expand=True)

        self.menubar = Tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        
        # file menu
        file_menu = Tk.Menu(self.menubar)
        file_menu.add_command(label="About", command=self.on_about)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        self.menubar.add_cascade(label="File", menu=file_menu)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.columnconfigure(0, weight=1)

        input_output_file_frame = Tk.Frame(self)
        input_output_file_frame.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=0, column=0, columnspan=3, padx=5, pady=5)

        input_output_file_frame.columnconfigure(1, weight=1)

        # input file label
        input_file_path_entry_label = Tk.Label(input_output_file_frame, text="Input File:")
        input_file_path_entry_label.grid(sticky=Tk.W, row=0, column=0, padx=10) 

        self.input_file_path_var = Tk.StringVar() 
        self.input_file_path_var.set("no file selected")
        input_file_path_entry = Tk.Entry(input_output_file_frame, textvariable=self.input_file_path_var, state='readonly', justify=Tk.LEFT).grid(sticky=Tk.E+Tk.W, row=0, column=1, padx=10)

        # input file selection button
        input_file_selection_button = Tk.Button(input_output_file_frame, text="Open Input File", command=self.on_select_input_file).grid(sticky=Tk.W, row=0, column=2, padx=10)


        # input file label
        output_directory_path_entry_label = Tk.Label(input_output_file_frame, text="Output Directory:")
        output_directory_path_entry_label.grid(sticky=Tk.W, row=1, column=0, padx=10) 

        self.output_directory_path_var = Tk.StringVar() 
        self.output_directory_path_var.set("no directory selected")
        output_directory_path_entry = Tk.Entry(input_output_file_frame, textvariable=self.output_directory_path_var, state='readonly', justify=Tk.LEFT).grid(sticky=Tk.E+Tk.W, row=1, column=1, padx=10)

        # input file selection button
        output_direcotry_selection_button = Tk.Button(input_output_file_frame, text="Select", command=self.on_select_output_directory).grid(sticky=Tk.W, row=1, column=2, padx=10)


        # ffmpeg log
        ffmpeg_log_frame = Tk.LabelFrame(self, text="FFmpeg Log")
        ffmpeg_log_frame.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=1, column=0, columnspan=3, padx=5, pady=5)

        ffmpeg_log_frame.rowconfigure(0, weight=1)
        ffmpeg_log_frame.columnconfigure(0, weight=1)

        ffmpeg_log_text = Tk.Text(ffmpeg_log_frame)
        ffmpeg_log_text.config(state=DISABLED)
        ffmpeg_log_text.grid(sticky=Tk.N+Tk.E+Tk.S+Tk.W, row=0, column=0, padx=5, pady=5)

        # quit and convert button
        quit_and_convert_frame = Tk.Frame(self)
        quit_and_convert_frame.grid(sticky=Tk.E, row=2, column=0)

        quit_button = Tk.Button(quit_and_convert_frame, text="Quit", command=self.root.quit).grid(row=0, column=0)
        convert_button = Tk.Button(quit_and_convert_frame, text="Convert", command=self.on_convert).grid(row=0, column=1)


    def on_select_input_file(self):
        user_dir = Path.home()
        input_file_path_string = askopenfilename(title='Open a video file', initialdir=user_dir)

        if input_file_path_string:
            self.input_file_set = True
            self.input_file_path_var.set(input_file_path_string)


    def on_select_output_directory(self):
        user_dir = Path.home()
        output_directory_path_string = askdirectory(title='Select output directory', initialdir=user_dir)

        if output_directory_path_string:
            self.output_directory_set = True
            self.output_directory_path_var.set(output_directory_path_string)

    def on_convert(self):
        # check if input file is set
        if not self.input_file_set:
            messagebox.showerror("Error", "No input file selected.")
            return

        # check if output directory is set
        if not self.output_directory_set:
            messagebox.showerror("Error", "No output directory selected.")
            return

        # check input file is readable
        if not os.access(self.input_file_path_var.get(), os.R_OK):
            messagebox.showerror("Error", "Input file can not be read.")
            return

        # check if output directory is writable 
        if not os.access(self.output_directory_path_var.get(), os.W_OK):
            messagebox.showerror("Error", "Output directory can not be written to.")
            return

        # check if output file already exists
        output_file_path_string = self.model.get_output_file_path(self.input_file_path_var.get(), self.output_directory_path_var.get())

        if os.path.isfile(output_file_path_string):
            overwrite = messagebox.askyesno("Warning", "Output file already exists.\nDo you want to overwrite it?")

            if overwrite:
                os.remove(output_file_path_string)

            if not overwrite:
                return

        self.model.convert_to_webm(self.input_file_path_var.get(), output_file_path_string)                

    def notify(self):
        pass

    def on_about(self):
        about_dialog = AboutDialog(self.root)

        # make window modal
        about_dialog.wait_visibility()
        about_dialog.focus_set()
        about_dialog.grab_set()
        about_dialog.transient(self.root)
