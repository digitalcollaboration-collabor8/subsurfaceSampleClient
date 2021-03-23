from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
from subsurfaceCollabor8 import production_frames
#from subsurfaceCollabor8 import production
from subsurfaceCollabor8 import frame_utils
import os 
import unittest

class TestProductionFromConfig(unittest.TestCase):


    def setUp(self):

        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_config_file('./test/config_auth.json')
            authObj=auth.Authenticate(authInfo) 
            self.token=authObj.authenticate()
            self.subscriptionKey=authInfo.subscriptionKey
            self.graphUrl=authInfo.graphUrl
        except Exception as err:
            self.fail("Failed in getting token:"+str(err)) 

    def test_production_volumes_to_excel(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'production_volumes_result_from_config.xlsx')
        start="2021-03-18"
        end="2021-03-20"
        entity="ALVE"
        volume_type='"Production","Injection","Consumption","Comments"'
        query=queries.get_production_volumes(start,end,entity,volume_type)
        
        try: 
            query_obj=graph.Graph(self.token,self.subscriptionKey,self.graphUrl)
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