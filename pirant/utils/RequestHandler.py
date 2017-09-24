from .UrlBuilder import URLBuilder
import requests

class RequestHandler:
    def __init__(self):
        self.UrlBuilder = URLBuilder()

    def getRants(self, sort, limit, skip):
        url = self.UrlBuilder.getRantURL(sort, limit, skip)
        response = requests.get(url)
        return response