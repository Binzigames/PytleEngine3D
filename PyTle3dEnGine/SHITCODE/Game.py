import pyray as pr
import SHITCODE.Scene1 as ass
import SHITCODE.Debug as debugg
import SHITCODE.SceneReader as SR
from SHITCODE.SceneReader import ReadScene


class Game:
    def __init__(self):
        pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE | pr.ConfigFlags.FLAG_VSYNC_HINT)
        pr.init_window(1280, 900, "Pytle3D (proto ver.)")
        pr.init_audio_device()
        self.Test_map =[
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
            [1, 0,0 , 1, 1, 1, 0, 0, 0, 1,],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1,],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1,],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1,],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1,],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]
        ]

        self.gameScreenWidth = 732
        self.gameScreenHeight = 480
        self.renderScreen = pr.RenderTexture2D
        self.renderScreen = pr.load_render_texture(self.gameScreenWidth, self.gameScreenHeight)
        #pr.set_texture_filter(self.renderScreen.texture, 1)
        self.scale = 0
        #pr.set_target_fps(60)
        self.scene = ass.BaseScene()
        #pr.toggle_fullscreen()
        
    
        

    def run(self):
        while not pr.window_should_close():
            self.draw()
            self.update()
        pr.close_window()

    def draw(self):
        pr.begin_texture_mode(self.renderScreen)
        pr.clear_background(pr.GRAY)
        #self.scene.Draw()
        self.scene.Draw()
        #pr.draw_fps(0, 0)
        pr.end_texture_mode()

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_texture_pro(self.renderScreen.texture, pr.Rectangle(0, 0, float(self.renderScreen.texture.width), float(-self.renderScreen.texture.height)), pr.Rectangle((pr.get_screen_width() - float(self.gameScreenWidth*self.scale))*0.5, (pr.get_screen_height() - float(self.gameScreenHeight*self.scale))*0.5, float(self.gameScreenWidth*self.scale), float(self.gameScreenHeight*self.scale)), pr.Vector2(0, 0), 0.0, pr.WHITE)
        pr.end_drawing()
    
    def update(self):
        self.scale = min(float(pr.get_screen_width()/self.gameScreenWidth), float(pr.get_screen_height()/self.gameScreenHeight))
        self.scene.Update()
            
        
        

        
            