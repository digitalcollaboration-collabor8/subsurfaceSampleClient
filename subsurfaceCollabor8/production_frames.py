from pandas import json_normalize
import pandas as pd



def production_volumes_to_frame(data):
    """
    Takes a json production volumes result from the Collabor8 Graphql response
    and turns it into the form of a Pandas data frame
    Accepts in data in the form of
    {
    "data": {
        "production": {
        "data": [
            {
            "sourceStartTime": "2020-04-05T00:00:00Z",
            "sourceEndTime": "2020-04-06T00:00:00Z",
            "dataStartTime": "2020-04-05T00:00:00Z",
            "dataEndTime": "2020-04-06T00:00:00Z",
            "sourceEntity": {
                "name": "",
                "type": ""
            },
            "owningEntity": {
                "name": "",
                "type": ""
            },
    Return a frame in the form of
            sourceStartTime         sourceEndTime         dataStartTime           dataEndTime dataPeriod  ... owningEntity.type dataEntity.name dataEntity.type volume.uom volume.value
0  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z        day  ...                        34/10-A-23            well        Sm3  11.958302
1  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z        day  ...                        34/10-A-23            well        Sm3  148.958300
2  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z        day  ...                        34/10-A-23            well        Sm3  128.958302
3  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z        day  ...                        34/10-A-23            well        Sm3  333.958300
4  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z  2017-11-01T00:00:00Z  2017-11-02T00:00:00Z        day  ...                        34/10-A-23            well        Sm3  444.958302

    """
    #need to handle well and wellbores separately
    wells=[]
    other=[]
    for item in data['data']['production']['data']:
        if item['dataEntity']['type']=='wellbore' or item['dataEntity']['type']=='well':
            #just unpack measurements
            if item['wellMeasurements']!=None:
                for key in item['wellMeasurements'].keys():
                    wellitem=item['wellMeasurements'][key]
                    name='wellMeasurements.'+key
                    value=''
                    uom=''
                    if len(wellitem)>0:
                        value=wellitem[0]['value']
                        uom=wellitem[0]['uom']
                    item[name+".value"]=value 
                    item[name+".uom"]=uom 
                #null out the wellmeasurements
                item['wellMeasurements']={}
                wells.append(item)
        else:
            other.append(item)

    result_wells=json_normalize(wells)
    result_others=json_normalize(other)
    #concat the 2 frames into one...
    result=pd.concat([result_wells,result_others])
    return result