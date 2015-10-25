import urllib.request
import json

"""
This class is responsible for reading in all json data either from the API or cached files.
DataManager has 2 functions: read_api_call() and read_cached_data(). The first takes a url
for a REST call and returns the json format data received. The second takes a file name or
file path and returns the json format data read from the file.
"""


class DataManager:
    # returns json format data from API call
    @staticmethod
    def read_api_call(url):
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        return data

    # returns json format data from cache file
    @staticmethod
    def read_cached_data(file_name):
        data_file = open(file_name)
        data = json.loads(''.join(data_file.readlines()))
        data_file.close()
        return data
