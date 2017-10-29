from __future__ import absolute_import, division, print_function
from builtins import object
from .handlers import RequestHandler, ResponseHandler


class DevRant(object):

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

    def search_rants_by_keyword(self, keyword):
        response = self.RequestHandler.search_rants_by_keyword(keyword)
        return self.ResponseHandler.search_rants_by_keyword_build_response(response)

    def get_collabs(self, skip, limit):
        response = self.RequestHandler.get_collabs(skip, limit)
        return self.ResponseHandler.get_collabs_build_response(response)

    def get_collab_by_id(self, collab_id):
        response = self.RequestHandler.get_rant_by_id(collab_id)
        return self.ResponseHandler.get_rant_by_id_build_response(response)
