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
        sc = Scrapper.Scrapper()
        obj = sc.scrap(url);
        #print obj
        #obj = json.dumps({'privacy':{'p':[{'name':'first para in privacy'},{'name':'second para in privacy'}] },
        # 'taxes':{'p':[{'name':'first para in taxes'},{'name':'second para in taxes'}] }
        #})
        obj = Analysis.Analysis().analysis(obj)

        #obj = json.dumps({'privacy':{'classify':'computer software','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
        # 'taxes':{'classify':'computer software','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] }
        #})
                                
        obj = Generator.Generator().generate(obj) 
                               
        return json.dumps(obj,indent=4)

if __name__ == '__main__':        
    bottle.debug(True)
    run(host='localhost', port=8000, reloader=True)