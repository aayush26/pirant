from .handlers import RequestHandler, ResponseHandler


class DevRant:

    def __init__(self):
        self.RequestHandler = RequestHandler()
        self.ResponseHandler = ResponseHandler()

    def getRants(self, sort, limit, skip):
        response = self.RequestHandler.getRants(sort, limit, skip)
        return self.ResponseHandler.getRantsBuildResponse(response)
