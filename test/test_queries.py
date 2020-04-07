
import unittest
from subsurfaceCollabor8 import queries


class Test_TestQueries(unittest.TestCase):

    def test_drilling_activity(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        result=queries.get_drilling_activity_query(start,
        end,entity)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        

if __name__ == "__main__":
    unittest.main()