from __future__ import absolute_import, division, print_function
from builtins import str
from builtins import object

class URLBuilder(object):
    def __init__(self):
        self.APP_VERSION = 3
        self.BASE_URL = "https://www.devrant.io/api/devrant"
        self.RANTS_URL = "%s/rants?sort=%s&limit=%d&skip=%d&app=%d"
        self.WEEKLY_RANTS_URL = "%s/weekly-rants?sort=%s&skip=%d&app=%d"
        self.RANT_URL = "%s/rants/%d?app=%d"
        self.SEARCH_URL = "%s/search?term=%s&app=%d"
        self.COLLABS_URL = "%s/collabs?app=%d&skip=%d&limit=%d"
        self.SORT_TOP = "top"
        self.SORT_ALGO = "algo"
        self.SORT_RECENT = "recent"
        self.VALID_SORTS = [self.SORT_ALGO, self.SORT_RECENT, self.SORT_TOP]

    def get_rants_url(self, sort, limit, skip):
        sort = self.validate_sort_input(self, sort)
        limit = self.validate_int_input(limit)
        skip = self.validate_int_input(skip)
        return str(self.RANTS_URL % (self.BASE_URL, sort, limit, skip, self.APP_VERSION))

    def get_rant_by_id_url(self, rant_id):
        return str(self.RANT_URL % (self.BASE_URL, rant_id, self.APP_VERSION))

    def get_weekly_rant_url(self, sort, skip):
        sort = self.validate_sort_input(self, sort)
        skip = self.validate_int_input(skip)
        return str(self.WEEKLY_RANTS_URL % (self.BASE_URL, sort, skip, self.APP_VERSION))

    def search_rants_by_keywords(self, keyword):
        return str(self.SEARCH_URL % (self.BASE_URL, keyword, self.APP_VERSION))

    def get_collabs_url(self, skip, limit):
        limit = self.validate_int_input(limit)
        skip = self.validate_int_input(skip)
        return str(self.COLLABS_URL % (self.BASE_URL, self.APP_VERSION, skip, limit))

    @staticmethod
    def validate_sort_input(self, sort_type):
        if sort_type == "":
            sort_type = "top"
        elif sort_type not in self.VALID_SORTS:
            raise ValueError("Invalid Sort type")
        return sort_type

    @staticmethod
    def validate_int_input(some_int):
        if some_int >= 0:
            return some_int
        raise ValueError("Positive integer required")
