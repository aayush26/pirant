"""Utility classes for testing."""
from __future__ import absolute_import, division, print_function

# pylint: disable=too-few-public-methods,fixme


class MockHttpResponse(object):
    """Test Util: mocks response."""

    # TODO Move this to helpers under tests directory
    def __init__(self, content, status_code):
        """Initialize mock instance."""
        self.content = content
        self.status_code = status_code
