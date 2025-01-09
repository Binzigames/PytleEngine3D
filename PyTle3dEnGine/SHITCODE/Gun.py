import pyray as pr
import SHITCODE.Game as GM
import random

class Gun:
    def __init__(self):

        self.image = pr.load_image("./SHITVISUAL/SHITTEXTURES/AT47.png")
        self.muzle_flash = pr.load_image("./SHITVISUAL/SHITTEXTURES/MuzleFlash.png")
        self.texture = pr.load_texture_from_image(self.image)
        self.texture_MF = pr.load_texture_from_image(self.muzle_flash)
        self.screen_height = GM.gameScreenHeight
        self.screen_width = GM.gameScreenWidth


    def draw_muzle_flash(self):
        sprite_x = self.screen_width / 2
        sprite_y = self.screen_height  - 100
        rotation = random.randrange(1 , 15)
        pr.draw_texture_pro(self.texture_MF, pr.Rectangle(0, 0, 39, 37), pr.Rectangle(sprite_x, sprite_y, 360, 360), pr.Vector2(sprite_x/2, sprite_y/2),rotation, pr.WHITE)



    def Draw(self):
        sprite_x = self.screen_width / 2
        sprite_y = self.screen_height - 390


        pr.draw_texture_ex(self.texture, pr.Vector2(sprite_x, sprite_y), 0, 20, pr.WHITE)
        pr.draw_text("50/50", 400 + 3, 200 + 200 + 3, 50, pr.BLACK)
        pr.draw_text("50/50", 400, 200 + 200, 50, pr.WHITE)
        pr.draw_text("[1] 2", 400+10+2, 200+200+50+2, 20, pr.BLACK)
        pr.draw_text("[1] 2", 400+10, 200+200+50, 20, pr.WHITE)