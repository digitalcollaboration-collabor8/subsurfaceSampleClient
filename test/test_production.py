from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
from subsurfaceCollabor8 import production_frames
from subsurfaceCollabor8 import production
from subsurfaceCollabor8 import frame_utils
import os 
import unittest

class Test_Production(unittest.TestCase):

    def setUp(self):

        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            self.token=authObj.authenticate()
        except Exception as err:
            self.fail("Failed in getting token:"+str(err)) 
    
    def test_production_volumes(self):
        start="2017-10-31T23:00:00.000Z"
        end="2017-11-20T12:00:00.000Z"
        entity="34/10-A-23"
        volume_type="Production"
        query=queries.get_production_volumes(start,end,entity,volume_type)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            production_frames.production_volumes_to_frame(result)
        except Exception as err:
            self.fail("Query production volumes failed with error:"+str(err)) 
    
    def test_production_volumes_to_csv(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'production_volumes_result.csv')
        start="2017-10-31T23:00:00.000Z"
        end="2017-11-20T12:00:00.000Z"
        entity="34/10-A-23"
        volume_type="Production"
        query=queries.get_production_volumes(start,end,entity,volume_type)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=production_frames.production_volumes_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_csv(normalized_frame,result_file)
            print ("CSV result written to:"+result_file)
        except Exception as err:
            self.fail("Query production volumes failed with error:"+str(err)) 

    def test_production_volumes_to_excel(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'production_volumes_result.xlsx')
        start="2017-10-31T23:00:00.000Z"
        end="2017-11-20T12:00:00.000Z"
        entity="34/10-A-23"
        volume_type="Production"
        query=queries.get_production_volumes(start,end,entity,volume_type)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=production_frames.production_volumes_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_excel(normalized_frame,result_file)
            print ("Excel result written to:"+result_file)
        except Exception as err:
            self.fail("Query production volumes failed with error:"+str(err))         
    
    

if __name__ == "__main__":
    unittest.main()