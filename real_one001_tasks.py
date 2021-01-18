# pillow library for iimage interaction

import PIL 
from PIL import Image

img = Image.open("automationNinja.PNG")
img.rotate(45).show()

# manioulate size if an image

from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

# rotate image and save to new file
from PIL import Image
im = Image.open("automationNinja.PNG")
new_im = im.rotate(45)
new_im = im.resize((300,500))
new_im.save("rotated.PNG")

# combined in one line with flipped image

from PIL import Image
im = Image.open("Google_ITCourses.PNG")
im.rotate(180).resize((640,480)).save("flipped_and_resized.PNG")
