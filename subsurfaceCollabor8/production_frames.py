from pandas import json_normalize




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
    result=json_normalize(data,['data','production','data'])
    return result