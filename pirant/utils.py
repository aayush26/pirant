class MockHttpResponse:
    """
    Test Util: mocks response
    """
    # TODO Move this to helpers under tests directory
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code