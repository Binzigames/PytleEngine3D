import pyray as pr
import glm
class Hud:
    def __init__(self):
        self.font = pr.load_font("./SHITVISUAL/SHITFONTS/HomeVideo-Regular.ttf")
        self.count = 0

    def draw(self):
        self.count += 1
        pr.draw_circle(0, 480, 50, pr.RED)
        self.DrawTextShadows("100", 20, 400, 55, 2, pr.RED)

    def DrawTextShadows(self, text, posX, posY, size, leng, color):
        pr.draw_text_pro(self.font, text, pr.Vector2(posX + leng, posY + leng), pr.Vector2(0, 0), 15, size, 1, pr.BLACK)
        pr.draw_text_pro(self.font, text, pr.Vector2(posX, posY), pr.Vector2(0, 0), 15, size, 1, color)