import bottle # Web server
from bottle import run, route, request
import json

import Scrapper
import Analysis
import Generator

@route('/')
def index():
    """ Display welcome & instruction messages """
    return "<p>Welcome to my extra simple bottle.py powered server !</p> \
    	   <p>There are two ways to invoke the web service :\
	   <ul><li>http://localhost:8080/up?s=type_your_string_here</li>\
	   <li>http://localhost:8080/up?URL=http://url_to_file.txt</li></ul>"

@route('/up')
def uppercase():  
    url   = request.GET.get('s'  , default=None)
    
    if url is not None:
        #url = "http://www.apple.com/legal/internet-services/itunes/us/terms.html"         
        obj = Scrapper.scrap(url);
        
        obj = json.dumps({'head':{'name':'privacy','p':{'name':'first para in privacy'},'p':{'name':'second para in privacy'} },
         'head':{'name':'taxes','p':{'name':'first para in taxes'},'p':{'name':'second para in taxes'} },
         'head':{'name':'indemnity','p':{'name':'first para in indemnity'},'p':{'name':'second para in indemnity'} },
        })
        obj = Analysis.analysis(obj)

        obj = json.dumps({'head':{'name':'privacy','classify':'computer software','p':{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} },
         'head':{'name':'taxes','classify':'computer software','p':{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} }
        })
                                
        obj = Generator.generate(obj) 
            
        #obj = {
        #    'input' : url, 
        #    'result': url.upper()
        #}                                
        return json.dumps(obj,indent=4)

if __name__ == '__main__':        
    bottle.debug(True)
    run(host='localhost', port=8000, reloader=True) 