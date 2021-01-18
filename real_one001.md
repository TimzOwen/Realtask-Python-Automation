## Python external tools

#### built-in Libraries and external libraries

New libraries are published in (PYPL): python package index

[pypi.org](https://pypi.org/)

#### Python image library

used to convert images and manipulate images

[PIL library for python below version 3](http://www.pythonware.com/products/pil/)

[Pillow image lib for python 3](https://pypi.org/project/Pillow/)

Ubuntu install:

    sudo apt install python3-pil

    pip3 install pillow ---> for other packages

#### API (Application Programming Interface)

Helps different pieces of software to talk to each other

Have a deeper understanding of how functions are called and used in APIs

Can also be used as pieces of software 

used as a communicaiton platform for softwares

[Saving breaking changes in an API](https://semver.org/#summary)

#### Making Sense out of  an API

Have your APIs functions follow naming conventions to help a user have a clear expectation

Example:

    from PIL import Image
    im = Image.open("bride.jpg")
    im.rotate(45).show()

[Reference page for the image objects above ](https://pillow.readthedocs.io/en/stable/reference/Image.html)

For py library like PIL its documented using docstring (Doc that lives within the code)

[Pillow Full documentation](https://pillow.readthedocs.io/)

[PIL handbook](https://pillow.readthedocs.io/en/stable/handbook/index.html)

[Tutorials for PIL](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)


===========================================================================================latest commit

#### using PIL with images manipulation

Resize image :

    from PIL import Image   (imports the library)
    im = Image("example.jpg") (opens the image)
    new_im = im.resize((640,480)) (Resize the image to a different pixel)
    new_im.save("example_resized.jpg") (save image to bew resolution)

[More Practice with PIL , check the Docs](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)


### web Application Services

This are applications  that users interact with over HTTP

user sends a quest to server and receives a request of information rendered in HTML web browser

Web apps that have APIs are called **Web Services**

Sends __API CALLS__ to a web services  and the part listening to the call is called **API Endpoint**



### Data serialization

Process of writing data into understandable formarts like **CSV** 

Data serialization is the process of taking an in-memory data structure, like a Python object, and turning it 

into something that can be stored on disk or transmitted across a network

Turning the serialized object back into an in-memory object is called __deserialization__

Example of CSV data

    name,username,phone,department,role
    Sabrina Green,sgreen,802-867-5309,IT Infrastructure,System Administrator
    Eli Jones,ejones,684-3481127,IT Infrastructure,IT specialist

Data in dictionary state

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

Add more data in same formart (added phone number )

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

### Json and Serialization

[Interact with JSON (JavaScript Object Notation)](https://json.org/)

Open and dump data:

    import json

    with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)


### Yet Another Makeup Language

