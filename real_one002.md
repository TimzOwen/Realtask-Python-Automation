### HTTP GET and POST Methods

HTTP supports several [HTTP methods](https://tools.ietf.org/html/rfc7231#section-4.3), like GET, POST, PUT, and DELETE

[HTTP GET](https://tools.ietf.org/html/rfc7231#section-4.3.1)  gets resources specified by the URL by sending Get request to the server

Get request parameter

    https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15

These parameters are one or more key-value pairs, formatted as a [query string](https://en.wikipedia.org/wiki/Query_string)

[Requests.get()](https://requests.readthedocs.io/en/master/api/#requests.get)  constructs a URL based on a set of dictionary search

[HTTP POST method](https://tools.ietf.org/html/rfc7231#section-4.3.3) is a good alternative if data is large. This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're using the POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit.

Contains **'data'** that will be sent  as part of POST request instead of params as in GET 

    >>> p = {"description": "white kitten",
    ...      "name": "Snowball",
    ...      "age_months": 6}
    >>> response = requests.post("https://example.com/path/to/api", data=p)

URL generated request

    >>> response.request.url
    'https://example.com/path/to/api'

Body HTTP message

    >>> response.request.body
    'description=white+kitten&name=Snowball&age_months=6'

Using JSON to send and receive data over web

    >>> response = requests.post("https://example.com/path/to/api", json=p)
    >>> response.request.url
    'https://example.com/path/to/api'
    >>> response.request.body
    b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 

[Learn more Request Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)

