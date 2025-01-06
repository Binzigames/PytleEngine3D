import pyray as pr
import glm
class Hud:
    def __init__(self):
        self.font = pr.load_font("./SHITVISUAL/SHITFONTS/HomeVideo-Regular.ttf")
        self.count = 800

    def draw(self, music, level, shit):
        self.count -= 2
        if self.count >= -100:
            self.DrawTextShadows("M: " + music, self.count, 20, 20, 2, pr.WHITE)
            self.DrawTextShadows(level, self.count, 40, 40, 4, pr.BLUE)
        else:
            self.count = -100

        
        pr.draw_circle(0, 480, 50, pr.RED)
        self.DrawTextShadows(f"{shit}", 20, 400, 55, 5, pr.RED)

    def DrawTextShadows(self, text, posX, posY, size, leng, color):
        pr.draw_text(text, posX+leng, posY+leng, size, pr.BLACK)
        pr.draw_text(text, posX, posY, size, color)

    
            
            