from .handlers import RequestHandler, ResponseHandler


class DevRant:

    def __init__(self):
        self.RequestHandler = RequestHandler()
        self.ResponseHandler = ResponseHandler()

    def getRants(self, sort, limit, skip):
        response = self.RequestHandler.getRants(sort, limit, skip)
        return self.ResponseHandler.getRantsBuildResponse(response)

    def getRantById(self, rantId):
        response = self.RequestHandler.getRantById(rantId)
        return self.ResponseHandler.getRantByIdBuildResponse(response)
