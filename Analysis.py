# -*- coding: utf-8 -*-
#input = {'privacy':{'p':[{'name':'Our privacy policy explains how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that Google can use such data in accordance with our privacy policy.'}
#                        ,{'name':"You will ensure that at all times you use the Services, the Properties have a clearly labeled and easily accessible privacy policy that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users’ devices in connection with the Services, including, as applicable, information about end users’ options for cookie management.  You will use commercially reasonable efforts to ensure that an end user gives consent to the storing and accessing of cookies, device-specific information, location information or other information on the end user's device in connection with the Services where such consent is required by law."}] },
#        'taxes':{'p':[{'name':'As between you and Google, Google is responsible for all taxes (if any) associated with the transactions between Google and advertisers in connection with Ads displayed on the Properties.  You are responsible for all taxes (if any) associated with the Services, other than taxes based on Google’s net income.  All payments to you from Google in relation to the Services will be treated as inclusive of tax (if applicable) and will not be adjusted.'}] }
#       }      


from aylienapiclient import textapi
import json

class Analysis:
    def __init__(self):
       self.client = textapi.Client("a3d83921", "e6f553b78d258d7d17b7037bf5e94425")
 
    def analysis(self, obj):
        
        final_hash = {}
        names = []
        for n in input.keys():
		    names.append(n)
        for i in names:
    		para_text=""
    		paras_list = []
    		para = input[i]
    		list_para = para['p']
    		length = len(list_para)
    		for j in range(0,length):
    			p = list_para[j]
    			hashtags = self.client.Hashtags({"text": p['name']})
    			par_hash = {}
    			par_hash["name"] = p['name']
	        	par_hash["tags"] = hashtags['hashtags']
	        	paras_list.append(par_hash)

	        for ind_para in paras_list:
	        	para_text+=ind_para['name']

	        classify = self.client.Classify({"text": para_text})

	        final_hash[i]={}
	        final_hash[i]["classify"]=classify['categories'][0]['label']
	        final_hash[i]['p'] = paras_list

	#print final_hash
        return final_hash
        #summarize = self.client.Summarize({"text": para_text,"title":"policy"})

#a = Analysis()
#obj = Analysis.analysis(a,input)