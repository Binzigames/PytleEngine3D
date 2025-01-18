import pyray as pr
import math

def round_int(x):
    if x in [float("-inf"), float("inf")]: return str(x)
    return int(x)

class Base:
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ):
        self.x = x
        self.y = y
        self.z = z
        self.rotation = rot
        self.scale = pr.Vector3(scaleX, scaleY, scaleZ)

    def Draw(self): 
        ...

    def UpdateCollision(self): ...

class Cube(Base):
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ, color):
        super().__init__(x, y, z, rot, scaleX, scaleY, scaleZ)
        self.color = color
        self.image = pr.gen_image_checked(20, 20, 1, 1, pr.WHITE, color)
        self.texture = pr.load_texture_from_image(self.image)
        self.model = pr.load_model_from_mesh(pr.gen_mesh_cube(self.scale.x, self.scale.y, self.scale.z))
        self.model.materials[0].maps[pr.MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = self.texture
        
        

    def Draw(self):
        pr.draw_model(self.model, pr.Vector3(self.x, self.y, self.z), 1, pr.WHITE)
        pr.draw_cube_wires(pr.Vector3(self.x, self.y, self.z), self.scale.x, self.scale.y, self.scale.z, pr.BLACK)
        self.UpdateCollision()

    def UpdateCollision(self):
        self.CollisionsPos = pr.Vector3(self.x, self.y, self.z)
        self.CollisionsScale = pr.Vector3(self.scale.x, self.scale.y, self.scale.z)



class Skybox(Base):
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ):
        super().__init__(x, y, z, rot, scaleX, scaleY, scaleZ)
        self.image = pr.gen_image_perlin_noise(264, 264, 0, 0, 5)
        self.texture = pr.load_texture_from_image(self.image)
        self.model = pr.load_model_from_mesh(pr.gen_mesh_plane(self.scale.x, self.scale.z, 4, 3))
        self.model.materials[0].maps[pr.MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = self.texture


    def Draw(self):
        pr.rl_push_matrix()
        pr.rl_rotatef(180, 1, 0, 0)
        pr.begin_blend_mode(2)
        pr.draw_model(self.model, pr.Vector3(self.x, self.y, self.z), 1, pr.WHITE)
        pr.end_blend_mode()
        pr.rl_pop_matrix()

class Marisa(Base):
    def __init__(self, x, y, z, rot, scaleX, scaleY, scaleZ):
        super().__init__(x, y, z, rot, scaleX, scaleY, scaleZ)
        self.image = pr.load_image("./Marisa Kirisame/marisa.png")
        self.texture = pr.load_texture_from_image(self.image)
        self.model = pr.load_model("./Marisa Kirisame/Marisa_Kirisame.obj")
        self.model.materials[0].maps[pr.MaterialMapIndex.MATERIAL_MAP_ALBEDO].texture = self.texture

    def Draw(self):
        pr.draw_model(self.model, pr.Vector3(self.x, self.y, self.z), 10, pr.WHITE)
