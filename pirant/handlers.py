import json
import requests
from .models import RantsResponse, RantResponse
from .urlbuilder import URLBuilder


class ResponseHandler:

    def __init__(self):
        self.RantsResponse = RantsResponse()
        self.RantResponse = RantResponse()

    def get_rants_build_response(self, response):
        json_string = json.loads(response.content)
        deserialized = self.RantsResponse.deserialize(json_string)
        return deserialized

    def get_rant_by_id_build_response(self, response):
        json_string = json.loads(response.content)
        deserialized = self.RantResponse.deserialize(json_string)
        return deserialized


class RequestHandler:

    def __init__(self):
        self.UrlBuilder = URLBuilder()

    def get_rants(self, sort, limit, skip):
        url = self.UrlBuilder.get_rant_url(sort, limit, skip)
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
