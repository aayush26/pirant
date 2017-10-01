import unittest
from mock import Mock, patch, PropertyMock
from pirant.handlers import RequestHandler


class TestRequestHandler(unittest.TestCase):

    def setUp(self):
        self.requestHandler = RequestHandler()
        self.sortType = "top"
        self.limit = 1
        self.skip = 0
        self.testJSONResponse = "{\"success\":true,\"rants\":[{\"id\":132,\"text\":\"A .....anyway?!\",\"score\":2192,\"created_time\":1474486614,\"attached_image\":\"\",\"num_comments\":18,\"tags\":[],\"vote_state\":0,\"edited\":true,\"rt\":1,\"user_id\":1098,\"user_username\":\"test\",\"user_score\":402,\"user_avatar\":{\"b\":\"f9966\",\"i\":\"v-17_c-3_b-3_g-m_9-1_5-2_15-1_4-2.jpg\"}}],\"settings\":[],\"set\":\"58cebc\",\"wrw\":71,\"news\":{\"id\":99,\"type\":\"rant\",\"headline\":\"devea m nt!\",\"body\":\"Thi pm \",\"footer\":\"Tap here to learn more\",\"height\":100,\"action\":\"rant-8966\"}}"

    @patch('pirant.handlers.requests.get')
    def test_successfulResponse(self, mockSuccessRequestGet):
        mockSuccessRequestGet.return_value = Mock(ok=True)
        mockSuccessRequestGet.return_value.json.return_value = self.testJSONResponse
        response = self.requestHandler.getRants(self.sortType, self.limit, self.skip)
        self.assertTrue(mockSuccessRequestGet.called)
        self.assertEqual(self.testJSONResponse, response.json())

if __name__ == '__main__':
    unittest.main()
