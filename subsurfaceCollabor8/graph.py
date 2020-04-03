import requests
import os


class Graph:
    def __init__(self,token:str,
    subscriptionKey="",graphUrl=""):
        """
        Inits the graph class given the specified parameters
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
        try:
            response = requests.post(self.__graphUrl,json={"query": query},headers=headers)
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except Exception as err:
            raise Exception('Failed in graphql query:'+str(err)+",response:"+str(response.json()))

    