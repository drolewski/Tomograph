import ttkthemes
import tkinter as tk
import matplotlib
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.image as mpimg
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedStyle
import pygubu
from PIL import ImageTk, Image
import os

def addFile(self):
    print("XD")
    pass


class App(pygubu.TkApplication):
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Interface.ui')

        self.window = builder.get_object('main_window')
        self.window.title("Tomograph")
        self.window.geometry('700x740')
        self._create_ui()
        self.prepareCanvas()

        self.style = ThemedStyle(self.window)
        self.style.set_theme("winnative")
        self.window.mainloop()

    def prepareCanvas(self):
        self.image_canvas_container = self.builder.get_object('image_canvas')
        self.image_figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.image_canvas = image_canvas = FigureCanvasTkAgg(
            fig, master=self.image_canvas_container)
        image_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.sinogram_canvas_container = self.builder.get_object(
            'sinogram_canvas')
        self.sinogram_figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.sinogram_canvas = sinogram_canvas = FigureCanvasTkAgg(
            fig, master=self.sinogram_canvas_container)
        sinogram_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.recon_canvas_container = self.builder.get_object('recon_canvas')
        self.recon_figure = fig = Figure(figsize=(3, 3), dpi=100)
        self.recon_canvas = recon_canvas = FigureCanvasTkAgg(
            fig, master=self.recon_canvas_container)
        recon_canvas .get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def addFile(self):
        filename = filedialog.askopenfilename(
            initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.image = mpimg.imread(filename)
        axim = self.image_figure.add_axes([0,0,1,1], anchor='SW')
        axim.imshow(self.image, aspect='auto',cmap='gray')
        axim.axis('off')
        self.image_canvas.draw()
        pass

    def run(self):
        self.generateSinogram()
        self.generateRecon()
        pass

    def generateSinogram(self):
        self.sinogram = self.image
        axim = self.sinogram_figure.add_axes([0,0,1,1], anchor='SW')
        axim.imshow(self.sinogram, aspect='auto',cmap='gray')
        axim.axis('off')
        self.sinogram_canvas.draw()
        pass

    def generateRecon(self):
        self.recon = self.sinogram
        axim = self.recon_figure.add_axes([0,0,1,1], anchor='SW')
        axim.imshow(self.recon, aspect='auto',cmap='gray')
        axim.axis('off')
        self.recon_canvas.draw()
        pass

    def _create_ui(self):
        callbacks = {
            'addFile': self.addFile,
            'run': self.run,
        }
        self.builder.connect_callbacks(callbacks)


if __name__ == '__main__':
    app = App()
