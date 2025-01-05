import pyray as pr
import SHITCODE.BaseObjects as Obj
import SHITCODE.Entity as Ent
import SHITCODE.Debug as dg
import SHITCODE.Hud as hud
import numpy as np
import glm

class BaseScene:
    def __init__(self):
        self.debug = dg.Debug()
        self.hud = hud.Hud()
        self.camera = pr.Camera3D([1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 60, 0)
        self.cubes = [Obj.Cube(1, 2, 2, 0, 5 * 21, 0.2, 5 * 21, pr.BLUE),
                      Obj.Cube(30, 2, 2, 0, 1, 20, 1, pr.BLACK),
                      Obj.Skybox(0, -100, 0, 0, 5000, 0, 5000)]
        self.player = Ent.Player(1, 50, 2, 2, 2, 2)
        self.count = 0
        self.cameraa = self.player.camera

        self.memeImg = pr.load_image("./SHITVISUAL/SHITTEXTURES/PytleLogo.png")
        self.memeTexture = pr.load_texture_from_image(self.memeImg)

        self.music = pr.load_music_stream("./SHITAUDIO/badapple.ogg")
        pr.play_audio_stream(self.music.stream)

        
    # Я їбав цей пітон сука блять  
    def Draw(self):
        pr.begin_mode_3d(self.cameraa)

        for i in range(len(self.cubes)):
            self.cubes[i].Draw()
        
        self.player.Draw()

        #pr.draw_grid(250, 2)
        pr.draw_billboard(self.cameraa, self.memeTexture, pr.Vector3(0, 5, 0), 1, pr.WHITE)
        pr.end_mode_3d()
        self.hud.draw("Bad Apple", "Test ZonE")
        self.debug.Draw(self.cameraa)
        pr.draw_text(f"{self.count}", 10, 10, 10, pr.WHITE)
        

    def Update(self):
        pr.update_music_stream(self.music)
        #pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)
        self.player.Update()
        self.player.DetectCollision(self.cubes[0])
        for i in range(len(self.cubes)):
            self.cubes[i].UpdateCollision()
    

        if pr.is_key_pressed(pr.KeyboardKey.KEY_TAB) and self.debug.isShow == False:
            self.debug.isShow = True
        elif pr.is_key_pressed(pr.KeyboardKey.KEY_TAB) and self.debug.isShow == True:
            self.debug.isShow = False
            
        if self.debug.isShow == False:
            pr.set_mouse_position(int(pr.get_screen_width()/2), int(pr.get_screen_height()/2))
            
        
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
        