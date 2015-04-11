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
       
    def generate(self, obj):
        categories = {}
        obj = json.loads(obj)
        for key,value in obj.iteritems():
            if(value['classify'] not in categories):
                categories[value['classify']] = []
            categories[value['classify']].append({'key':key,'value':value})     
        final = {} 
        final['children'] = []  
        for level in categories:
            final['children'].append({ 'name': level,"children":self.getChilds(categories[level])})
        return final
                        
    def getChilds(self, level):
        children = [] 
        for eachChild in level:
            child = {}
            child["name"] = eachChild["key"]
            child["children"] = []
            for eachP in eachChild['value']['p']:
                node = {}
                node["name"] = eachP['name']
                node["tags"] = eachP['tags']                
                node["summarizer"] = eachP['summarizer']
                child["children"].append(node)    
            children.append(child)
        return children

#gen = Generator()
#print gen.generate(obj)