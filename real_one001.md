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


[Read on the YAML](https://yaml.org/)

format:

    import yaml

    with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

Output of generated code

    - department: IT Infrastructure
    name: Sabrina Green
    phone:
        cell: 802-867-5310
        office: 802-867-5309
    role: Systems Administrator
    username: sgreen
-   department: IT Infrastructure
    name: Eli Jones
    phone:
        office: 684-348-1127
    role: IT Specialist
    username: ejones

YAML is used mostly to store configuration values

#### Other tools

[Python Pickle](https://docs.python.org/3/library/pickle.html)

[Protocol Buffers](https://developers.google.com/protocol-buffers)

[Extensible makeup Language XML](https://www.w3.org/XML/)

#### More on JSON

#### More on JSON

[JSON](https://json.org/)

json makes data human readable by converting complex data into a readable format

sample:

    {
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002,
  "phone": {
    "office": "802-867-5309",
    "cell": "802-867-5310"
     }
    }

JSON arrays

    [
  "apple",
  "banana",
  12345,
  67890,
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
     }
    ]

you have to import Json 

    import json

you can use dump to serialize the data


### Load vs dump

The **load()** method does the inverse of the __dump()__ method. It deserializes JSON from a file into basic Python objects. The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.

    >>> import json
    >>> with open('people.json', 'r') as people_json:
    ...     people = json.load(people_json)
    ... 
    >>> print(people)
    [{'name': 'Sabrina Green', 'username': 'sgreen', 'phone': {'office': '802-867-5309', 'cell': '802-867-5310'}, 'department': 'IT Infrastructure', 'role': 'Systems           Administrator'}, {'name': 'Eli Jones', 'username': 'ejones', 'phone': {'office': '684-348-1127'}, 'department': 'IT Infrastructure', 'role': 'IT Specialist'}, {'name':           'Melody Daniels', 'username': 'mdaniels', 'phone': {'cell': '846-687-7436'}, 'department': 'User Experience Research', 'role': 'Programmer'}, {'name': 'Charlie Rivera',      'username': 'riverac', 'phone': {'office': '698-746-3357'}, 'department': 'Development', 'role': 'Web Developer'}]

[Converting Python objects into into Json](https://docs.python.org/3/library/json.html#py-to-json-table)
