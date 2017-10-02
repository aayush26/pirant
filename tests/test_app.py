import unittest
from pirant import DevRant
from mock import patch
import json
from pirant.utils import MockHttpResponse

class TestApp(unittest.TestCase):
    def setUp(self):
        self.devrant = DevRant()

    @patch('pirant.handlers.RequestHandler.getRants')
    def test_happyCaseGetRants(self, mockGetRantsresponse):
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
        mockResponse = MockHttpResponse(test_content, 200)
        mockGetRantsresponse.return_value = mockResponse
        rants = self.devrant.getRants("top",1,0)
        self.assertTrue(mockGetRantsresponse.called)
        self.assertEqual(rants['rants'][0]['text'], 'Txt')

    @patch('pirant.handlers.RequestHandler.getRantById')
    def test_happyCaseGetRantById(self, mockGetRantByIdResponse):
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
        mockGetRantByIdResponse.return_value = mockResponse
        rant = self.devrant.getRantById(2)
        self.assertTrue(mockGetRantByIdResponse.called)
        assert rant['rant']['id'] == 1234
        assert rant['comments'][0]['upvotes'] == 2

if __name__ == '__main__':
    unittest.main()
