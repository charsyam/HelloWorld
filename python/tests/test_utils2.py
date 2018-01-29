import unittest
import sys, os

from guoid import utils2

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_1_1(self):
        self.assertEqual(2, utils2.add(1,1))
    
    def test_add_1_2_fail(self):
        self.assertEqual(3, utils2.add(1,2))

if __name__=="__main__":
    sys.exit(unittest.main())
