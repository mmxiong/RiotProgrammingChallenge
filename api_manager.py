import urllib.request
import json

"""
This class has only one method -- make_api_call() that takes in a url for the GET request
from the Riot API. It then reads the data, decodes it from byte form into a string, and
loads it into a json object to be returned.
"""


class ApiManager:
    @staticmethod
    def make_api_call(url):

        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        return data


