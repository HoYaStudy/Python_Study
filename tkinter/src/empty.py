import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Empty UI")

        self.canvas = tk.Canvas(self, width=240, height=240, highlightthickness=0)
        self.canvas.pack()


app = Application(master=tk.Tk())
app.mainloop()
