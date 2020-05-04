import requests
import os
from requests.exceptions import HTTPError
import json 
import logging

class AuthInfo:
    clientId=None 
    clientSecret=None
    tokenUrl=None 
    resourceId=None 
    subscriptionKey=None 


    def __init__(self,clientId="",clientSecret="",
    tokenUrl="",resourceId="",subscriptionKey=""):
        super().__init__()
        self.clientId=clientId 
        self.clientSecret=clientSecret
        self.tokenUrl=tokenUrl
        self.resourceId=resourceId
        self.subscriptionKey=subscriptionKey

    def init_from_env_vars(self):
        """
        Tries to read and populate the credentials based on local environment variables
        """
        self.clientId=os.getenv('AzureClientId')
        self.clientSecret=os.getenv('AzureClientSecret')
        self.tokenUrl=os.getenv('AzureTokenUrl')
        self.resourceId=os.getenv('AzureResourceId')
        self.subscriptionKey=os.getenv('AzureSubscriptionKey')
        if self.clientId==None \
        or self.clientSecret==None \
        or self.tokenUrl==None \
        or self.resourceId==None \
        or self.subscriptionKey==None:
          raise Exception('Seems like not all required environment varible are set...')



class Authenticate:
    def __init__(self,authInfo:AuthInfo):
        super().__init__()
        self.__authInfo=authInfo
    
    def authenticate(self):
        """
        Function tries to authenticate against Azure and returns a token if succesful otherwise exception
        
        Class needs to be initiated with an AuthInfo object
        """
        authData={
            "grant_type":"client_credentials",
            "client_id":self.__authInfo.clientId,
            "client_secret":self.__authInfo.clientSecret,
            "resource":self.__authInfo.resourceId
        }
        logging.debug("Running auth with params:client_id:%s,secretLength:%d, resourceId:%s",
        self.__authInfo.clientId,len(self.__authInfo.clientSecret),self.__authInfo.resourceId)
        try:
             response = requests.post(self.__authInfo.tokenUrl, data = authData)
             # If the response was successful, no Exception will be raised
             logging.debug("Got auth response:code,%d, content:%s",response.status_code,
             str(response.content))
             response.raise_for_status()
             return response.json()['access_token']
        except HTTPError as http_err:
            logging.error(err,exc_info=True)
            raise HTTPError('HTTP error occurred:'+str(http_err))  
        except Exception as err:
            logging.error(err,exc_info=True)
            raise Exception('Other error occurred:'+str(err))  # Python 3.6
        

    
    
