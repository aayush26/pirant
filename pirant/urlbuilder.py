from __future__ import absolute_import, division, print_function
from builtins import str
from builtins import object

class URLBuilder(object):
    def __init__(self):
        self.APP_VERSION = 3
        self.BASE_URL = "https://www.devrant.com/api"
        self.RANTS_URL = "%s/devrant/rants?sort=%s&limit=%d&skip=%d&app=%d"
        self.WEEKLY_RANTS_URL = "%s/devrant/weekly-rants?sort=%s&skip=%d&app=%d"
        self.RANT_PATH = "%s/devrant/rants/%d?app=%d"
        self.SEARCH_PATH = "%s/devrant/search?term=%s&app=%d"
        self.SORT_TOP = "top"
        self.SORT_ALGO = "algo"
        self.SORT_RECENT = "recent"
        self.VALID_SORTS = [self.SORT_ALGO, self.SORT_RECENT, self.SORT_TOP]

    def get_rant_url(self, sort, limit, skip):
        sort = self.validate_sort_input(self, sort)
        limit = self.validate_int_input(limit)
        skip = self.validate_int_input(skip)
        return str(self.RANTS_URL % (self.BASE_URL, sort, limit, skip, self.APP_VERSION))

    def get_rant_by_id_url(self, rant_id):
        return str(self.RANT_PATH % (self.BASE_URL, rant_id, self.APP_VERSION))

    def get_weekly_rant_url(self, sort, skip):
        sort = self.validate_sort_input(self, sort)
        skip = self.validate_int_input(skip)
        return str(self.WEEKLY_RANTS_URL % (self.BASE_URL, sort, skip, self.APP_VERSION))

    def search_rants_by_keywords(self, keyword):
        return str(self.SEARCH_PATH % (self.BASE_URL, keyword, self.APP_VERSION))

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
