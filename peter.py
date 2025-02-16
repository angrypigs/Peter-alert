from os import path
import sys
import tkinter as tk

class Peter:

    def __init__(self, root: tk.Tk, w: float, h: float, width: int, height: int) -> None:
        self.WIDTH = width
        self.HEIGHT = height
        self.peter = True
        self.new_peter = False
        self.master = tk.Toplevel(root)
        self.master.geometry(f"{width}x{height}+{w - self.WIDTH // 2}+{h - self.HEIGHT // 2}")
        self.master.title("Peter alert")
        self.master.resizable(False, False)
        self.master.iconbitmap(default = self.res_path("peter griffin icon.ico"))
        self.pixel = tk.PhotoImage(master=self.master, height = 1, width = 1)
        self.canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH,
                                bd=0, highlightthickness=0)
        self.canvas.place(x = 0, y = 0)
        self.peter_image = tk.PhotoImage(file = self.res_path("peter griffin.png"))
        self.canvas.create_image(self.WIDTH // 2, self.HEIGHT / 4, anchor = 'center',
                                 image = self.peter_image)
        tk.Button(self.canvas, image = self.pixel, compound = 'c', height = 30, width = 100, text = "OK", command=self.quit_peter
                  ).place(x = self.WIDTH // 2, y = self.HEIGHT / 4 * 3, anchor = 'center')
        self.master.protocol("WM_DELETE_WINDOW", self.peter_signal)

    def res_path(self, rel_path: str) -> str:
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = sys.path[0]
        return path.join(base_path, rel_path)
    
    def quit_peter(self) -> None:
        self.master.withdraw()
        self.master.after(20, self.destroy_peter)

    def destroy_peter(self) -> None:
        self.peter = False
        self.master.destroy()
    
    def peter_signal(self) -> None:
        self.new_peter = True

