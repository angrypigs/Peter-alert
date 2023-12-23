from os import path
import sys
import tkinter as tk
from threading import Thread

class Peter:

    def __init__(self, w: float, h: float) -> None:
        Thread(target=self.__init_peter, args=(w, h, ), daemon=True).start()

    def __init_peter(self, w: int, h: int) -> None:
        self.WIDTH = 300
        self.HEIGHT = 200
        self.master = tk.Tk()
        self.master.title("Peter alert")
        self.master.geometry(f"{self.WIDTH}x{self.HEIGHT}+{w - self.WIDTH // 2}+{h - self.HEIGHT // 2}")
        self.master.resizable(False, False)
        self.master.iconbitmap(default = self.res_path("peter griffin icon.ico"))
        self.pixel = tk.PhotoImage(master=self.master, height = 1, width = 1)
        self.canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH,
                                bd=0, highlightthickness=0)
        self.canvas.place(x = 0, y = 0)
        peter_image = tk.PhotoImage(master=self.master, file = self.res_path("peter griffin.png"))
        self.canvas.create_image(self.WIDTH // 2, self.HEIGHT / 4, anchor = 'center',
                                 image = peter_image)
        tk.Button(self.canvas, image = self.pixel, compound = 'c', height = 30, width = 100, text = "OK"
                  ).place(x = self.WIDTH // 2, y = self.HEIGHT / 4 * 3, anchor = 'center')
        self.master.mainloop()

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
        self.master.destroy()

