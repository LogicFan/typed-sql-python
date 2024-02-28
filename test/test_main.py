from typed_sql import main
import unittest


class MainTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)
