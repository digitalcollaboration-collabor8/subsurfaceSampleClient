import unittest
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
import json
import os
class Test_Graph(unittest.TestCase):

    def test_query_facility_id(self):
        test_query='''query{
        metadata {
            facilities(referenceId:"18116481"){
                name
                id
                created
                createdBy
                referenceId
                code
                type
                aliases {
                    name
                    code
                    description
                }
            }
        
        }
    }'''
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            query_obj=graph.Graph(token)
            result=query_obj.query(test_query)
            print ('result:'+str(result))
        except Exception as err:
            self.fail("Query failed with error:"+str(err)) 
    
    

    
    def test_query_field_name_to_file(self):
        test_query='''query{
                metadata {
                    fields(name:"OSEBERG"){
                        name
                        id
                        status
                        created
                        createdBy
                        validFrom
                        validTo
                        description
                        code 
                        country
                        referenceId
                        license {
                            name

                        }
                        wells{
                            name
                            referenceId
                        
                            
                        }
                        platforms {
                            name
                            referenceId
                        }
                    
                        wellbores{
                            name
                            referenceId
                        }
                    
                    }
                    
                }
                
            }'''
        authInfo=auth.AuthInfo()
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'field_result.json')
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            query_obj=graph.Graph(token)
            query_obj.query_to_file(test_query,result_file)
        except Exception as err:
            self.fail("Query failed with error:"+str(err)) 
    
    def test_query_drilling_activities(self):
        query='''
        query {
  drilling {
    drillingActivity(
      limit: 1000
      period_after: "2020-03-21T23:00:00.000Z"
      period_before: "2020-03-26T12:00:00.000Z"
    ) {
      created
      modified
      endTime
      startTime
      dataStartTime
      dataEndTime
      dataEntity {
        name
        type
      }
     conveyance
     state
     stateDetailActivity
     phase
     proprietaryCode
     comment
    
     
   
  }
  }
}
        '''
        authInfo=auth.AuthInfo()
        result_file = os.path.join(os.path.dirname(__file__)+"/data/", 'drilling_activities_result.json')
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            query_obj=graph.Graph(token)
            query_obj.query_to_file(query,result_file)
        except Exception as err:
            self.fail("Query failed with error:"+str(err)) 


if __name__ == '__main__':
    unittest.main()


