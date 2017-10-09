import unittest
from pirant import DevRant
from mock import patch
import json
from pirant.utils import MockHttpResponse

class TestApp(unittest.TestCase):
    def setUp(self):
        self.devrant = DevRant()

    @patch('pirant.handlers.RequestHandler.get_rants')
    def test_happyCaseGetRants(self, mock_get_rants_response):
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
        mock_response = MockHttpResponse(test_content, 200)
        mock_get_rants_response.return_value = mock_response
        rants = self.devrant.get_rants("top",1,0)
        self.assertTrue(mock_get_rants_response.called)
        self.assertEqual(rants['rants'][0]['text'], 'Txt')

    @patch('pirant.handlers.RequestHandler.get_rant_by_id')
    def test_happyCaseGetRantById(self, mock_get_rant_by_id_response):
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
        mock_response = MockHttpResponse(test_content, test_status_code)
        mock_get_rant_by_id_response.return_value = mock_response
        rant = self.devrant.get_rant_by_id(2)
        self.assertTrue(mock_get_rant_by_id_response.called)
        assert rant['rant']['id'] == 1234
        assert rant['comments'][0]['upvotes'] == 2

    @patch('pirant.handlers.RequestHandler.get_weekly_rants')
    def test_happy_case_get_weekly_rants(self, mock_get_weekly_rants_response):
        test_content = {
                "success": True,
                "rants": [
                    {
                        "id": 890185,
                        "text": "Pixel 2 design looks like shit.",
                        "score": 1,
                        "created_time": 1507147639,
                        "attached_image": "",
                        "num_comments": 3,
                        "tags": [
                            "wk72"
                        ],
                        "vote_state": 0,
                        "edited": False,
                        "rt": 1,
                        "rc": 1,
                        "user_id": 80000,
                        "user_username": "1234abcd",
                        "user_score": 366,
                        "user_avatar": {
                            "b": "69c9cd",
                            "i": "v-17_c-3_b-6_g-m_9-1_1-6_16-1_3-2_8-1_7-1_5-1_12-6_6-14_2-3_15-14_11-1_4-1.jpg"
                        }
                    },
                ],
                "settings": [

                ],
                "wrw": 72,
                "news": {
                    "id": 0,
                    "type": "weekly",
                    "headline": "Worst code review experience?",
                    "footer": "Week 72 Group Rant - Add tag 'wk72' to your rant",
                    "height": 65,
                    "action": "none"
                }
            }
        test_content = json.dumps(test_content)
        test_status_code = 200
        mock_reponse = MockHttpResponse(test_content, test_status_code)
        mock_get_weekly_rants_response.return_value = mock_reponse
        rant = self.devrant.get_weekly_rants("algo", 2)
        self.assertTrue(mock_get_weekly_rants_response.called)
        assert rant['rants'][0]['id'] == 890185

    @patch('pirant.handlers.RequestHandler.search_rants_by_keyword')
    def test_happy_case_search_rants_by_keyword(self, mock_search_rants_by_keyword_response):
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
        test_keyword = "test"
        mock_reponse = MockHttpResponse(test_content, test_status_code)
        mock_search_rants_by_keyword_response.return_value = mock_reponse
        searchResults = self.devrant.search_rants_by_keyword(test_keyword)
        self.assertTrue(mock_search_rants_by_keyword_response.called)
        assert searchResults['success'] == True

    if __name__ == '__main__':
        unittest.main()
