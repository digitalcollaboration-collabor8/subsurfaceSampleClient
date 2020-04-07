from pandas import json_normalize


def activities_to_frame(data):
    '''
    Takes a data drilling activity object which is a dict from the Collabor8 response and
    flattens it into a normalized data fram table to be used for further processing
    Structure coming in from the Collabor8 drilling activity object
    {
    "data": {
    "drilling": {
      "drillingActivity": [
        {
          "created": "2020-03-26T11:01:52Z",
          "modified": "2020-03-26T11:01:52Z", 
          .....
          .....
    
    Returned as a normalized datafram in the form of
                    created              modified               endTime  ... measuredHoleStart.value trueVerticalDepth.unitOfMeasurement trueVerticalDepth.value
            0  2020-03-19T13:11:31Z  2020-03-19T13:11:31Z  2020-03-17T01:45:00Z  ...                     0.0                                                         0.0
    '''
    result=json_normalize(data,['data','drilling','drillingActivity'])
    return result

def status_info_to_frame(data):
    '''
    Takes a data drilling status info object which is a dict from the Collabor8 response and
    flattens it into a normalized data fram table to be used for further processing
    Structure coming in from the Collabor8 drilling status info object
    {
    "data": {
    "drilling": {
      "statusInfo": [
        {
          "dataStartTime": "2020-03-24T23:00:00Z",
          "dataEndTime": "2020-03-25T23:00:00Z",
          "dataEntity": {
            "name": "34/4-M-2 H",
            "type": "wellbore"
            .....
          },
    
    Returned as a normalized datafram in the form of
    .          dataStartTime           dataEndTime                sourceSystemReportName  ... trueVerticalDepthKickoff.value wellheadElevation.unitOfMeasurement  wellheadElevation.value
    0  2020-03-16T23:00:00Z  2020-03-17T23:00:00Z  NO 34/4-M-4 H Daily Drilling Report   ...                            0.0                                   m                    0.7
                                                        
    '''
    result=json_normalize(data,['data','drilling','statusInfo'])
    return result