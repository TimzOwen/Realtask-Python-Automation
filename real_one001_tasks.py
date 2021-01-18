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
    
# Processing Textfiles python dictionaries and uploading them to running web servies
#! /usr/bin/env python3
import os
import requests

import json

# put the IP_ADDRESS here
IP_ADDRESS = '127.0.0.1'

feedback_path = '/data/feedback/'
post_data_keys = ['title', 'name', 'date', 'feedback']
corpweb_feedback_url = 'http://{}/feedback/'.format(IP_ADDRESS)

def process_feedback(filename):

    post_data = {}
    with open(filename, 'r') as fb:
        lines = fb.readlines()

        for k, line in zip(post_data_keys, lines):
            post_data.update({k: line})

    response = requests.post(corpweb_feedback_url, json=post_data)
    response.raise_for_status()

def process_feedbacks():

    for feedback in os.listdir(feedback_path):
        process_feedback(os.path.join(feedback_path, feedback))

def main():

    print('Posting feedbacks from {} folder'.format(feedback_path))
    print('Posting feedbacks to {}'.format(corpweb_feedback_url))

    process_feedbacks()

    print('Done... Exiting')

if __name__ == '__main__':





