# Subsurface Collabor8 - sample python client

The following repository contains an example python client that can be used to interact with the Subsurface Collabor8 platform.


## Needed libraries

* Requires Python  > 3.6
* Requires the requests library (to install, pip3 install requests)
* Requires the pandas library to use dataframe functionality (e.g. csv++), to install pip3 install pandas
* Requies the openpyxl to use excel functions from pandas, to install pip3 install openpyxl

## Unit tests

In order to run the unit tests the client needs to be configure up-front using the environment variables as it will run active tests against the Collabor8 platform

## Configuration

The library can be used in 2 ways

1. Using environment variables as configuration
2. Telling the library upfront which variables to use

The unit tests contains examples of both variants

### Configuration through environment variables

These needs to be configured in order to run the libraries as is without any additional coding.

1. AzureClientId - the client id from Azure
2. AzureClientSecret - the client secret from Azure
3. AzureTokenUrl - the token url from azure
4. AzureResourceId - the azure resource id to authenticate against
5. AzureFileDownloadUrl - the url from where to download files in azure
6. AzureSubscriptionKey - the service subscription key to use when calling the api's
7. AzureGraphUrl - the url for graph queries
8. AzureValidateUrl - the url to use for validation of reports
9. AzureSubmitUrl - the url to use for submital of reports

### Configuration through code

The same parameters if not specified can be added as part of the call to the different functions


## Installing and running as a client

The package can be installed and run directly from a command line if needed and through this it will then be possible to e.g. download certain drilling and production data directly to e.g. excel/csv.

### To install and run it as a client

1. Python 3 needs to be installed locally
2. Pip3 needs to be installed locally
3. You can install the package locally using the command: **pip3 install --user -e .** 
4. Afterwards you can run the client e.g. with the command **subsurfaceCollabor8 drilling --help** to display the help message

### To run it without installing the package

You can also run the package directly without installing it using the standard python3 command

**pyhton3 -m subsurfaceCollabor8 --help** which displays the help message

### Help on options for client

Run the command **python3 -m subsurfaceCollabor8 drilling --help** to display possible options for the sample client


### Data conversion and how to convert query results to other formats

In the drilling_frames module there is examples of how to convert the result from a Collabor8 platform drilling GraphQL query to a Pandas dataframe to be used for further processing

## Example usage of client directly

### Downlod drilling data activities to Excel

This example demonstrates how to query for drilling activity data for a given wellbore and period and save the result to an excel file.

1. Make sure the client is installed with python3 and any needed libraries as described above
2. Make sure that you have configured the required Azure environment variables as described above
3. Example to download drilling activities for wellbore "34/4-M-4 H" in period 2020-01-21 to 2020-03-26 run the command
   1. **python3 -m subsurfaceCollabor8 drilling --datatype="activities" --format="excel" --start="2020-01-20" --end="2020-03-26" --wellbore="34/4-M-4 H" --log="./log.txt" --output="./excel_data/activities.xlsx"**
4. Example to download drilling status_info for wellbore "34/4-M-4 H" in period 2020-01-21 to 2020-03-26 run the command
   1. **python3 -m subsurfaceCollabor8 drilling --datatype="status_info" --format="excel" --start="2020-01-20" --end="2020-03-26" --wellbore="34/4-M-4 H" --log="./log.txt" --output="./excel_data/activities.xlsx"**
5. Example to download drilling lithologies for wellbore "34/4-M-4 H" in period 2020-01-21 to 2020-03-26 run the command
   1. **python3 -m subsurfaceCollabor8 drilling --datatype="lithology" --format="excel" --start="2020-01-20" --end="2020-03-26" --wellbore="34/4-M-4 H" --log="./log.txt" --output="./excel_data/activities.xlsx"**



## Example code usage




#### Get a authorization token using environment variables

```python
from subsurfaceCollabor8 import auth
....
.....
 def get_token():
        authInfo=auth.AuthInfo() 
        authInfo.init_from_env_vars()
        authObj=auth.Authenticate(authInfo) 
        try:
             token=authObj.authenticate()
             return token
        except Exception as err:
            raise Exception('Failed in getting token:'+str(err)) 
```


#### Validate a report using environment variables

```python
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import reports
....
.....
 def validate_report(self,file_path:str):
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            report=reports.Reports(reports.ReportType.DDRML,
            file_path,
            token)
            return report.validate()
        except Exception as err:
             raise Exception('Failed in validating file:'+str(err))  
```

#### Submit a report using environment variables

```python
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import reports
....
.....
 def submit_report(self,file_path:str):
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            report=reports.Reports(reports.ReportType.DDRML,
            file_path,
            token)
            return report.submit()
        except Exception as err:
             raise Exception('Failed in submit of file:'+str(err))  
```


#### Query the system through GraphQL

```python
from subsurfaceCollabor8 import auth
from subsurfaceCollabor8 import graph
....
....
def run_sample_query(self):
        query='''query{
        metadata {
            facilities(referenceId:"18116481"){
                name
                id
                created
                createdBy
                referenceId
                code
                type
                aliases {
                    name
                    code
                    description
                }
            }
        
        }
    }'''
        authInfo=auth.AuthInfo()
        try:
            authInfo.init_from_env_vars()
            authObj=auth.Authenticate(authInfo) 
            token=authObj.authenticate()
            query_obj=graph.Graph(token)
            result=query_obj.query(query)
            print ('result:'+str(result))
        except Exception as err:
            self.fail("Query failed with error:"+str(err))
```

#### Query the system for drilling activities, converting it to a panda normalized dataframe and then write result to Excel

```python
 from subsurfaceCollabor8 import queries
 from subsurfaceCollabor8 import auth
 from subsurfaceCollabor8 import graph
 from subsurfaceCollabor8 import drilling_frames
 from subsurfaceCollabor8 import frame_utils
 import os

 def get_activities_to_excel(token:str,excel_file:str): 
        start="2020-01-21T23:00:00.000Z"
        end="2020-03-26T12:00:00.000Z"
        entity="34/4-M-4 H"
        query=queries.get_drilling_activity_query(start,end,entity)
        try:
            query_obj=graph.Graph(self.token)
            result=query_obj.query(query)
            #have the dict send it to a panda frame creation
            normalized_frame=drilling_frames.activities_to_frame(result)
            #write the data to a csv file
            frame_utils.frame_to_excel(normalized_frame,excel_file)
            print ("Excel result written to:"+result_file)
        except Exception as err:
            self.fail("Query drilling activities failed with error:"+str(err))         
```




Look in the test suite for more examples
