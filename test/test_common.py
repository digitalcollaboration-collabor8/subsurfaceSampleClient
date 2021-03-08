import unittest
from subsurfaceCollabor8 import common_utils as common
import datetime

class Test_CommonUtils(unittest.TestCase):

    def test_date_format(self):
        x = datetime.datetime(2018, 9, 15)
        formatted=common.format_date_to_yy_mm_dd(x)
        self.assertEqual(formatted,'2018-09-15')

    def test_substracts_days(self):
        x = datetime.datetime(2018, 9, 15)
        substracted=common.substract_days(x,5)
        self.assertEqual(common.format_date_to_yy_mm_dd(substracted),'2018-09-10')


if __name__ == '__main__':
    unittest.main()
