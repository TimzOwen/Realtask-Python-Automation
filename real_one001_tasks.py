# pillow library for iimage interaction

import PIL 
from PIL import Image

img = Image.open("automationNinja.PNG")
img.rotate(45).show()
