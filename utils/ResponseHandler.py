import json
from models.RantsResponse import RantsResponse

class ResponseHandler:

    def __init__(self):
        self.RantsResponse = RantsResponse()

    def getRantsBuildResponse(self, response):
        deserialized = self.RantsResponse.deserialize(json.loads(response.content))
        return deserialized