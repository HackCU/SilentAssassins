import json

class Generator:
    def __init__(self):
       print ""
       
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
            #print level
            final['children'].append({ 'name': level,"children":self.getChilds(categories[level])})
        return final
                        
    def getChilds(self, level):
        children = [] 
        print "--------------------------------------"
        for eachChild in level:
            child = {}
            #print eachChild
            #print "$$$$$$$$$$$$$$$$$$$$"
            child["name"] = eachChild["key"]
            child["children"] = []
            #print eachChild['value']
            for eachP in eachChild['value']['p']:
                #for p in eachP['p']:
                node = {}
                node["name"] = eachP['name']                
                child["children"].append(node)    
                #print eachP
            children.append(child)
        return children
    
#obj = json.dumps({[{'head':{'name':'privacy','classify':'computer software','p':{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} }},
#    {'head':{'name':'taxes','classify':'computer software','p':{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},'p':{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']} }}
#]})

obj = json.dumps({'privacy':{'classify':'computer software','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
         'taxes':{'classify':'computer software','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
         'something':{'classify':'cat 2','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
         'some other thing':{'classify':'cat 3','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] }
        })

#obj = json.dumps({'privacy':{'classify':'computer software','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'taxes':{'classify':'computer software','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'something':{'classify':'cat 2','p':[{'name':'first para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in privacy','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] },
#         'some other thing':{'classify':'cat 3','p':[{'name':'first para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']},{'name':'second para in taxes','summarizer':'example of summarized paragraph','tags':['tag1','tag2','tag3']}] }
#        })

#print obj 
gen = Generator()
print gen.generate(obj)