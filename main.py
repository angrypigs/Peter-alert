import tkinter as tk
import sys
import os

class App:

    def __init__(self) -> None:
        self.WIDTH = 300
        self.HEIGHT = 200
        self.master = tk.Tk()
        self.master.title("Peter alert")
        self.master.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.master.resizable(False, False)
        self.master.iconbitmap(default=self.res_path("peter griffin icon.ico"))
        self.pixel = tk.PhotoImage(height=1,width=1)
        self.canvas = tk.Canvas(self.master, height=self.HEIGHT, width=self.WIDTH,
                                bd=0, highlightthickness=0)
        self.canvas.place(x=0,y=0)
        peter_image = tk.PhotoImage(file=self.res_path("peter griffin.png"))
        self.canvas.create_image(self.WIDTH//2, self.HEIGHT/4, anchor='center',
                                 image=peter_image)
        tk.Button(self.canvas, image=self.pixel, compound='c', height=30, width=100, text="OK",
                  command=lambda: self.close_app()).place(
                      x=self.WIDTH//2, y=self.HEIGHT/4*3, anchor='center')
        self.master.mainloop()
    
    def res_path(self, rel_path: str) -> str:
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = sys.path[0]
        return os.path.join(base_path, rel_path)
    
    def close_app(self) -> None:
        self.master.quit()

if __name__ == "__main__":
    App()