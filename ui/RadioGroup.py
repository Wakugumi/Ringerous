import tkinter as tk


class RadioGroup(tk.Frame):
    def __init__(self, parent, options, default=None, command = None, **kwargs):
        super().__init__(parent, **kwargs)

        self.var = tk.StringVar(value = default)
        self.command = command

        for opt in options:
            rb = tk.Radiobutton(
                self,
                text = opt,
                value = opt,
                variable = self.var,
                command = self._on_change
            )
            rb.pack(anchor="w")


    # callback to return value on value change
    def _on_change(self):
        if self.command:
            self.command(self.var.get())

    def get_value(self):
        return self.var.get()

    def set_value(self, value):
        self.var.set(value)

