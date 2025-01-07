import pyray as pr

class Gun:
    def __init__(self):
        self.image = pr.load_image("./SHITVISUAL/SHITTEXTURES/FuckingGun.png")
        self.texture = pr.load_texture_from_image(self.image)

    def Draw(self):
        pr.draw_texture_ex(self.texture, pr.Vector2(400, 200), 0, 2.5, pr.WHITE)
        pr.draw_text("50/50", 400 + 3, 200 + 200 + 3, 50, pr.BLACK)
        pr.draw_text("50/50", 400, 200 + 200, 50, pr.WHITE)