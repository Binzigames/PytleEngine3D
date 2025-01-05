import pyray as pr
import glm
import SHITCODE.BaseObjects as obj

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
        self.camera = pr.Camera3D(pr.Vector3(self.x, self.y, self.z), pr.Vector3(2, 2, 2), pr.Vector3(0, 1, 0), 60, 0)
        
        self.scale = pr.Vector3(0.1, 0.5, 0.1)

        self.rotation_angle = 0.0
        self.speed = 5
        self.sensivity = 5
        
        self.gravity = 15
        self.gravitySpeed = 0
        self.force = 2
        self.mass = 3  # Initial rotation angle in degree

    def Draw(self):
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, pr.WHITE)
        pr.draw_ray(pr.Ray(pr.Vector3(self.camera.position.x, self.camera.position.y, self.camera.position.z), pr.Vector3(self.camera.target.x, self.camera.target.y, self.camera.target.z)), pr.BLACK)

   
    def Update(self):
        self.x = self.camera.position.x
        self.y = self.camera.position.y - 0.2
        self.z = self.camera.position.z

        
        


        
        
        pr.update_camera_pro(self.camera, pr.Vector3((pr.is_key_down(pr.KeyboardKey.KEY_W)* self.speed * pr.get_frame_time() - pr.is_key_down(pr.KeyboardKey.KEY_S) * self.speed * pr.get_frame_time()),
                                                     (pr.is_key_down(pr.KeyboardKey.KEY_D)* self.speed * pr.get_frame_time() - pr.is_key_down(pr.KeyboardKey.KEY_A) * self.speed * pr.get_frame_time()), 0),
                                                     pr.Vector3(pr.get_mouse_delta().x * self.sensivity * pr.get_frame_time(), pr.get_mouse_delta().y * self.sensivity * pr.get_frame_time(), 0), 0)
        # self.camera.target.x = 


        # self.camera.target.y = pitch

    def DetectCollision(self, boxCollide):
        if not pr.check_collision_boxes(pr.BoundingBox(pr.Vector3(self.x - self.scale.x/2,
                                                              self.y - self.scale.y/2,
                                                              self.z - self.scale.z/2),
                                                   pr.Vector3(self.x + self.scale.x/2,
                                                              self.y + self.scale.y/2,
                                                              self.z + self.scale.z/2)),
                                                              
                                 pr.BoundingBox(pr.Vector3(boxCollide.x - boxCollide.scale.x/2,
                                                           boxCollide.y - boxCollide.scale.y/2,
                                                           boxCollide.z - boxCollide.scale.z/2),
                                                pr.Vector3(boxCollide.x + boxCollide.scale.x/2,
                                                           boxCollide.y + boxCollide.scale.y/2,
                                                           boxCollide.z + boxCollide.scale.z/2))):
            self.gravitySpeed += self.gravity * pr.get_frame_time()
            self.camera.position.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
            self.camera.target.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        else:
            self.camera.position.y = boxCollide.y + 0.4
            self.gravitySpeed = 0

        
        if pr.is_key_pressed(pr.KeyboardKey.KEY_SPACE):
            self.gravitySpeed += self.gravity * pr.get_frame_time()
            self.camera.position.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
            self.camera.target.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        


