
from aylienapiclient import textapi

class Analysis:
    def __init__(self):
       self.client = textapi.Client("a3d83921", "e6f553b78d258d7d17b7037bf5e94425")
 
    def analysis(self, text):
        
        classify = self.client.Classify({"text": text})
        concepts = self.client.Concepts({"text": text})
        entities = self.client.Entities({"text": text})
        hashtags = self.client.Hashtags({"text": text})
        
    