"""DevRant class providing API methods."""

from __future__ import absolute_import, division, print_function
from pirant.handlers import RequestHandler, ResponseHandler


class DevRant(object):
    """API Class providing interface methods."""

    def __init__(self):
        """Initialize the class instance."""
        self.request_handler = RequestHandler()
        self.response_handler = ResponseHandler()

    def get_rants(self, sort, limit, skip):
        """
        Fetch rants from API.

        :param sort:
        :param limit:
        :param skip:
        :return:
        """
        response = self.request_handler.get_rants(sort, limit, skip)
        return self.response_handler.get_rants_build_response(response)

    def get_rant_by_id(self, rant_id):
        """
        Feth a rant by its rant ID.

        :param rant_id:
        :return:
        """
        response = self.request_handler.get_rant_by_id(rant_id)
        return self.response_handler.get_rant_by_id_build_response(response)

    def get_weekly_rants(self, sort, skip):
        """
        Fetch the weekly rants.

        :param sort:
        :param skip:
        :return:
        """
        response = self.request_handler.get_weekly_rants(sort, skip)
        return self.response_handler.get_rants_build_response(response)

    def search_rants_by_keyword(self, keyword):
        """
        Search rants by given keyword.

        :param keyword:
        :return:
        """
        response = self.request_handler.search_rants_by_keyword(keyword)
        return self.response_handler.search_rants_by_keyword_build_response(response)

    def get_collabs(self, skip, limit):
        """
        Fetch collabs from the API.

        :param skip:
        :param limit:
        :return:
        """
        response = self.request_handler.get_collabs(skip, limit)
        return self.response_handler.get_collabs_build_response(response)

    def get_collab_by_id(self, collab_id):
        """
        Fetch a collab by its collab ID.

        :param collab_id:
        :return:
        """
        response = self.request_handler.get_rant_by_id(collab_id)
        return self.response_handler.get_rant_by_id_build_response(response)
