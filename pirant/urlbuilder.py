"""URL constructor class to generate valid API request URLs."""
from __future__ import absolute_import, division, print_function
from builtins import str
from builtins import object


class URLBuilder(object):
    """Handles generating valid URLs to requests resources from DevRant."""
    
    def __init__(self):
        self.app_version = 3
        self.base_url = "https://www.devrant.com/api/devrant"
        self.rants_url = "%s/rants?sort=%s&limit=%d&skip=%d&app=%d"
        self.weekly_rants_url = "%s/weekly-rants?sort=%s&skip=%d&app=%d"
        self.rant_url = "%s/rants/%d?app=%d"
        self.search_url = "%s/search?term=%s&app=%d"
        self.collabs_url = "%s/collabs?app=%d&skip=%d&limit=%d"
        self.sort_top = "top"
        self.sort_algo = "algo"
        self.sort_recent = "recent"
        self.valid_sorts = [self.sort_algo, self.sort_recent, self.sort_top]

    def get_rants_url(self, sort, limit, skip):
        sort = self.validate_sort_input(self, sort)
        limit = self.validate_int_input(limit)
        skip = self.validate_int_input(skip)
        return str(self.rants_url % (self.base_url, sort, limit, skip, self.app_version))

    def get_rant_by_id_url(self, rant_id):
        return str(self.rant_url % (self.base_url, rant_id, self.app_version))

    def get_weekly_rant_url(self, sort, skip):
        sort = self.validate_sort_input(self, sort)
        skip = self.validate_int_input(skip)
        return str(self.weekly_rants_url % (self.base_url, sort, skip, self.app_version))

    def search_rants_by_keywords(self, keyword):
        return str(self.search_url % (self.base_url, keyword, self.app_version))

    def get_collabs_url(self, skip, limit):
        limit = self.validate_int_input(limit)
        skip = self.validate_int_input(skip)
        return str(self.collabs_url % (self.base_url, self.app_version, skip, limit))

    @staticmethod
    def validate_sort_input(self, sort_type):
        if sort_type == "":
            sort_type = "top"
        elif sort_type not in self.valid_sorts:
            raise ValueError("Invalid Sort type")
        return sort_type

    @staticmethod
    def validate_int_input(some_int):
        if some_int >= 0:
            return some_int
        raise ValueError("Positive integer required")
