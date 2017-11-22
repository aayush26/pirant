"""Request and Response handlers for interfacing with the DevRant API."""
from __future__ import absolute_import, division, print_function
import json
import requests
from pirant.models import RantsResponse, RantResponse, SearchResponse
from pirant.urlbuilder import URLBuilder


class ResponseHandler(object):
    """Handles deserialization of API responses to pirant Response Objects."""

    def __init__(self):
        """Initialize the instance."""
        self.rants_response = RantsResponse()
        self.rant_response = RantResponse()
        self.search_response = SearchResponse()

    @staticmethod
    def build_response(model, response):
        """Build a  response for the given Response Object and model."""
        json_string = json.loads(response.content)
        deserialized = model.deserialize(json_string)
        return deserialized

    def get_rants_build_response(self, response):
        """Deserialize the given Rants to RantsResponse object."""
        return self.build_response(self.rants_response, response)

    def get_rant_by_id_build_response(self, response):
        """Deserialize the given Rant to RantsResponse object."""
        return self.build_response(self.rant_response, response)

    # pylint: disable=invalid-name
    def search_rants_by_keyword_build_response(self, response):
        """Deserialize the given Search to SerachResponse object."""
        return self.build_response(self.search_response, response)

    def get_collabs_build_response(self, response):
        """Deserialize the given Collabs to RantsResponse object."""
        return self.build_response(self.rants_response, response)


class RequestHandler(object):
    """Handles generating a request URL for pirant Requests."""

    def __init__(self):
        """Initialize the instance."""
        self.url_builder = URLBuilder()

    def get_rants(self, sort, limit, skip):
        """Build a request to get rants, send it and return its repsonse."""
        url = self.url_builder.get_rants_url(sort, limit, skip)
        response = requests.get(url)
        return response

    def get_rant_by_id(self, rant_id):
        """Build the request to get a rant by id, send it and return its repsonse."""
        url = self.url_builder.get_rant_by_id_url(rant_id)
        response = requests.get(url)
        return response

    def get_weekly_rants(self, sort, skip):
        """Build the request to get the weekly rants, send it and return its repsonse."""
        url = self.url_builder.get_weekly_rant_url(sort, skip)
        response = requests.get(url)
        return response

    def search_rants_by_keyword(self, keyword):
        """Build the request to search for rants by keyword, send it and return its repsonse."""
        url = self.url_builder.search_rants_by_keywords(keyword)
        response = requests.get(url)
        return response

    def get_collabs(self, skip, sort):
        """Build the request to get all collabs, send it and return its repsonse."""
        url = self.url_builder.get_collabs_url(skip, sort)
        response = requests.get(url)
        return response
