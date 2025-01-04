import pyray as pr
import SHITCODE.BaseObjects as Obj
import SHITCODE.entity as Ent
import SHITCODE.Debug as dg
import numpy as np
import math

class BaseScene:
    def __init__(self):
        self.debug = dg.Debug()
        self.camera = pr.Camera3D([1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 60, 0)
        self.cubes = [Obj.Cube(6, 0, 2, 0, 0.2 * 21, 0.2, 0.2 * 21, pr.RED),
                      Obj.Cube(1, 0, 2, 0, 0.2 * 21, 0.2, 0.2 * 21, pr.BLUE)]
        
        self.player = Ent.Player(1, 2, 2, 2, 2, 2)
        self.count = 0

        
    # Я їбав цей пітон сука блять  
    def Draw(self):
        pr.begin_mode_3d(self.player.camera)

        for i in range(len(self.cubes)):
            self.cubes[i].Draw()
        
        self.player.Draw()

        pr.draw_grid(250, 2)
        pr.end_mode_3d()
        self.debug.Draw(self.player.camera.target.x)

        

    def Update(self):
        self.player.Update()
        for i in range(len(self.cubes)):
            self.cubes[i].UpdateCollision()
        self.count += 1
        


        if pr.is_key_down(pr.KeyboardKey.KEY_TAB):
            self.debug.isShow = True
            pr.disable_cursor()
            pr.show_cursor()
        else:
            self.debug.isShow = False
            pr.set_mouse_position(int(pr.get_screen_width()/2), int(pr.get_screen_height()/2))
            pr.enable_cursor()
            pr.disable_cursor()
        
class Scene:
    def __init__(self):
        self.camera = pr.Camera3D([1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 40, 0)

        
    # Я їбав цей пітон сука блять  
    def Draw(self):
        pr.begin_mode_3d(self.camera)
        for i in range(11):
            for j in range(11):
                Obj.Cube(i, 0, j, 0, 0.2, 0.2, 0.2, 1).Draw()
                Obj.Cube(i + 50, 0, j, 0, 0.2, 0.2, 0.2, pr.GREEN).Draw()

        pr.end_mode_3d()

    def Update(self):
        pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)
        