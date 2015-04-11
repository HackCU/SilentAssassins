import bottle # Web server
from bottle import run, route, request
import json

@route('/')
def index():
    """ Display welcome & instruction messages """
    return "<p>Welcome to my extra simple bottle.py powered server !</p> \
    	   <p>There are two ways to invoke the web service :\
	   <ul><li>http://localhost:8080/up?s=type_your_string_here</li>\
	   <li>http://localhost:8080/up?URL=http://url_to_file.txt</li></ul>"

@route('/up')
def uppercase():
    """ 
    Convert given text to uppercase
    (as a plain argument, or from a textfile's URL)
    Returns an indented JSON structure
    """
    
    # Store HTTP GET arguments
    plain_text   = request.GET.get('s'  , default=None)
    textfile_url = request.GET.get('URL', default=None)

    # Execute WebService specific task
    # here, converting a string to upper-casing
    if plain_text is not None:
        return json.dumps(
            {'input' : plain_text, 
             'result': plain_text.upper()
             },
            indent=4)

    elif textfile_url is not None:
        textfile = urlopen(textfile_url).read()
        return json.dumps(
            {'input' : textfile,
             'output': '\n'.join([line.upper() for line in textfile.split('\n')]) 
             },
            indent=4)


if __name__ == '__main__':        
    # To run the server, type-in $ python server.py
    bottle.debug(True) # display traceback 
    run(host='localhost', port=8000, reloader=True) 