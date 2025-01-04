import pyray as pr

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
        self.scale = pr.Vector3(1, 1, 1)

    def Draw(self):
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z)
        