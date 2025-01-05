import pyray as pr

class Debug:
    def __init__(self):
        self.imageLogo = pr.load_image("./SHITVISUAL/SHITTEXTURES/PytleLogo.png")
        self.textureLogo = pr.load_texture_from_image(self.imageLogo)
        self.BaseAndStats = []
        self.CameraStats = []
        self.isShow = False
        self.FPS = None
        self.FrameTime = None

    def Draw(self, camera):
        self.FPS = pr.get_fps()
        self.FrameTime = pr.get_frame_time()
        self.BaseAndStats = [f"FPS: {self.FPS}",
                             f"FrameTime: {self.FrameTime}"]
        
        self.CameraStats = [f"CameraPosition: (X: {camera.position.x}, Y: {camera.position.y}, Z: {camera.position.z}",
                            f"CameraTarget: (X: {camera.target.x}, Y: {camera.target.y}, Z: {camera.target.z})"]
        

        if(self.isShow == True):
            pr.draw_texture(self.textureLogo, 15, 15, pr.BLACK)
            pr.draw_texture(self.textureLogo, 10, 10, pr.WHITE)
            self.DrawTextShadows("Ver.proto", 250, 75, 20, 2)

            self.DrawTextShadows("Base", 10, 100, 30, 3)
            for i in range(len(self.BaseAndStats)):
                self.DrawTextShadows(self.BaseAndStats[i], 15, 130 + i * 20, 20, 2)

            self.DrawTextShadows("Camera Stats", 10, 170, 30, 3)

            for i in range(len(self.CameraStats)):
                self.DrawTextShadows(self.CameraStats[i], 15, 200 + i * 20, 20, 2)


    def DrawTextShadows(self, text, posX, posY, size, leng):
        pr.draw_text(text, posX + leng, posY + leng, size, pr.BLACK)
        pr.draw_text(text, posX, posY, size, pr.WHITE)
