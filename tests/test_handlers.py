import unittest
from mock import Mock, patch
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
    def test_successfulGetRantsResponse(self, mockSuccessGetRantsRequest):
        sortType = "top"
        limit = 1
        skip = 0
        testJSONResponse = "{\"success\":true,\"rants\":[{\"id\":132,\"text\":\"A .....anyway?!\",\"score\":2192,\"created_time\":1474486614,\"attached_image\":\"\",\"num_comments\":18,\"tags\":[],\"vote_state\":0,\"edited\":true,\"rt\":1,\"user_id\":1098,\"user_username\":\"test\",\"user_score\":402,\"user_avatar\":{\"b\":\"f9966\",\"i\":\"v-17_c-3_b-3_g-m_9-1_5-2_15-1_4-2.jpg\"}}],\"settings\":[],\"set\":\"58cebc\",\"wrw\":71,\"news\":{\"id\":99,\"type\":\"rant\",\"headline\":\"devea m nt!\",\"body\":\"Thi pm \",\"footer\":\"Tap here to learn more\",\"height\":100,\"action\":\"rant-8966\"}}"
        mockSuccessGetRantsRequest.return_value = Mock(ok=True)
        mockSuccessGetRantsRequest.return_value.json.return_value = testJSONResponse
        response = self.requestHandler.get_rants(sortType, limit, skip)
        self.assertTrue(mockSuccessGetRantsRequest.called)
        self.assertEqual(testJSONResponse, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successfulGetRantByIdResponse(self, mockSuccessGetRantByIdRequest):
        rantId = 1
        testJSONResponse = "{\"rant\": {\"id\": 1234,\"text\": \"Txt\",\"score\": 111,\"created_time\": 234432,\"user_id\": 43289,\"num_comments\": 121,\"user_username\": \"user\"},\"comments\": [{\"id\": 1234,\"rant_id\": 2345,\"body\": \"test body\",\"upvotes\": 2,\"downvotes\": 1,\"score\": 10,\"created_time\": 20102313123,\"user_id\": 111,\"user_username\": \"testUser\",\"user_userscore\": 56}],\"success\": True}"
        mockSuccessGetRantByIdRequest.return_value = Mock(ok=True)
        mockSuccessGetRantByIdRequest.return_value.json.return_value = testJSONResponse
        response = self.requestHandler.get_rant_by_id(rantId)
        self.assertTrue(mockSuccessGetRantByIdRequest.called)
        self.assertEqual(testJSONResponse, response.json())

    @patch('pirant.handlers.requests.get')
    def test_successful_get_weekly_rants(self, mockSuccessGetRantByIdRequest):
        sort_type = "top"
        skip = 0
        test_json_response = "{\"rant\": {\"id\": 1234,\"text\": \"Txt\",\"score\": 111,\"created_time\": 234432,\"user_id\": 43289,\"num_comments\": 121,\"user_username\": \"user\"},\"comments\": [{\"id\": 1234,\"rant_id\": 2345,\"body\": \"test body\",\"upvotes\": 2,\"downvotes\": 1,\"score\": 10,\"created_time\": 20102313123,\"user_id\": 111,\"user_username\": \"testUser\",\"user_userscore\": 56}],\"success\": True}"
        mockSuccessGetRantByIdRequest.return_value = Mock(ok=True)
        mockSuccessGetRantByIdRequest.return_value.json.return_value = test_json_response
        response = self.requestHandler.get_weekly_rants(sort_type, skip)
        self.assertTrue(mockSuccessGetRantByIdRequest.called)
        self.assertEqual(test_json_response, response.json())

class TestResponseHandler(unittest.TestCase):
    """
    Unit tests for ResponseHandler class
    """
    def setUp(self):
        self.responseHandler = ResponseHandler()

    # TODO Write a test data provider factory to get test data eg. test_content which are used in multiple places
    def test_successfulGetRantsBuildResponse(self):
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

    def test_successfulGetRantByIdBuildResponse(self):
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
