import json
import requests
from .models import RantsResponse, RantResponse
from .urlbuilder import URLBuilder


class ResponseHandler:

    def __init__(self):
        self.RantsResponse = RantsResponse()
        self.RantResponse = RantResponse()

    def getRantsBuildResponse(self, response):
        json_string = json.loads(response.content)
        deserialized = self.RantsResponse.deserialize(json_string)
        return deserialized

    def getRantByIdBuildResponse(self, response):
        json_string = json.loads(response.content)
        deserialized = self.RantResponse.deserialize(json_string)
        return deserialized

class RequestHandler:
    def __init__(self):
        self.UrlBuilder = URLBuilder()

    def getRants(self, sort, limit, skip):
        url = self.UrlBuilder.getRantURL(sort, limit, skip)
        response = requests.get(url)
        return response

    def getRantById(self, rantId):
        url = self.UrlBuilder.getRantByIdURL(rantId)
        response = requests.get(url)
        return response