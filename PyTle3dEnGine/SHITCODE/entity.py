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
        self.camera = pr.Camera3D(pr.Vector3(self.x, self.y, self.z), pr.Vector3(2, 2, 2), pr.Vector3(0, 1, 0), 70, 0)
        
        self.scale = pr.Vector3(0.1, 0.5, 0.1)

        self.speed = 4
        self.sensivity = 5
        
        self.gravity = 10
        self.gravitySpeed = 0
        self.floorRay = pr.Ray(pr.Vector3(self.x, self.y, self.z), pr.Vector3(self.x, 0, self.z))
        self.collidedFloor = False
        self.collidedPosition = 0  # Initial rotation angle in degree

    def Draw(self):
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, pr.WHITE)
        pr.draw_ray(pr.Ray(pr.Vector3(self.camera.position.x, self.camera.position.y, self.camera.position.z), pr.Vector3(self.camera.target.x, self.camera.target.y, self.camera.target.z)), pr.BLACK)

   
    def Update(self):
        self.floorRay = pr.Ray(pr.Vector3(self.x, self.y, self.z), pr.Vector3(0, -1, 0))
        self.x = self.camera.position.x
        self.y = self.camera.position.y - 0.2
        self.z = self.camera.position.z

        if pr.is_key_down(pr.KeyboardKey.KEY_LEFT_SHIFT):
            self.speed = 10
            self.camera.fovy = 80
        else:
            self.speed = 4
            self.camera.fovy = 70
        


        if self.collidedFloor == False:
            self.gravitySpeed += self.gravity * pr.get_frame_time()
            self.camera.position.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
            self.camera.target.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        else:
            self.gravitySpeed = 0
            self.camera.position.y = self.collidedPosition + 0.4
            

        # if not self.collidedFloor == True:
        #     self.gravitySpeed += self.gravity * pr.get_frame_time()
        #     self.camera.position.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        #     self.camera.target.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        # else:
        #     self.camera.position.y = self.collidedPosition + 0.4

        #if not self.collidedFloor == False:



        if pr.is_key_pressed(pr.KeyboardKey.KEY_SPACE) and self.collidedFloor == True:
            self.gravitySpeed += self.gravity * pr.get_frame_time()
            self.camera.position.y += 10 - self.gravitySpeed * pr.get_frame_time()
            self.camera.target.y += self.camera.position.y
            self.collidedFloor = False
        
        
        
        pr.update_camera_pro(self.camera, pr.Vector3((pr.is_key_down(pr.KeyboardKey.KEY_W)* self.speed * pr.get_frame_time() - pr.is_key_down(pr.KeyboardKey.KEY_S) * self.speed * pr.get_frame_time()),
                                                     (pr.is_key_down(pr.KeyboardKey.KEY_D)* self.speed * pr.get_frame_time() - pr.is_key_down(pr.KeyboardKey.KEY_A) * self.speed * pr.get_frame_time()), 0),
                                                     pr.Vector3(pr.get_mouse_delta().x * self.sensivity * pr.get_frame_time(), pr.get_mouse_delta().y * self.sensivity * pr.get_frame_time(), 0), 0)
        # self.camera.target.x = 


        # self.camera.target.y = pitch

    def DetectCollisionBase(self, boxCollides):
        if isinstance(boxCollides, list):
            for boxCollide in boxCollides:
                if pr.check_collision_boxes(
                        pr.BoundingBox(
                            pr.Vector3(self.x - self.scale.x / 2,
                                       self.y - self.scale.y / 2,
                                       self.z - self.scale.z / 2),
                            pr.Vector3(self.x + self.scale.x / 2,
                                       self.y + self.scale.y / 2,
                                       self.z + self.scale.z / 2)
                        ),
                        pr.BoundingBox(
                            pr.Vector3(boxCollide.x - boxCollide.scale.x / 2,
                                       boxCollide.y - boxCollide.scale.y / 2,
                                       boxCollide.z - boxCollide.scale.z / 2),
                            pr.Vector3(boxCollide.x + boxCollide.scale.x / 2,
                                       boxCollide.y + boxCollide.scale.y / 2,
                                       boxCollide.z + boxCollide.scale.z / 2)
                        )
                ):
                    self.collidedFloor = True
                    self.collidedPosition = boxCollide.y
                    return True
            self.collidedFloor = False
            self.collidedPosition = 0
            return False
        else:
            if pr.check_collision_boxes(
                    pr.BoundingBox(
                        pr.Vector3(self.x - self.scale.x / 2,
                                   self.y - self.scale.y / 2,
                                   self.z - self.scale.z / 2),
                        pr.Vector3(self.x + self.scale.x / 2,
                                   self.y + self.scale.y / 2,
                                   self.z + self.scale.z / 2)
                    ),
                    pr.BoundingBox(
                        pr.Vector3(boxCollides.x - boxCollides.scale.x / 2,
                                   boxCollides.y - boxCollides.scale.y / 2,
                                   boxCollides.z - boxCollides.scale.z / 2),
                        pr.Vector3(boxCollides.x + boxCollides.scale.x / 2,
                                   boxCollides.y + boxCollides.scale.y / 2,
                                   boxCollides.z + boxCollides.scale.z / 2)
                    )
            ):
                self.collidedFloor = True
                self.collidedPosition = boxCollides.y
                return True
            else:
                self.collidedFloor = False
                self.collidedPosition = 0
                return False
    


        

    #def DetectCollisionRay(self, mesh):
        #Collided = 0
        #for m in range(mesh.meshCount):
            #Collided = pr.get_ray_collision_mesh(self.floorRay, mesh.meshes[m], mesh.transform)
            #if Collided.hit:
                #print(f"COLLIDI! {mesh.meshCount}")


    
        
        


