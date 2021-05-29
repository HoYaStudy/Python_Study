import tkinter as tk
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Draw Shapes")

        self.canvas = tk.Canvas(self, width=240, height=240, highlightthickness=0)
        self.canvas.pack()

        self.canvas.delete("all")

        self.on_draw_lines()
        self.on_draw_circles()
        self.on_draw_rectangles()
        self.on_draw_polygons()
        self.on_draw_images()
        self.on_draw_texts()

    def on_draw_lines(self):
        self.canvas.create_line(20, 20, 100, 20)
        self.canvas.create_line(20, 40, 100, 40, width=1, fill="#d32f2f")
        self.canvas.create_line(20, 60, 100, 60, width=3, fill="#f57c00")
        self.canvas.create_line(20, 80, 100, 80, width=2, fill="#fbc02d", dash=(5, 2))
        self.canvas.create_line(20, 100, 100, 100, 100, 120, fill="#388e3c")

    def on_draw_circles(self):
        self.canvas.create_oval(140, 20, 160, 40)
        self.canvas.create_oval(180, 20, 220, 40, width=3)
        self.canvas.create_oval(140, 60, 170, 90, fill="#00796b")
        self.canvas.create_oval(190, 60, 220, 90, outline="#1976d2", dash=(5, 2))

    def on_draw_rectangles(self):
        self.canvas.create_rectangle(20, 140, 40, 170)
        self.canvas.create_rectangle(60, 140, 90, 160, width=2)
        self.canvas.create_rectangle(
            20, 190, 50, 220, width=4, fill="#303f9f", outline="#7b1fa2"
        )
        self.canvas.create_rectangle(60, 190, 90, 220, outline="#5d4037", dash=(5, 2))

    def on_draw_polygons(self):
        self.canvas.create_polygon(
            140,
            140,
            155,
            155,
            170,
            140,
            155,
            170,
            width=2,
            fill="red",
            outline="blue",
            dash=(3, 3),
        )
        self.canvas.create_arc(
            190,
            140,
            220,
            170,
            start=60,
            extent=120,
            style="arc",
        )
        self.canvas.create_arc(
            190,
            190,
            220,
            220,
            start=200,
            extent=150,
            width=3,
            fill="green",
            outline="blue",
            dash=(5, 2),
        )

    def on_draw_images(self):
        self.img = ImageTk.PhotoImage(Image.open("test_image.jpg"))
        self.canvas.create_image(140, 190, image=self.img, anchor=tk.NW)

    def on_draw_texts(self):
        self.canvas.create_text(
            20, 110, text="Hello tkinter", font="consolas 12", anchor=tk.NW
        )


app = Application()
app.pack()
app.mainloop()
