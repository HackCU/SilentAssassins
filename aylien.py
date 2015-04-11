# -*- coding: utf-8 -*-

from aylienapiclient import textapi

text = "Our privacy policy explains how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that Google can use such data in accordance with our privacy policy. You will ensure that at all times you use the Services, the Properties have a clearly labeled and easily accessible privacy policy that provides end users with clear and comprehensive information about cookies, device-specific information, location information and other information stored on, accessed on, or collected from end users’ devices in connection with the Services, including, as applicable, information about end users’ options for cookie management.  You will use commercially reasonable efforts to ensure that an end user gives consent to the storing and accessing of cookies, device-specific information, location information or other information on the end user's device in connection with the Services where such consent is required by law."

client = textapi.Client("a3d83921", "e6f553b78d258d7d17b7037bf5e94425")

#summarize = client.Summarize({"text": text})
classify = client.Classify({"text": text})
concepts = client.Concepts({"text": text})
entities = client.Entities({"text": text})
hashtags = client.Hashtags({"text": text})

#print summarize
print "\n--------------------------------------\n"
print classify
print "\n--------------------------------------\n"
print concepts
print "\n--------------------------------------\n"
print entities
print "\n--------------------------------------\n"
print hashtags
