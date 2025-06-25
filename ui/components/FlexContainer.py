import tkinter as tk

class FlexContainer(tk.Frame):
    def __init__(self, parent, direction="row", gap=4, **kwargs):
        super().__init__(parent, **kwargs)
        self.direction = direction
        self.gap = gap

    def add(self, widget, expand = False, fill = True):

        widget.pack(side = tk.LEFT if self.direction == "row" else tk.TOP,
                    padx = (0 if self.direction == "column" else self.gap),
                    pady = (self.gap if self.direction == "column" else 0),
                    expand = expand,
                    fill = tk.BOTH if fill else tk.NONE)

