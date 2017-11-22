"""Request and Response handlers for interfacing with the DevRant API."""
from __future__ import absolute_import, division, print_function
import json
import requests
from builtins import object
from pirant.models import RantsResponse, RantResponse, SearchResponse
from pirant.urlbuilder import URLBuilder


class ResponseHandler(object):

    def __init__(self):
        self.rants_response = RantsResponse()
        self.rant_response = RantResponse()
        self.search_response = SearchResponse()

    def build_response(self, model, response):
        json_string = json.loads(response.content)
        deserialized = model.deserialize(json_string)
        return deserialized
    
    def get_rants_build_response(self, response):
        return self.build_response(self.rants_response, response)

    def get_rant_by_id_build_response(self, response):
        return self.build_response(self.rant_response, response)

    def search_rants_by_keyword_build_response(self, response):
        return self.build_response(self.search_response, response)

    def get_collabs_build_response(self, response):
        return self.build_response(self.rants_response, response)


class RequestHandler(object):

    def __init__(self):
        self.url_builder = URLBuilder()

    def get_rants(self, sort, limit, skip):
        url = self.url_builder.get_rants_url(sort, limit, skip)
        response = requests.get(url)
        return response

    def get_rant_by_id(self, rant_id):
        url = self.url_builder.get_rant_by_id_url(rant_id)
        response = requests.get(url)
        return response

    def get_weekly_rants(self, sort, skip):
        url = self.url_builder.get_weekly_rant_url(sort, skip)
        response = requests.get(url)
        return response

    def search_rants_by_keyword(self, keyword):
        url = self.url_builder.search_rants_by_keywords(keyword)
        response = requests.get(url)
        return response
      
    def get_collabs(self, skip, sort):
        url = self.url_builder.get_collabs_url(skip, sort)
        response = requests.get(url)
        return response
