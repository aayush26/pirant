class URLBuilder:
    def __init__(self):
        self.APP_VERSION = 3
        self.BASE_URL = "https://www.devrant.io/api"
        self.RANTS_URL = "%s/devrant/rants?sort=%s&limit=%d&skip=%d&app=%d"
        self.SORT_TOP = "top"
        self.SORT_ALGO = "algo"
        self.SORT_RECENT = "recent"
        self.VALID_SORTS = [self.SORT_ALGO, self.SORT_RECENT, self.SORT_TOP]

    def getRantURL(self, sort, limit, skip):
        if sort == "":
            sort = "top"
        elif sort not in self.VALID_SORTS:
            raise ValueError("Invalid Sort type")
        if limit <= 0 or limit > 100:
            limit = 15
        return str(self.RANTS_URL % (self.BASE_URL, sort, limit, skip, self.APP_VERSION))
