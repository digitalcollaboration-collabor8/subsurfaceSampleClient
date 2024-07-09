from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import metadata
import logging
import os 
import unittest
import sys
logger = logging.getLogger()
logger.level = logging.DEBUG

class Test_Metadata(unittest.TestCase):

    def setUp(self):
        
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            self.token=authObj.authenticate()
        except Exception as err:
            self.fail("Failed in getting token:"+str(err)) 
    

    def test_get_entity_names(self):
       
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        metaData=metadata.MetaData(self.token)
        entities=metaData.get_data_entities_for_field("FENJA")
        if len(entities)==0:
            self.fail("No entities found")
        #generate the query string
        names=""
        i=0
        for entity in entities:
            if i==0:
                names=names+'"'+entity+'"'
            else:
                names=names+',"'+entity+'"'
            i=i+1
        logging.debug("names:%s",names)