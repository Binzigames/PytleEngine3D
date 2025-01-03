import pyray as pr
import SHITCODE.Scene1 as ass
import SHITCODE.Debug as debugg
class Game:
    def __init__(self):
        pr.init_window(1920, 1060, "Hello")
        #pr.set_target_fps(60)
        self.scene = ass.BaseScene()
        self.debug = debugg.Debug()
        pr.disable_cursor()
        #pr.toggle_fullscreen()
    

    def run(self):
        while not pr.window_should_close():
            self.draw()
            self.update()
        pr.close_window()

    def draw(self):
        pr.begin_drawing()
        pr.clear_background(pr.GRAY)
        self.scene.Draw()
        self.debug.Draw()
        #pr.draw_fps(0, 0)
        pr.end_drawing()
    
    def update(self):
        self.scene.Update()
        if pr.is_key_down(pr.KeyboardKey.KEY_TAB):
            self.debug.isShow = True
        else:
            self.debug.isShow = False
            
        
        

        
            