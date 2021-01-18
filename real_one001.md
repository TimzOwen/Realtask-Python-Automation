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



