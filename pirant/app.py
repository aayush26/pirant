from .handlers import RequestHandler, ResponseHandler


class DevRant:

    def __init__(self):
        self.RequestHandler = RequestHandler()
        self.ResponseHandler = ResponseHandler()

    def get_rants(self, sort, limit, skip):
        response = self.RequestHandler.get_rants(sort, limit, skip)
        return self.ResponseHandler.get_rants_build_response(response)

    def get_rant_by_id(self, rant_id):
        response = self.RequestHandler.get_rant_by_id(rant_id)
        return self.ResponseHandler.get_rant_by_id_build_response(response)

    def get_weekly_rants(self, sort, skip):
        response = self.RequestHandler.get_weekly_rants(sort, skip)
        return self.ResponseHandler.get_rants_build_response(response)
