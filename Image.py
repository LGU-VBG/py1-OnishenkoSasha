class Image:
    resolution = [720, 720]
    title = 'image'
    extension = 'png'

    def __init__(self, width, height, titleIn, extensionIn):
        self.resolution = [width, height]
        self.title = titleIn
        self.extension = extensionIn

    def resize(self, width, height):
        self.resolution = [width, height]



image0 = Image(140, 140, 'flover', 'png')
image1 = Image(360, 360, 'wall', 'jpg')

image0.resize(360, 360)