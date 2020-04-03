# Subsurface Collabor8 - sample python client

The following repository contains an example python client that can be used to interact with the Subsurface Collabor8 platform.


## Needed libraries

* Requires Python  > 3.6
* Requires the requests library (to install, pipenv install requests)

## Configuration

The library can be used in 2 ways

1. Using environment variables as configuration
2. Telling the library upfront which variables to use

The unit tests contains examples of both variants

### Configuration through environment variables

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


## Example usage


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




Look in the test suite for more examples
