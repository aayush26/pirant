import unittest

from pirant.utils.UrlBuilder import URLBuilder


class UrlBuilderTest(unittest.TestCase):

    def setUp(self):
        self.URLBuilder = URLBuilder()
        self.test_sort = "top"
        self.test_limit = 10
        self.test_skip = 0

    def test_happyCaseGetRantUrl(self):
        test_devRantURL = "https://www.devrant.io/api/devrant/rants?sort=top&limit=10&skip=0&app=3"
        devRantURL = self.URLBuilder.getRantURL(self.test_sort, self.test_limit, self.test_skip)
        self.assertEqual(test_devRantURL, devRantURL)

    def test_invalidSortType(self):
        test_sort = "dummy_sort"
        with self.assertRaises(ValueError):
            self.URLBuilder.getRantURL(test_sort, self.test_limit, self.test_skip)

    def test_invalidLimitValue(self):
        test_limit = -1
        test_devRantURL = "https://www.devrant.io/api/devrant/rants?sort=top&limit=15&skip=0&app=3"
        devRantURL = self.URLBuilder.getRantURL(self.test_sort, test_limit, self.test_skip)
        self.assertEqual(test_devRantURL, devRantURL)
        test_limit = 101
        devRantURL = self.URLBuilder.getRantURL(self.test_sort, test_limit, self.test_skip)
        self.assertEqual(test_devRantURL, devRantURL)


if __name__ == '__main__':
    unittest.main()
