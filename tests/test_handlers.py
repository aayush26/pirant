from __future__ import absolute_import, division, print_function
import unittest
try:
    from mock import patch, Mock
except ImportError:
    from unittest.mock import patch, Mock

from pirant.handlers import RequestHandler, ResponseHandler
import json
from pirant.utils import MockHttpResponse


class TestRequestHandler(unittest.TestCase):
    """
    Unit tests for RequestHandler class
    """

    def setUp(self):
        self.requestHandler = RequestHandler()

    @patch('pirant.handlers.requests.get')
    def test_successful_get_rants_response(self, mock_success_get_rants_request):
        sortType = "top"
        limit = 1
        skip = 0
        testJSONResponse = "{\"success\":true,\"rants\":[{\"id\":132,\"text\":\"A .....anyway?!\",\"score\":2192,\"created_time\":1474486614,\"attached_image\":\"\",\"num_comments\":18,\"tags\":[],\"vote_state\":0,\"edited\":true,\"rt\":1,\"user_id\":1098,\"user_username\":\"test\",\"user_score\":402,\"user_avatar\":{\"b\":\"f9966\",\"i\":\"v-17_c-3_b-3_g-m_9-1_5-2_15-1_4-2.jpg\"}}],\"settings\":[],\"set\":\"58cebc\",\"wrw\":71,\"news\":{\"id\":99,\"type\":\"rant\",\"headline\":\"devea m nt!\",\"body\":\"Thi pm \",\"footer\":\"Tap here to learn more\",\"height\":100,\"action\":\"rant-8966\"}}"
        mock_success_get_rants_request.return_value = Mock(ok=True)
        mock_success_get_rants_request.return_value.json.return_value = testJSONResponse
        response = self.requestHandler.get_rants(sortType, limit, skip)
        self.assertTrue(mock_success_get_rants_request.called)
        self.assertEqual(testJSONResponse, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successful_get_rant_by_id_response(self, mock_success_get_rant_by_id_request):
        rantId = 1
        testJSONResponse = "{\"rant\": {\"id\": 1234,\"text\": \"Txt\",\"score\": 111,\"created_time\": 234432,\"user_id\": 43289,\"num_comments\": 121,\"user_username\": \"user\"},\"comments\": [{\"id\": 1234,\"rant_id\": 2345,\"body\": \"test body\",\"upvotes\": 2,\"downvotes\": 1,\"score\": 10,\"created_time\": 20102313123,\"user_id\": 111,\"user_username\": \"testUser\",\"user_userscore\": 56}],\"success\": True}"
        mock_success_get_rant_by_id_request.return_value = Mock(ok=True)
        mock_success_get_rant_by_id_request.return_value.json.return_value = testJSONResponse
        response = self.requestHandler.get_rant_by_id(rantId)
        self.assertTrue(mock_success_get_rant_by_id_request.called)
        self.assertEqual(testJSONResponse, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successful_get_weekly_rants(self, mock_success_get_weekly_rant_request):
        sort_type = "top"
        skip = 0
        test_json_response = "{\"rant\": {\"id\": 1234,\"text\": \"Txt\",\"score\": 111,\"created_time\": 234432,\"user_id\": 43289,\"num_comments\": 121,\"user_username\": \"user\"},\"comments\": [{\"id\": 1234,\"rant_id\": 2345,\"body\": \"test body\",\"upvotes\": 2,\"downvotes\": 1,\"score\": 10,\"created_time\": 20102313123,\"user_id\": 111,\"user_username\": \"testUser\",\"user_userscore\": 56}],\"success\": True}"
        mock_success_get_weekly_rant_request.return_value = Mock(ok=True)
        mock_success_get_weekly_rant_request.return_value.json.return_value = test_json_response
        response = self.requestHandler.get_weekly_rants(sort_type, skip)
        self.assertTrue(mock_success_get_weekly_rant_request.called)
        self.assertEqual(test_json_response, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successful_search_rants_by_keyword(self, mock_success_search_rants_by_keyword):
        test_keyword = "test"
        test_json_response = "{\"success\": true,\"results\": [{\"id\": 173,\"text\": \"Random Text 1\",\"score\": 241,\"created_time\": 14707,\"attached_image\": \"\",\"num_comments\": 5,\"tags\": [],\"vote_state\": 0,\"edited\": false,\"rt\": 1,\"rc\": 1,\"user_id\": 473,\"user_username\": \"dt\",\"user_score\": 3,\"user_avatar\": {\"b\": \"2b9d\",\"i\": \"v-175_4-2.jpg\"}}, {\"id\": 5878,\"text\": \"Random text 2\",\"score\": 238,\"created_time\": 1492513,\"attached_image\": {\"url\": \"https://sample.url\",\"width\": 800,\"height\": 516},\"num_comments\": 13,\"tags\": [\"family\", \"tech support\", \"won't fix your computer\"],\"vote_state\": 0,\"edited\": false,\"rt\": 1,\"rc\": 1,\"user_id\": 5458,\"user_username\": \"ded\",\"user_score\": 327,\"user_avatar\": {\"b\": \"2a8b9d\",\"i\": \"v-17_c-3_b-_19-1.jpg\"}}]}"
        mock_success_search_rants_by_keyword.return_value = Mock(ok=True)
        mock_success_search_rants_by_keyword.return_value.json.return_value = test_json_response
        response = self.requestHandler.search_rants_by_keyword(test_keyword)
        self.assertTrue(mock_success_search_rants_by_keyword.called)
        self.assertEqual(test_json_response, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successful_get_collabs(self, mock_success_get_collabs):
        test_skip = 0
        test_limit = 1
        test_json_response = "{\"success\":true,\"rants\":[{\"id\":435,\"text\":\"Test Text\",\"score\":5,\"created_time\":15072,\"attached_image\":\"\",\"num_comments\":3,\"tags\":[],\"vote_state\":0,\"edited\":false,\"link\":\"collabs\/913738\/sample-link\",\"rt\":2,\"rc\":2,\"c_type\":3,\"c_type_long\":\"Project idea\",\"user_id\":9856,\"user_username\":\"testuser\",\"user_score\":14,\"user_avatar\":{\"b\":\"b9d\",\"i\":\"v-10-1_2-10_15-11_4-1.jpg\"}}]}"
        mock_success_get_collabs.return_value = Mock(ok=True)
        mock_success_get_collabs.return_value.json.return_value = test_json_response
        response = self.requestHandler.get_collabs(test_skip, test_limit)
        self.assertTrue(mock_success_get_collabs.called)
        self.assertEqual(test_json_response, response.json())

class TestResponseHandler(unittest.TestCase):
    """
    Unit tests for ResponseHandler class
    """
    def setUp(self):
        self.responseHandler = ResponseHandler()

    # TODO Write a test data provider factory to get test data eg. test_content which are used in multiple places
    def test_successful_get_rants_build_response(self):
        test_content = {
            'rants': [{
                    'id': 1234,
                    'text': 'Txt',
                    'score': 111,
                    'created_time': 234432,
                    'user_id': 43289,
                    'num_comments': 121,
                    'user_username': 'user'
            }],
            'news': {
                'id': 123,
                'type': 'T',
                'headline': 'MyHeadline',
                'body': 'MyBody',
                'footer': 'MyFooter',
                'height': 456,
                'action': 'MyAction'
            },
            'success': True,
            'set': '1',
            'wrw': 1
        }
        test_content = json.dumps(test_content)
        test_status_code = 200
        mockResponse = MockHttpResponse(test_content, test_status_code)
        rants = self.responseHandler.get_rants_build_response(mockResponse)
        assert rants['rants'][0]['id'] == 1234

    def test_successful_get_rant_by_id_build_response(self):
        test_content = {
            'rant': {
                'id': 1234,
                'text': 'Txt',
                'score': 111,
                'created_time': 234432,
                'user_id': 43289,
                'num_comments': 121,
                'user_username': 'user'
            },
            'comments': [{
                'id': 1234,
                'rant_id': 2345,
                'body': 'test body',
                'upvotes': 2,
                'downvotes': 1,
                'score': 10,
                'created_time': 20102313123,
                'user_id': 111,
                'user_username': 'testUser',
                'user_userscore': 56
            }],
            'success': True
        }
        test_content = json.dumps(test_content)
        test_status_code = 200
        mockResponse = MockHttpResponse(test_content, test_status_code)
        rant = self.responseHandler.get_rant_by_id_build_response(mockResponse)
        assert rant['rant']['id'] == 1234
        assert rant['comments'][0]['upvotes'] == 2

    def test_successful_search_rants_by_keyword_build_response(self):
        test_content = {
            "success": True,
            "results": [{
                "id": 173,
                "text": "Random Text 1",
                "score": 241,
                "created_time": 14707,
                "attached_image": "",
                "num_comments": 5,
                "tags": [],
                "vote_state": 0,
                "edited": False,
                "rt": 1,
                "rc": 1,
                "user_id": 473,
                "user_username": "dt",
                "user_score": 3,
                "user_avatar": {
                    "b": "2b9d",
                    "i": "v-175_4-2.jpg"
                }
            }, {
                "id": 5878,
                "text": "Random text 2",
                "score": 238,
                "created_time": 1492513,
                "attached_image": {
                    "url": "https://sample.url",
                    "width": 800,
                    "height": 516
                },
                "num_comments": 13,
                "tags": ["family", "tech support", "won't fix your computer"],
                "vote_state": 0,
                "edited": False,
                "rt": 1,
                "rc": 1,
                "user_id": 5458,
                "user_username": "ded",
                "user_score": 327,
                "user_avatar": {
                    "b": "2a8b9d",
                    "i": "v-17_c-3_b-_19-1.jpg"
                }
            }]
        }
        test_content = json.dumps(test_content)
        test_status_code = 200
        mockResponse = MockHttpResponse(test_content, test_status_code)
        searchResults = self.responseHandler.search_rants_by_keyword_build_response(mockResponse)
        assert searchResults['results'][0]['id'] == 173
        assert searchResults['success'] == True
