import unittest
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
import json

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
    
    

    
    def test_query_field_name(self):
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
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            query_obj=graph.Graph(token)
            result=query_obj.query(test_query)
            print ('result field:'+str(result))
        except Exception as err:
            self.fail("Query failed with error:"+str(err)) 




if __name__ == '__main__':
    unittest.main()


