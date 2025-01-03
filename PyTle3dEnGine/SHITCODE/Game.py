import pyray as pr
import SHITCODE.Scene1 as ass

class Game:
    def __init__(self):
        pr.init_window(800, 450, "Hello")
        self.scene = ass.BaseScene()

    def run(self):
        while not pr.window_should_close():
            self.draw()
            self.update()
        pr.close_window()

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        self.scene.Draw()
        pr.end_drawing()
    
    def update(self):
        self.scene.Update()