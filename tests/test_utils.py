import unittest
from pirant.utils import MockHttpResponse

class TestUtils(unittest.TestCase):
    def test_happyCaseMockHttpResponse(self):
        test_content = "sample"
        test_status_code = 200
        mockResponse = MockHttpResponse(test_content, test_status_code)
        assert mockResponse.content == test_content
        assert mockResponse.status_code == test_status_code

if __name__ == '__main__':
    unittest.main()
