from time import sleep
from peter import Peter
from math import pi, cos, sin
from pyautogui import size as screen_size
import asyncio


class App:

    def __init__(self) -> None:
        self.QUANTITY = 30
        self.peters: list[Peter | None] = [None for x in range(self.QUANTITY)]
        w, h = screen_size()
        r = h//3
        w, h = w//2, h//2
        self.POINTS = tuple((int(w + r * cos(2 * pi * i / self.QUANTITY)), 
                        int(h + r * sin(2 * pi * i / self.QUANTITY))) 
                        for i in range(self.QUANTITY))
        self.current_peter = 0
        asyncio.run(self.peter_loop())

    async def create_peter(self, index: int) -> None:
        await asyncio.sleep(0.01)
        self.peters[index] = Peter(self.POINTS[index][0], self.POINTS[index][1])

    async def peter_loop(self) -> None:
        for i in range(200):
            await self.create_peter(self.current_peter)
            if self.peters[self.current_peter - 5] is not None:
                self.peters[(self.current_peter - 5) % self.QUANTITY].quit_peter()
                self.peters[(self.current_peter - 5) % self.QUANTITY] = None
            self.current_peter = (self.current_peter + 1) % self.QUANTITY
            await asyncio.sleep(0.01)



if __name__ == "__main__":
    App()

