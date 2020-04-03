import unittest
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import reports
import os
import sys
class Test_TestReports(unittest.TestCase):

    def test_validatereport(self):
        authInfo=auth.AuthInfo()
        ddrmlFile = os.path.join(os.path.dirname(__file__)+"/data/", 'test_ddrml_report.xml')
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            report=reports.Reports(reports.ReportType.DDRML,
            ddrmlFile,
            token)
            result=report.validate()
        except Exception as err:
            self.fail("Failed with error:"+str(err)) 
             
    def test_submitreport(self):
        authInfo=auth.AuthInfo()
        ddrmlFile = os.path.join(os.path.dirname(__file__)+"/data/", 'test_ddrml_report.xml')
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            report=reports.Reports(reports.ReportType.DDRML,
            ddrmlFile,
            token)
            result=report.publish()
        except Exception as err:
            self.fail("Submit failed with error:"+str(err)) 

if __name__ == '__main__':
    unittest.main()