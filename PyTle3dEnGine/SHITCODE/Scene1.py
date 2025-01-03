import pyray as pr
import SHITCODE.BaseObjects as Obj
import numpy as np

class BaseScene:
    def __init__(self):
        self.cube = Obj.Cube(0, 0, 0, 0, 1, 1, 1)
        self.camera = pr.Camera3D([20.0, 20.0, 20.0], [self.cube.x, self.cube.y, self.cube.z], [0.0, 1.0, 0.0], 40, 0)

        
    # Я їбав цей пітон сука блять  
    def Draw(self):
        self.cube.Draw()

    def Update(self):
        pr.update_camera(self.camera, pr.CameraMode.CAMERA_ORBITAL)
        self.cube.UpdateCollision()

        