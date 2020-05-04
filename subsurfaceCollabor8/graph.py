import requests
import os
import json
import pandas as pd
from pandas.io.json import json_normalize
import logging

class Graph:
    def __init__(self,token:str,
    subscriptionKey="",graphUrl=""):
        """
        Inits the graph class given the specified parameters

        Parameters
        ----------

        token - OAUTH2 token to use
        subscriptionKey - the API subscription key, if not specified tries to load it from environment variables
        graphUrl - the url to the GraphQL endpoint, if not specified tries to load it from environment variables
        """
        super().__init__()
        self.__token=token 
        if subscriptionKey=="":
            #try reading it from environment variable
            self.__subscriptionKey=os.getenv("AzureSubscriptionKey")
        else:
            self.__subscriptionKey=subscriptionKey
        if graphUrl=="":
            #try reading it from environment variables
            self.__graphUrl=os.getenv('AzureGraphUrl')
        else: 
            self.__graphUrl=graphUrl

    def query(self,query:str):
        """
        Runs a graphql query and returns the result as a json object
        """
        headers={
            "Authorization":"Bearer "+self.__token,
            "Accept": "application/json",
            "Ocp-Apim-Subscription-Key":self.__subscriptionKey
            }
        #send it
        
        logging.debug("Running query, url:%s, query:\n%s, subscriptionKey:%s",
        self.__graphUrl,query,self.__subscriptionKey)
        try:
            response = requests.post(self.__graphUrl,json={"query": query},headers=headers)
            logging.debug("Got query response:code,%d, content:%s",
            response.status_code,
             str(response.content))
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except Exception as err:
            raise Exception('Failed in graphql query:'+str(err)+",response:"+str(response))

    def query_to_file(self,query:str,file_path:str):
        """
        Runs a graphql query and saves the result to the given file

        """
        try:
            response=self.query(query)
            with open(file_path, "w") as outfile: 
                outfile.write(json.dumps(response)) 
        except Exception as err:
            raise Exception('Failed in processing query to file:'+str(err)+",response:"+str(response.json()))
