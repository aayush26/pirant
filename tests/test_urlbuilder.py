from __future__ import absolute_import, division, print_function
import unittest

from pirant.urlbuilder import URLBuilder


class UrlBuilderTest(unittest.TestCase):

    def setUp(self):
        self.url_builder = URLBuilder()
        self.test_sort = "top"
        self.test_limit = 10
        self.test_skip = 1

    def test_happy_case_get_rant_url(self):
        expected_url = "https://www.devrant.com/api/devrant/rants?sort=top&limit=10&skip=1&app=3"
        obtained_url = self.url_builder.get_rant_url(self.test_sort, self.test_limit, self.test_skip)
        self.assertEqual(expected_url, obtained_url)

    def test_empty_sort_type_get_rant_url(self):
        test_devrant_url = "https://www.devrant.com/api/devrant/rants?sort=top&limit=10&skip=1&app=3"
        devrant_url = self.url_builder.get_rant_url("", self.test_limit, self.test_skip)
        self.assertEqual(test_devrant_url, devrant_url)

    def test_invalid_sort_type_get_rant_url(self):
        test_sort = "dummy_sort"
        with self.assertRaises(ValueError):
            self.url_builder.get_rant_url(test_sort, self.test_limit, self.test_skip)

    def test_invalid_limit_value_get_rant_url(self):
        test_limit = -1
        with self.assertRaises(ValueError):
            self.url_builder.get_rant_url(self.test_sort, test_limit, self.test_skip)

    def test_happy_case_get_rant_by_id_url(self):
        test_devrant_url = "https://www.devrant.com/api/devrant/rants/2?app=3"
        test_rant_id = 2
        devrant_url = self.url_builder.get_rant_by_id_url(test_rant_id)
        self.assertEqual(test_devrant_url, devrant_url)

    def test_id_must_be_int_get_rant_by_id_url(self):
        test_rant_id = '2'
        with self.assertRaises(TypeError):
            self.url_builder.get_rant_by_id_url(test_rant_id)

    def test_idMustBeIntGetRantByIdUrl(self):
        test_rant_id = '2'
        with self.assertRaises(TypeError):
            self.url_builder.get_rant_by_id_url(test_rant_id)


if __name__ == '__main__':
    unittest.main()
