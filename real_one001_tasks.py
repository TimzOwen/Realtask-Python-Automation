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
# imgae manipulation and convertions 

from PIL import Image
import os, sys

user=os.getenv('USER')
images_dir='/home/{}/images/'.format(user)
for image_name in os.listdir(images_dir):
    if not image_name.startswith('.'):
        image_path=images_dir+image_name
        im=Image.open(image_path)
        new_path='/opt/icons/'+image_name.split('.')[0]
        im.rotate(-90).convert('RGB').resize((128,128)).save(new_path,'jpeg')
        im.close()

#json and data serialization

import json

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
    ]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)


# Yet Another Makeup Language

import yaml

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
    ]

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)


import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
    

