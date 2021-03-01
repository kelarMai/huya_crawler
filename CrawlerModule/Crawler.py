import requests
import HuyaConfig
import re

class MyRequest():
    def __init__(self):
        pass

    def requestUrls(self,urls,callback):
        for url in urls:
            response_object = requests.get(url)
            callback(response_object)



