import os
import sys
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from pirant import DevRant

class DevRantTest(unittest.TestCase):
    def setUp(self):
        self.devRant = DevRant()

    def test_getRant(self):
        print self.devRant.getRant()
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
