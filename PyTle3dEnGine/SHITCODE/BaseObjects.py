import pyray as pr

class Base:
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ):
        self.x = x
        self.y = y
        self.z = z
        self.rotation = rot
        self.scale = pr.Vector3(scaleX, scaleY, scaleZ)

    def Draw(self): ...

    def UpdateCollision(self): ...

class Cube(Base):
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ, color):
        super().__init__(x, y, z, rot, scaleX, scaleY, scaleZ)
        self.color = color

    def Draw(self):
        pr.draw_cube(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, self.color)
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, self.color)
        self.UpdateCollision()

    def UpdateCollision(self):
        self.CollisionsPos = pr.Vector3(self.x, self.y, self.z)
        self.CollisionsScale = pr.Vector3(self.scale.x, self.scale.y, self.scale.z)

    