# -*- coding: utf-8 -*-
#http://www.hasbro.com/en-us/terms
#input = {'privacy':{'p':[{'name':'Our privacy policy explains how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that Google can use such data in accordance with our privacy policy.'}
#                        ,{'name':"You will ensure that at all times you use the Services, the Properties have a clearly labeled and easily accessible privacy policy that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users’ devices in connection with the Services, including, as applicable, information about end users’ options for cookie management.  You will use commercially reasonable efforts to ensure that an end user gives consent to the storing and accessing of cookies, device-specific information, location information or other information on the end user's device in connection with the Services where such consent is required by law."}] },
#        'taxes':{'p':[{'name':'As between you and Google, Google is responsible for all taxes (if any) associated with the transactions between Google and advertisers in connection with Ads displayed on the Properties.  You are responsible for all taxes (if any) associated with the Services, other than taxes based on Google’s net income.  All payments to you from Google in relation to the Services will be treated as inclusive of tax (if applicable) and will not be adjusted.'}] }
#       }    
import requests
import os
import json
from bs4 import BeautifulSoup
import codecs
from aylienapiclient import textapi

class Scrapper:

    def __init__(self):
        None
        
    def scrap1(self,url):
        r =requests.get(url)
        soup=BeautifulSoup(r.content)
        strr= str(soup.find_all(class_="textblock_text"))
        strcpy=strr.replace("<h3>","$").replace("<h4>","$").replace("</h3>","$").replace("</h4>","$").replace("<p>", "").replace("</p>","").replace("[","").replace("]","")
        strcpy= strcpy.split("$")
        strNew=[]
        
        for each in strcpy:
            if(len(each)!=0):
                strNew.append(each)
        del strNew[0]

        i = 0
        obj = {}
        while(i<len(strNew)):
            print i
            obj[strNew[i]] = {'p':[{'name':strNew[i+1]}] }        
            i = i+2
        #print obj
        return obj        
    
    def rmGarbage(self,strr):
        val=["browser","cookies","signing in", "all rights reserved"] # append bullshit words here to filter more and more
        for each in val:
            if(each.lower() in strr.lower()):
                return False
        return True
        
    def scrap(self,url):
        
        self.client = textapi.Client("69285ee3", "cd2036c898a03bcc45fd3b4178c5c0d8")
        #Links tested on
        #html_doc =requests.get('http://www.colorado.edu/controller/approving-officials-procedural-statement')
        #html_doc=requests.get('http://www.hasbro.com/en-us/terms')
        html_doc=requests.get(url)
        #html_doc=requests.get('http://www.apple.com/legal/internet-services/itunes/us/terms.html')
        #html_doc=requests.get('https://twitter.com/tos?lang=en')
        #html_doc=requests.get('http://en.wikipedia.org/wiki/Apple')
        html_doc= html_doc.content  # get all content of webpage
        html_doc=''.join([i if ord(i) < 128 else '' for i in html_doc]) # remove utf-8
        soup = BeautifulSoup(html_doc) # reform webpage
        title = soup.title.string 
        para=soup.find_all("p")
        paralist=[]
        para=str(para).replace("[","").replace("]","").replace("u'","")
        para=BeautifulSoup(para)
        
        for each in para.find_all("p"):
            paralist.append(each.get_text())
        
        #Filter some garbage values
        paralistgrb=paralist[:]
        paralist=[]
        for each in paralistgrb:
            if(self.rmGarbage(each)):
                paralist.append(each)
        
        #Will print the paragraph in order
        obj = {}
        

        
        
        for each in paralist:
            if("." in each and len(each)>30):
                try:
                    print each
                    each=each.encode('utf-8')
                    
                    hashtags = self.client.Hashtags({"text": each})   
                    obj[hashtags['hashtags'][0]] = {'p':[{"name":each}]}
                except:
                    print "exceptioneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
                    None
        print obj
        newObj = {}
        newObj['title'] = title
        newObj['obj'] = obj 
        print "SCRAPPER"
        print newObj
        return newObj
            
#url = "http://www.hasbro.com/en-us/terms"
#ob = Scrapper()
#ob.scrap(url)