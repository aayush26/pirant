from __future__ import absolute_import, division, print_function
from builtins import object

class MockHttpResponse(object):
    """
    Test Util: mocks response
    """
    # TODO Move this to helpers under tests directory
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code
