from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
import logging



class MetaData:

    def __init__(self,token):
        super().__init__()
        self.__token=token
    

    def get_data_entities_for_field(self,assetName):
        '''
        Get all accessible entities entities for a given field and returns them as a string array 
        '''
        entities=[]
        query=queries.get_entities_query(assetName)
        print (query)
        logging.debug("Generated entity names query:%s".format(query))
        #run the query
        entitityData=self.__run_query(query)
        logging.debug("Got back entities for field:%s",entitityData['data']['metadata'])
        fieldLength=len(entitityData['data']['metadata']['fields'])
        logging.debug("Resultlength:%s",fieldLength)
        #check that we have any data coming back
        if fieldLength!=1:
            raise Exception("No metadata returned for field with name:%s".format(assetName))
        #extract then entities
        #first take the metadata basis information
        fieldInfo=entitityData['data']['metadata']['fields'][0]
        logging.debug("Keys:%s".format(fieldInfo))
        for well in fieldInfo['wells']:
                entities.append(well['name'])
        for wellbore in fieldInfo['wellbores']:
                entities.append(wellbore['name'])
        for platforms in fieldInfo['platforms']:
                entities.append(platforms['name'])
        #also append the field name itself
        if assetName not in entities:
            entities.append(assetName)
        logging.debug("Entities:%s",' '.join(map(str, entities)))
        return entities


    def __run_query(self,query):
        graph_obj=graph.Graph(self.__token)
        return graph_obj.query(query)