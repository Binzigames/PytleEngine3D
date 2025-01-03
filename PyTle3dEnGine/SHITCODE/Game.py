import pyray as pr
class Game:
    def __init__(self):
        pr.init_window(800, 450, "Hello")

    def run(self):
        while not pr.window_should_close():
            self.draw()
            self.update()
        pr.close_window()

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        pr.draw_text("Hello world", 190, 200, 20, pr.VIOLET)
        pr.end_drawing()
    
    def update(self):
        pass