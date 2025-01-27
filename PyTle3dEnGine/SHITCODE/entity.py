import pyray as pr
import glm
import SHITCODE.BaseObjects as obj
import SHITCODE.Gun as gn

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
        self.lock = False
        self.camera = pr.Camera3D(pr.Vector3(self.x, self.y, self.z), pr.Vector3(2, 2, 2), pr.Vector3(0, 1, 0), 70, 0)
        
        self.scale = pr.Vector3(0.1, 0.5, 0.1)

        self.speed = 4
        self.sensivity = 5
        
        self.gravity = 7
        self.gravitySpeed = 0
        self.floorRay = pr.Ray(pr.Vector3(self.x, self.y, self.z), pr.Vector3(self.x, 0, self.z))
        self.collidedFloor = False
        self.collidedPosition = 0
        self.kill = False
        
        self.bullets = []
        self.gun = gn.Gun()

    def Draw(self):
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, pr.WHITE)
        pr.draw_ray(pr.Ray(pr.Vector3(self.camera.position.x, self.camera.position.y, self.camera.position.z), pr.Vector3(self.camera.target.x, self.camera.target.y, self.camera.target.z)), pr.BLACK)
        for i in range(len(self.bullets)):
            self.bullets[i].Draw()
    def DrawGun(self):
        if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
            self.gun.draw_muzle_flash()
        self.gun.Draw()
        print("its looks like a gun!")
   
    def Update(self):

        for i in range(len(self.bullets)):
            self.bullets[i].Update()

        

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
        
        if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
            self.bullets.append(Bullet(self.camera.position.x, self.camera.position.y, self.camera.position.z, 0, 0, 0, self.camera, pr.Vector3(self.camera.target.x, self.camera.target.y, self.camera.target.z)))
            print(self.bullets)

        if self.collidedFloor == False:
            self.y = self.camera.position.y
            self.gravitySpeed += self.gravity / 60
            self.camera.position.y += 0.2 - self.gravitySpeed / 60
            self.camera.target.y += 0.2 - self.gravitySpeed / 60
            self.y += 0.2 - self.gravitySpeed / 60
        else:
            self.y = self.camera.position.y
            # self.camera.position.y = self.y - 0.3
            self.gravitySpeed = 0
            

        # if not self.collidedFloor == True:
        #     self.gravitySpeed += self.gravity * pr.get_frame_time()
        #     self.camera.position.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        #     self.camera.target.y += 0.2 - self.gravitySpeed * pr.get_frame_time()
        # else:
        #     self.camera.position.y = self.collidedPosition + 0.4

        #if not self.collidedFloor == False:



        if pr.is_key_pressed(pr.KeyboardKey.KEY_SPACE) and self.collidedFloor == True:
            self.gravitySpeed += self.gravity / 60
            self.y += 2 - self.gravitySpeed / 60
            self.camera.position.y += 2 - self.gravitySpeed / 60
            self.camera.target.y += self.camera.position.y
            
            self.gravitySpeed += self.gravity / 60
            self.camera.position.y += 2 - self.gravitySpeed / 60
            self.camera.target.y += 2 - self.gravitySpeed / 60
        
        
        if self.lock == False:
            pr.update_camera_pro(self.camera, pr.Vector3((pr.is_key_down(pr.KeyboardKey.KEY_W)* self.speed / 60 - pr.is_key_down(pr.KeyboardKey.KEY_S) * self.speed / 60),
                                                        (pr.is_key_down(pr.KeyboardKey.KEY_D)* self.speed / 60 - pr.is_key_down(pr.KeyboardKey.KEY_A) * self.speed / 60), 0),
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


class Bullet(Entity):
    def __init__(self, x, y, z, speed, velocity, acceleration, camera, target):
        super().__init__(x, y, z, speed, velocity, acceleration)
        self.camera = camera
        self.scale = pr.Vector3(0.1, 0.1, 0.1)
        self.texture = pr.load_texture_from_image(pr.gen_image_checked(2, 2, 1, 1, pr.BLACK, pr.MAGENTA))
        self.target = target
        self.delay = 100

    def __delattr__(self, name):
        del self.camera
        del self.target
        del self.delay

    def Update(self):
        self.delay -= 1
        if self.delay <= 0:
            del self
            

    def Draw(self):
        if not self.delay <= 0:
            pr.draw_ray(pr.Ray(pr.Vector3(self.x, self.y, self.z), pr.Vector3(self.target.x, self.target.y - 4, self.target.z)), pr.RED)

    



