import pyray as pr
import SHITCODE.BaseObjects as Obj
import SHITCODE.Entity as Ent
import SHITCODE.Debug as dg
import SHITCODE.Hud as hud
import numpy as np
import math

class BaseScene:
    def __init__(self):
        self.debug = dg.Debug()
        self.hud = hud.Hud()
        self.camera = pr.Camera3D([1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 60, 0)
        self.cubes = [Obj.Cube(1, 2, 2, 0, 5 * 21, 0.2, 5 * 21, pr.BLUE)]
        
        self.player = Ent.Player(1, 50, 2, 2, 2, 2)
        self.count = 0
        self.cameraa = self.player.camera

        
    # Я їбав цей пітон сука блять  
    def Draw(self):
        pr.begin_mode_3d(self.cameraa)

        for i in range(len(self.cubes)):
            self.cubes[i].Draw()
        
        self.player.Draw()

        pr.draw_grid(250, 2)
        pr.end_mode_3d()
        pr.draw_text("CAMPOS: {posX}, {posY}, {posZ}\nCAMTARGET: {tarX}, {tarY}, {tarZ}\nGRAVITY: {gr} GRAVITY SPEED: {grsp}".format(posX = self.cameraa.position.x, posY = self.cameraa.position.y, posZ = self.cameraa.position.z, tarX = self.camera.target.x, tarY = self.cameraa.target.y, tarZ = self.cameraa.target.z, gr = self.player.gravity, grsp = self.player.gravitySpeed), 200, 100, 10, pr.WHITE)
        self.debug.Draw()
        self.hud.draw()

        

    def Update(self):
        #pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)
        self.player.DetectCollision(self.cubes[0])
        self.player.Update()
        for i in range(len(self.cubes)):
            self.cubes[i].UpdateCollision()
        self.count += 1
    

        if pr.is_key_down(pr.KeyboardKey.KEY_TAB):
            self.debug.isShow = True
            self.cameraa = self.camera
            pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)
        else:
            self.cameraa = self.player.camera
            pr.set_mouse_position(int(pr.get_screen_width()/2), int(pr.get_screen_height()/2))
            self.debug.isShow = False
            
        
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
        