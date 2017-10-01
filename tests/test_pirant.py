import unittest

from pirant import DevRant


class DevRantTest(unittest.TestCase):
    def setUp(self):
        self.devRant = DevRant()

    def test_getRant(self):
        # TODO: implement real unit tests
        print(self.devRant.getRants('top', 1, 0))
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
