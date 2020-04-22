from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
from subsurfaceCollabor8 import production_frames
from subsurfaceCollabor8 import frame_utils
from enum import Enum
import json
import os 

class ProductionDataType(Enum):
    PRODUCTION="Production"
    INJECTION="Injection"
    CONSUMPTION="Consumption"
    IMPORT="Import"
    EXPORT="Export"
    INVENTORY="Inventory"
    INSTALLATION_DATA="InstallationData"

class ProductionData:

    def __init__(self,token):
        super().__init__()
        self.__token=token

    def get_json_data(self,period_start,period_end,entity,data_type:ProductionDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for production data of 
        the given type and using the specified OAuth2 token for authentication. 
        Data is returned as a json dict

        Parameters
        ----------

        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of asset/entity to query for
        data_type : the type of production data to query for

        """
        return self.__run_query(self.__build_query(period_start,period_end,entity,data_type))
    
    def get_json_data_to_file(self,output_file,period_start,period_end,entity,data_type:ProductionDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for production data of the given type
        and using the specified OAuth2 token for authentication. Data is returned as a json dict

        Parameters
        ----------
        output_file : path to file to store json result in
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of asset/entity to query for
        data_type : the type of production data to query for

        """
        data=self.__run_query(self.__build_query(period_start,period_end,entity,data_type))
        with open(output_file, 'w') as fp:
            json.dump(data, fp)
    
    def get_csv_data(self,output_file,period_start,period_end,entity,data_type:ProductionDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for production data of the given type
        and using the specified OAuth2 token for authentication. Data is written to the specified csv file.

        Parameters
        ----------
        output_file : full path to where to store csv file
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of asset/entity to query for
        data_type : the type of production data to query for

        """
        json=self.get_json_data(period_start,period_end,entity,data_type)
        #convert it to a pandas frame
        frame=self.__convert_data_to_frame(json,data_type)
        frame_utils.frame_to_csv(frame,output_file)
    
    def get_excel_data(self,output_file,period_start,period_end,entity,data_type:ProductionDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for productiong data of 
        the given type and using the specified OAuth2 token for authentication. Data is as a Excel file using the specified output_file path

        Parameters
        ----------

        output_file : full path to excel file to write results to
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of asset/entity to query for
        data_type : the type of production data to query for
        
        """
        json=self.get_json_data(period_start,period_end,entity,data_type)
        #convert it to a pandas frame
        frame=self.__convert_data_to_frame(json,data_type)
        frame_utils.frame_to_excel(frame,output_file)
    
    def __build_query(self,period_start,period_end,entity,data_type:ProductionDataType):
        return queries.get_production_volumes_regex(period_start,
            period_end,entity,data_type.value)
    
    def map_str_prod_datatype_to_enum(self,data_type):

        if data_type==ProductionDataType.PRODUCTION.value:
            return ProductionDataType.PRODUCTION
        elif data_type==ProductionDataType.CONSUMPTION.value:
            return ProductionDataType.CONSUMPTION
        elif data_type==ProductionDataType.EXPORT.value:
            return ProductionDataType.EXPORT
        elif data_type==ProductionDataType.IMPORT.value:
            return ProductionDataType.IMPORT
        elif data_type==ProductionDataType.INJECTION.value:
            return ProductionDataType.INJECTION
        elif data_type==ProductionDataType.INSTALLATION_DATA.value:
            return ProductionDataType.INSTALLATION_DATA
        elif data_type==ProductionDataType.INVENTORY.value:
            return ProductionDataType.INVENTORY
        else:
            raise Exception("Unknown data_type specified:%s",data_type)
        


    
    def __convert_data_to_frame(self,data,data_type:ProductionDataType):
        return production_frames.production_volumes_to_frame(data)
    
    def __run_query(self,query):
        graph_obj=graph.Graph(self.__token)
        return graph_obj.query(query)