from time import sleep
from random import randint
from peter import Peter
from pyautogui import size
import tkinter as tk
from threading import Thread

class App:

    def __init__(self) -> None:
        self.PETER_WIDTH = 300
        self.PETER_HEIGHT = 200
        self.PETER_GEOMETRY = f"{self.PETER_WIDTH}x{self.PETER_HEIGHT}"
        self.screen_size = size()
        self.root = tk.Tk()
        self.peters: list[Peter] = [Peter(self.root, (self.screen_size[0] - self.PETER_WIDTH) // 2,
                                          (self.screen_size[1] - self.PETER_HEIGHT) // 2, 
                                          self.PETER_WIDTH, self.PETER_HEIGHT)]
        self.root.withdraw()
        Thread(target=self.peter_loop, daemon=True).start()
        self.root.mainloop()
    
    def peter_loop(self) -> None:
        while True:
            peters_to_remove: list[Peter] = []
            peter_flag = False
            for peter in self.peters:
                if not peter.peter:
                    peters_to_remove.append(peter)
                elif peter.new_peter:
                    peter_flag = True
            for peter in peters_to_remove:   
                self.peters.remove(peter)
            if peter_flag:
                self.peters.append(Peter(self.root, randint(200, self.screen_size[0] - self.PETER_WIDTH - 200),
                                          randint(200, self.screen_size[1] - self.PETER_HEIGHT - 200), 
                                          self.PETER_WIDTH, self.PETER_HEIGHT))
            if len(self.peters) > 100:
                self.peters = []
            if not self.peters:
                self.root.destroy()
            sleep(0.05)

if __name__ == "__main__":
    App()

