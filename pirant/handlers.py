from __future__ import absolute_import, division, print_function
import json
import requests
from builtins import object
from .models import RantsResponse, RantResponse, SearchResponse
from .urlbuilder import URLBuilder


class ResponseHandler(object):

    def __init__(self):
        self.RantsResponse = RantsResponse()
        self.RantResponse = RantResponse()
        self.SearchResponse = SearchResponse()

    def build_response(self, model, response):
        json_string = json.loads(response.content)
        deserialized = model.deserialize(json_string)
        return deserialized
    
    def get_rants_build_response(self, response):
        return self.build_response(self.RantsResponse, response)

    def get_rant_by_id_build_response(self, response):
        return self.build_response(self.RantResponse, response)

    def search_rants_by_keyword_build_response(self, response):
        return self.build_response(self.SearchResponse, response)

    def get_collabs_build_response(self, response):
        return self.build_response(self.RantsResponse, response)

class RequestHandler(object):

    def __init__(self):
        self.UrlBuilder = URLBuilder()

    def get_rants(self, sort, limit, skip):
        url = self.UrlBuilder.get_rants_url(sort, limit, skip)
        response = requests.get(url)
        return response

    def get_rant_by_id(self, rant_id):
        url = self.UrlBuilder.get_rant_by_id_url(rant_id)
        response = requests.get(url)
        return response

    def get_weekly_rants(self, sort, skip):
        url = self.UrlBuilder.get_weekly_rant_url(sort, skip)
        response = requests.get(url)
        return response

    def search_rants_by_keyword(self, keyword):
        url = self.UrlBuilder.search_rants_by_keywords(keyword)
        response = requests.get(url)
        return response
      
    def get_collabs(self, skip, sort):
        url = self.UrlBuilder.get_collabs_url(skip, sort)
        response = requests.get(url)
        return response
