import json
import requests
from .models import RantsResponse
from .urlbuilder import URLBuilder


class ResponseHandler:

    def __init__(self):
        self.RantsResponse = RantsResponse()

    def getRantsBuildResponse(self, response):
        json_string = json.loads(response.content)
        deserialized = self.RantsResponse.deserialize(json_string)
        return deserialized


class RequestHandler:
    def __init__(self):
        self.UrlBuilder = URLBuilder()

    def getRants(self, sort, limit, skip):
        url = self.UrlBuilder.getRantURL(sort, limit, skip)
        response = requests.get(url)
        return response
