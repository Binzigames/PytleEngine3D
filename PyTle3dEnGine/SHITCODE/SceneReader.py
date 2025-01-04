import pyray as pr

class ReadScene:
    def __init__(self):
        self.camera = pr.Camera3D([1.0, 1.0, 1.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 60, 0)

    # пайтон уйобіще блядь!

    def Draw(self, cell_size, map_data):
        pr.begin_mode_3d(self.camera)
        for z, row in enumerate(map_data):
            for x, cell in enumerate(row):
                pos = (x * cell_size, 0, z * cell_size)
                if cell == 1:
                    pr.draw_cube(pos, cell_size, cell_size, cell_size, pr.BLUE)
                    pr.draw_cube_wires(pos, cell_size, cell_size, cell_size, pr.BLACK)
        pr.end_mode_3d()

    def Update(self):
        pr.update_camera(self.camera, pr.CameraMode.CAMERA_FREE)
