#obj = json.dumps({[{'head':{'name':'privacy','classify':'computer software','p':{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} }},
#    {'head':{'name':'taxes','classify':'computer software','p':{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} }}
#]})


##### Input Format
#obj = json.dumps({'privacy':{'classify':'computer software','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'taxes':{'classify':'computer software','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'something':{'classify':'cat 2','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'some other thing':{'classify':'cat 3','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] }
#        })

import json

class Generator:
       
    def generate(self, obj,title):
        
        categories = {}
        
        for key,value in obj.iteritems():
            if(value['classify'] not in categories):
                categories[value['classify']] = []
            categories[value['classify']].append({'key':key,'value':value})     
        final = {}
        final['name'] = title 
        final["size"] = len(final["name"])*20000
        final['children'] = []  
        for level in categories:
            final['children'].append({ 'name': level,"children":self.getChilds(categories[level])})
        
        json.dump(final, open("generator.json","w"))
        return final
                
    def getChilds(self, level):
        children = [] 
        for eachChild in level:
            child = {}
            child["name"] = eachChild["key"]
            child["size"] = len(child["name"])*20000
            child["children"] = []
            for eachP in eachChild['value']['p']:
                node = {}
                node["name"] = eachP['name']
                node["size"] = len(node["name"])*20000
                node["tags"] = eachP['tags']                
                node["summary"] = eachP['summary']
                child["children"].append(node)    
            children.append(child)
        return children

#gen = Generator()
#print gen.generate(obj)