from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
from subsurfaceCollabor8 import drilling_frames
from subsurfaceCollabor8 import frame_utils
import os 
import unittest


class Test_Drilling(unittest.TestCase):

    def setUp(self):
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            self.token=authObj.authenticate()
        except Exception as err:
            self.fail("Failed in getting token:"+str(err))

    def test_activities(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_activity_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.activities_to_frame(result)
        except Exception as err:
            self.fail("Query drilling activities failed with error:"+str(err)) 

    def test_activities_to_csv(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_activities_result.csv')
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_activity_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.activities_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_csv(normalized_frame,result_file)
            print ("CSV result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling activities failed with error:"+str(err)) 


    def test_activities_to_excel(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_activities_result.xlsx')
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_activity_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.activities_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_excel(normalized_frame,result_file)
            print ("Excel result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling activities failed with error:"+str(err))         

    def test_status_info(self):
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_status_info_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.status_info_to_frame(result)
        except Exception as err:
            self.fail("Query drilling status info failed with error:"+str(err)) 

    def test_status_info_to_csv(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_status_info_result.csv')
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_status_info_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.status_info_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_csv(normalized_frame,result_file)
            print ("CSV result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling status info failed with error:"+str(err)) 
    
    def test_status_info_to_excel(self):
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_status_info_result.xlsx')
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_status_info_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.status_info_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_excel(normalized_frame,result_file)
            print ("Excel result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling status info failed with error:"+str(err))
    
    def test_lithology(self):
        entity="2/4-X-4 A"
        query=queries.get_drilling_lithology_description(entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            drilling_frames.lithology_info_to_frame(result)
        except Exception as err:
            self.fail("Query drilling lithology failed with error:"+str(err)) 
    
    def test_lithology_to_csv(self):
        entity="2/4-X-4 A"
        query=queries.get_drilling_lithology_description(entity)
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_lithology_result.xlsx')
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.lithology_info_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_excel(normalized_frame,result_file)
            print ("Excel result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling lithology failed with error:"+str(err)) 
    
    def test_lithology_to_excel(self):
        entity="2/4-X-4 A"
        query=queries.get_drilling_lithology_description(entity)
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_lithology_result.csv')
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.lithology_info_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_csv(normalized_frame,result_file)
            print ("CSV result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling lithology failed with error:"+str(err)) 
    

if __name__ == "__main__":
    unittest.main()