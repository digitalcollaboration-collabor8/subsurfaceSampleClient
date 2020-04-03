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
    def __init__(self,reportType:ReportType,fileName:str,
    token:str,subscriptionKey="",validateUrl="",submitUrl=""):
        """
        Inits the reports class with the specified report type,
        fileName path to the file to send,
        token from authentication,
        subscriptionKey needed for API, if this is not specified tries to load it from environment variable
        validateUrl to use for validation, if this is not specified the code tries to read it from the environment variables
        submitUrl to use for submittal, if this is not specified the code tries to read it from the environment variables
        """
        super().__init__()
        self.reportType=reportType
        self.__file=fileName
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
    
    def validate(self):
        """Validates the given file and report type against the Collabor8 API and return the
        response from the server as json
        """
        # get the file name and extension
        _, filename = os.path.split(self.__file)
        files = {'file': (filename, open(self.__file, 'rb'), 'application/xml')}
        headers={
            "Authorization":"Bearer "+self.__token,
            "Report-Type":self.reportType.value,
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

    def publish(self):
        """Publishes the given file and report type against the Collabor8 API and return the
        response from the server as json
        """
        # get the file name and extension
        _, filename = os.path.split(self.__file)
        files = {'file': (filename, open(self.__file, 'rb'), 'application/xml')}
        headers={
            "Authorization":"Bearer "+self.__token,
            "Report-Type":self.reportType.value,
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
    