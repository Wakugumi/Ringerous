import tkinter as tk

class Label(tk.Frame):
    def __init__(self, parent, text, **kwargs):
        super().__init__(parent, **kwargs)
        self.label = tk.Label(self, text = text, font = ("Arial", 14))
        self.label.pack()
