import pyray as pr
import glm
class Entity:
    def __init__(self, x, y, z, speed, velocity, acceleration):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        self.velocity = velocity
        self.acceleration = acceleration
    
    def Draw(self): ...

    def Update(self): ...

class Player(Entity):
    def __init__(self, x, y, z, speed, velocity, acceleration):
        super().__init__(x, y, z, speed, velocity, acceleration)
        self.camera = pr.Camera3D(pr.Vector3(self.x/2, self.y, self.z), pr.Vector3(2, 2, 2), pr.Vector3(0.0, 0.1, 0.0), 60, 0)
        self.camera.position.x = x
        self.camera.position.z = z
        self.cameraSensiv = pr.Vector3(0, 0, 0)
        self.scale = pr.Vector3(1, 1, 1)

        self.rotation_angle = 0.0  # Initial rotation angle in degrees
        self.rotation_speed = 45.0

    def Draw(self):
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, pr.WHITE)

   

    def Update(self):
        shit = 0
        shit += 0.1
        
        self.rotation_angle += self.rotation_speed * pr.get_frame_time()

        if self.rotation_angle >= 360.0:
            self.rotation_angle -= 360.0
        radius = 10.0

        self.camera.position.x = glm.cos(self.rotation_angle) * pr.get_frame_time()
        self.camera.position.z = glm.sin(self.rotation_angle) * pr.get_frame_time()

        # self.camera.target.x = 

        
        # self.camera.target.y = pitch
        
        


