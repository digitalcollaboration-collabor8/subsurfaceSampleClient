import unittest
from subsurfaceCollabor8 import auth
import json
import logging
class Test_TestAuthentication(unittest.TestCase):
    def test_authinfo(self):
        clientId="clientId"
        clientSecret="clientSecret"
        tokenUrl="tokenUrl"
        resourceId="resourceId"
        subscriptionKey="subscriptionKey"
        authObj=auth.AuthInfo(clientId,clientSecret,tokenUrl,resourceId,subscriptionKey)
        self.assertEqual(authObj.clientId,clientId)
        self.assertEqual(authObj.clientSecret,clientSecret)
        self.assertEqual(authObj.tokenUrl,tokenUrl)
        self.assertEqual(authObj.resourceId,resourceId)
        self.assertEqual(authObj.subscriptionKey,subscriptionKey)      
    
    def test_authenticate_fail_missing_authinfo(self):
        logging.disable(logging.CRITICAL) #disable error logging for this case as it should fail
        clientId="clientId"
        clientSecret="clientSecret"
        tokenUrl="tokenUrl"
        resourceId="resourceId"
        subscriptionKey="subscriptionKey"
        authObj=auth.AuthInfo(clientId,clientSecret,
        tokenUrl,resourceId,subscriptionKey)
        authObj=auth.Authenticate(authObj) 
        try:
            authObj.authenticate()
            self.fail('Expected an exception but got data...')
        except Exception as err:
            self.assertEqual(1,1) 


    

    def test_auth_from_env_variable(self):
        authInfo=auth.AuthInfo() 
        authInfo.init_from_env_vars()
        authObj=auth.Authenticate(authInfo) 
        try:
             token=authObj.authenticate()
            
        except Exception as err:
            self.fail('Expected not an exception but got it'+str(err))
       
        
        

if __name__ == '__main__':
    unittest.main()


