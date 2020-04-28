import requests 
import os
from enum import Enum
import json

class ReportType(Enum):
    NONE = ""
    DPR10 = "DPR10"
    DPR20 = "DPR20"
    MPRMLGOV = "MPR-GOV"
    MPRMLPARTNER = "MPR-PARTNER"
    DDRML = "DDR-GOV"
  
class Reports:
    """
    Reports class is used to validate and send reports to collabor8
    """
    def __init__(self,
    token:str,subscriptionKey="",validateUrl="",submitUrl=""):
        """
        Inits the reports class with the specified report type,
        
        Parameters
        ----------

        token from authentication,
        subscriptionKey needed for API, if this is not specified tries to load it from environment variable
        validateUrl to use for validation, if this is not specified the code tries to read it from the environment variables
        submitUrl to use for submittal, if this is not specified the code tries to read it from the environment variables
        
        """
        super().__init__()
        self.__token=token 
        if subscriptionKey=="":
            #try reading it from environment variable
            self.__subscriptionKey=os.getenv("AzureSubscriptionKey")
        else:
            self.__subscriptionKey=subscriptionKey
        if validateUrl=="":
            #try reading it from environment variables
            self.__validateUrl=os.getenv('AzureValidateUrl')
        else: 
            self.__validateUrl=validateUrl
        if submitUrl=="":
            #try reading it from environment variables
            self.__submitUrl=os.getenv("AzureSubmitUrl")
        else:
            self.__submitUrl=submitUrl
    
    def validate(self,reportType:ReportType,reportFile:str):
        """Validates the given file and report type against the Collabor8 API and return the
        response from the server as json
        """
        # get the file name and extension
        _, filename = os.path.split(reportFile)
        files = {'file': (filename, open(reportFile, 'rb'), 'application/xml')}
        headers={
            "Authorization":"Bearer "+self.__token,
            "Report-Type":reportType.value,
            "Accept": "application/json",
            "Ocp-Apim-Subscription-Key":self.__subscriptionKey
            }
        #send it
        try:
            response = requests.post(self.__validateUrl, files=files,headers=headers)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except Exception as err:
            raise Exception('Failed in validation of file:'+str(err)+",response:"+str(response.json()))
        return response.json()

    def publish(self,reportType:ReportType,reportFile:str):
        """Publishes the given file and report type against the Collabor8 API and return the
        response from the server as json
        """
        # get the file name and extension
        _, filename = os.path.split(reportFile)
        files = {'file': (filename, open(reportFile, 'rb'), 'application/xml')}
        headers={
            "Authorization":"Bearer "+self.__token,
            "Report-Type":reportType.value,
            "Accept": "application/json",
            "Ocp-Apim-Subscription-Key":self.__subscriptionKey
            }
        #send it
        try:
            response = requests.post(self.__submitUrl, files=files,headers=headers)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except Exception as err:
            raise Exception('Failed in submittal of file:'+str(err)+",response:"+str(response.json()))
        return response.json()    
    
    def map_str_reporttype_to_enum(self,report_type):
        if report_type==ReportType.DDRML.value:
            return ReportType.DDRML
        elif report_type==ReportType.DPR20.value:
            return ReportType.DPR20
        elif report_type==ReportType.MPRMLGOV.value:
            return ReportType.MPRMLGOV
        elif report_type==ReportType.MPRMLPARTNER.value:
            return ReportType.MPRMLPARTNER
        else:
            raise Exception('Unknown report type specified:%s',report_type)

