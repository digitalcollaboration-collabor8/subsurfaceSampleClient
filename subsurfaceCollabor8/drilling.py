from subsurfaceCollabor8 import queries
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
from subsurfaceCollabor8 import drilling_frames
from subsurfaceCollabor8 import frame_utils
from enum import Enum
import json
import os 


class DrillingDataType(Enum):
    ACTIVITIES = "activities"
    LITHOLOGY = "lithology"
    STATUS_INFO = "status_info"
    
class DrillingData:

    def __init__(self,token):
        super().__init__()
        self.__token=token
    
    def get_json_data(self,period_start,period_end,entity,data_type:DrillingDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for drilling data of the given type
        and using the specified OAuth2 token for authentication. Data is returned as a json dict

        Parameters
        ----------

        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of wellbore to query for
        data_type : the type of drilling data to query for

        """
        return self.__run_query(self.__build_query(period_start,period_end,entity,data_type))
    
    def get_json_data_to_file(self,output_file,period_start,period_end,entity,data_type:DrillingDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for drilling data of the given type
        and using the specified OAuth2 token for authentication. Data is returned as a json dict

        Parameters
        ----------
        output_file : path to file to store json result in
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of wellbore to query for
        data_type : the type of drilling data to query for

        """
        data=self.__run_query(self.__build_query(period_start,period_end,entity,data_type))
        with open(output_file, 'w') as fp:
            json.dump(data, fp)
    
    def get_csv_data(self,output_file,period_start,period_end,entity,data_type:DrillingDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for drilling data of the given type
        and using the specified OAuth2 token for authentication. Data is written to the specified csv file.

        Parameters
        ----------
        output_file : full path to where to store csv file
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of wellbore to query for
        data_type : the type of drilling data to query for

        """
        json=self.get_json_data(period_start,period_end,entity,data_type)
        #convert it to a pandas frame
        frame=self.__convert_data_to_frame(json,data_type)
        frame_utils.frame_to_csv(frame,output_file)
    
    def get_excel_data(self,output_file,period_start,period_end,entity,data_type:DrillingDataType):
        """
        Will run a GraphQL query against the Collabor8 platform and ask for drilling data of the given type
        and using the specified OAuth2 token for authentication. Data is as a Excel file using the specified output_file path

        Parameters
        ----------

        output_file : full path to excel file to write results to
        period_start : start of period to query for
        period_end : end of period to query for
        entity : name of wellbore to query for
        data_type : the type of drilling data to query for
        
        """
        json=self.get_json_data(period_start,period_end,entity,data_type)
        #convert it to a pandas frame
        frame=self.__convert_data_to_frame(json,data_type)
        frame_utils.frame_to_excel(frame,output_file)
        
    
    def __build_query(self,period_start,period_end,entity,data_type:DrillingDataType):
        if data_type==DrillingDataType.ACTIVITIES:
            return queries.get_drilling_activity_query(period_start,period_end,entity)
        elif data_type==DrillingDataType.LITHOLOGY:
            return queries.get_drilling_lithology_description(entity)
        elif data_type==DrillingDataType.STATUS_INFO:
            return queries.get_drilling_status_info_query(period_start,period_end,entity)
        else:
            raise Exception("Unknown data type specified")
    
    def __convert_data_to_frame(self,data,data_type:DrillingDataType):
        if data_type==DrillingDataType.ACTIVITIES:
            return drilling_frames.activities_to_frame(data)
        elif data_type==DrillingDataType.LITHOLOGY:
            return drilling_frames.lithology_info_to_frame(data)
        elif data_type==DrillingDataType.STATUS_INFO:
            return drilling_frames.status_info_to_frame(data)
        else:
            raise Exception("Unknown data type specified")
    

    def map_str_activity_to_enum(self,data_type):
        
        if data_type==DrillingDataType.ACTIVITIES.value:
            return DrillingDataType.ACTIVITIES
        elif data_type==DrillingDataType.LITHOLOGY.value:
            return DrillingDataType.LITHOLOGY
        elif data_type==DrillingDataType.STATUS_INFO.value:
            return DrillingDataType.STATUS_INFO
        else:
            raise Exception("Unknown data type specified")

    def __run_query(self,query):
        graph_obj=graph.Graph(self.__token)
        return graph_obj.query(query)

    