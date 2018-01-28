import unittest
import sys, os
import unittest.mock as mock

from guoid import Instagram

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def get_id(self, uid):
        s = 0
        for i in uid:
            s += ord(i) 
        return s%17

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(24576, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam2"))
        self.assertEqual(4194324480, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_2(self, time):
        time.return_value = 2
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(8388632576, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(24576, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())
