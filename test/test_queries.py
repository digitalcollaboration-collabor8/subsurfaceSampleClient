
import unittest
from subsurfaceCollabor8 import queries
import sys
from subsurfaceCollabor8 import production_frames
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
    
    def test_lithology(self):
        entity="34/4-M-4 H"
        result=queries.get_drilling_lithology_description(entity)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
    
    def test_get_production_volums(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        result=queries.get_production_volumes(start,
        end,entity,volume_type)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
    

    def test_get_production_volums_with_product(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        result=queries.get_production_volumes_regex(start,
        end,entity,volume_type,'oil')
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
        if not 'oil' in result:
            self.fail("Couldn't find product:oil in string:"+result)
    
    def test_get_production_volums_with_empty_reportypes(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        reportType=""
        result=queries.get_production_volumes_regex(start,
        end,entity,volume_type,'oil',reportType)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
        if not 'oil' in result:
            self.fail("Couldn't find product:oil in string:"+result)
        if 'source_system_names: ["DPR"]' in result:
            self.fail('Found report type: DPR which should not be there')
    
    def test_get_production_volums_with_reportypes(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        reportType="DPR"
        result=queries.get_production_volumes_regex(start,
        end,entity,volume_type,'oil',reportType)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
        if not 'oil' in result:
            self.fail("Couldn't find product:oil in string:"+result)
        if not 'source_system_names: ["DPR"]' in result:
            self.fail('Did not fint report type: DPR which shouldbe there')
    

    def test_get_production_volums_with_addfilter_and_reporttype(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        reportType="DPR"
        addFilter='data_periods:["day"]'
        result=queries.get_production_volumes_regex(start,
        end,entity,volume_type,'oil',reportType,addFilter)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
        if not 'oil' in result:
            self.fail("Couldn't find product:oil in string:"+result)
        if not 'source_system_names: ["DPR"]' in result:
            self.fail('Did not find report type: DPR which should be there')
        if not 'data_periods:["day"]' in result:
            self.fail('Did not find additional filter data_periods:["day"] in result')
    
    def test_get_production_volums_with_addfilter_and_noreporttype(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="GINA KROG"
        volume_type="Production"
        addFilter='data_periods:["day"]'
        result=queries.get_production_volumes_regex(start,
        end,entity,volume_type,'oil','',addFilter)
        if not start in result:
            self.fail("Couldn't find start:"+start+"in string:"+result)
        if not end in result:
            self.fail("Couldn't find en:"+end+"in string:"+result)
        if not entity in result:
            self.fail("Couldn't find entity:"+entity+"in string:"+result)
        if not volume_type in result:
            self.fail("Couldn't find volume_type:"+volume_type+"in string:"+result)
        if not 'oil' in result:
            self.fail("Couldn't find product:oil in string:"+result)
        if not 'data_periods:["day"]' in result:
            self.fail('Did not find additional filter data_periods:["day"] in result')
        if 'source_system_names: ["DPR"]' in result:
            self.fail('Found source system names in result which should not be there')
        
    
        

        

if __name__ == "__main__":
    unittest.main()