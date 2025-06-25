import tkinter as tk


class GridContainer(tk.Frame):
    def __init__(self, parent, columns = 2, gap = 10, **kwargs):

        super().__init__(parent, **kwargs)
        self.columns = columns
        self.gap = gap
        self.row = 0
        self.col = 0

    def add(self, widget):
        widget.grid(row = self.row, column = self.col, padx = self.gap, pady = self.gap, sticky="nsew")

        self.columnconfigure(self.col, weight = 1)
        self.rowconfigure(self.row, weight = 1)

        self.col += 1
        if self.col >= self.columns:
            self.col = 0
            self.row += 1

