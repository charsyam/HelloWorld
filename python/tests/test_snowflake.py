import unittest
import sys, os
import unittest.mock as mock

from guoid import SnowFlake

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(4194304000, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_0_and_datacenterid_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guid = SnowFlake(1, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(4194435072, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_0_and_workerid_1(self, time):
        time.return_value = 1
        epoch = 0
        guid = SnowFlake(0, 1, epoch)
        guoidvalue = guid.next()
        self.assertEqual(4194308096, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())

