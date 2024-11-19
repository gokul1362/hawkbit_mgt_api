# swagger_client.SoftwareModulesApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata1**](SoftwareModulesApi.md#create_metadata1) | **POST** /rest/v1/softwaremodules/{softwareModuleId}/metadata | Creates a list of meta data for a specific Software Module
[**create_software_modules**](SoftwareModulesApi.md#create_software_modules) | **POST** /rest/v1/softwaremodules | Create Software Module(s)
[**delete_artifact**](SoftwareModulesApi.md#delete_artifact) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId} | Delete artifact by Id
[**delete_metadata1**](SoftwareModulesApi.md#delete_metadata1) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Delete single meta data entry from the software module
[**delete_software_module**](SoftwareModulesApi.md#delete_software_module) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId} | Delete Software Module by Id
[**get_artifact**](SoftwareModulesApi.md#get_artifact) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId} | Return single Artifact meta data
[**get_artifacts**](SoftwareModulesApi.md#get_artifacts) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts | Return all meta data of artifacts assigned to a software module
[**get_metadata1**](SoftwareModulesApi.md#get_metadata1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/metadata | Return meta data for a Software Module
[**get_metadata_value1**](SoftwareModulesApi.md#get_metadata_value1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Return single meta data value for a specific key of a Software Module
[**get_software_module**](SoftwareModulesApi.md#get_software_module) | **GET** /rest/v1/softwaremodules/{softwareModuleId} | Return Software Module by id
[**get_software_modules**](SoftwareModulesApi.md#get_software_modules) | **GET** /rest/v1/softwaremodules | Return all Software modules
[**update_metadata1**](SoftwareModulesApi.md#update_metadata1) | **PUT** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Update a single meta data value of a Software Module
[**update_software_module**](SoftwareModulesApi.md#update_software_module) | **PUT** /rest/v1/softwaremodules/{softwareModuleId} | Update Software Module
[**upload_artifact**](SoftwareModulesApi.md#upload_artifact) | **POST** /rest/v1/softwaremodules/{softwareModuleId}/artifacts | Upload artifact

# **create_metadata1**
> list[MgmtSoftwareModuleMetadata] create_metadata1(body, software_module_id)

Creates a list of meta data for a specific Software Module

Create a list of meta data entries Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
body = [swagger_client.MgmtSoftwareModuleMetadata()] # list[MgmtSoftwareModuleMetadata] | 
software_module_id = 789 # int | 

try:
    # Creates a list of meta data for a specific Software Module
    api_response = api_instance.create_metadata1(body, software_module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->create_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtSoftwareModuleMetadata]**](MgmtSoftwareModuleMetadata.md)|  | 
 **software_module_id** | **int**|  | 

### Return type

[**list[MgmtSoftwareModuleMetadata]**](MgmtSoftwareModuleMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_software_modules**
> list[MgmtSoftwareModule] create_software_modules(body)

Create Software Module(s)

Handles the POST request of creating new software modules. The request body must always be a list of modules. Required Permission: CREATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
body = [swagger_client.MgmtSoftwareModuleRequestBodyPost()] # list[MgmtSoftwareModuleRequestBodyPost] | 

try:
    # Create Software Module(s)
    api_response = api_instance.create_software_modules(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->create_software_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtSoftwareModuleRequestBodyPost]**](MgmtSoftwareModuleRequestBodyPost.md)|  | 

### Return type

[**list[MgmtSoftwareModule]**](MgmtSoftwareModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> delete_artifact(software_module_id, artifact_id)

Delete artifact by Id

Handles the DELETE request for a single Artifact assigned to a SoftwareModule. Required Permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
artifact_id = 789 # int | 

try:
    # Delete artifact by Id
    api_instance.delete_artifact(software_module_id, artifact_id)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->delete_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **artifact_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata1**
> delete_metadata1(software_module_id, metadata_key)

Delete single meta data entry from the software module

Delete a single meta data. Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Delete single meta data entry from the software module
    api_instance.delete_metadata1(software_module_id, metadata_key)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->delete_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_software_module**
> delete_software_module(software_module_id)

Delete Software Module by Id

Handles the DELETE request for a single softwaremodule within Hawkbit. Required Permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 

try:
    # Delete Software Module by Id
    api_instance.delete_software_module(software_module_id)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->delete_software_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact**
> MgmtArtifact get_artifact(software_module_id, artifact_id, useartifacturlhandler=useartifacturlhandler)

Return single Artifact meta data

Handles the GET request of retrieving a single Artifact meta data request. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
artifact_id = 789 # int | 
useartifacturlhandler = true # bool |  (optional)

try:
    # Return single Artifact meta data
    api_response = api_instance.get_artifact(software_module_id, artifact_id, useartifacturlhandler=useartifacturlhandler)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **artifact_id** | **int**|  | 
 **useartifacturlhandler** | **bool**|  | [optional] 

### Return type

[**MgmtArtifact**](MgmtArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts**
> list[MgmtArtifact] get_artifacts(software_module_id, representation=representation, useartifacturlhandler=useartifacturlhandler)

Return all meta data of artifacts assigned to a software module

Handles the GET request of retrieving all meta data of artifacts assigned to a software module. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
representation = 'compact' # str |  (optional) (default to compact)
useartifacturlhandler = true # bool |  (optional)

try:
    # Return all meta data of artifacts assigned to a software module
    api_response = api_instance.get_artifacts(software_module_id, representation=representation, useartifacturlhandler=useartifacturlhandler)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **representation** | **str**|  | [optional] [default to compact]
 **useartifacturlhandler** | **bool**|  | [optional] 

### Return type

[**list[MgmtArtifact]**](MgmtArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata1**
> PagedListMgmtSoftwareModuleMetadata get_metadata1(software_module_id, offset=offset, limit=limit, sort=sort, q=q)

Return meta data for a Software Module

Get a paged list of meta data for a software module. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return meta data for a Software Module
    api_response = api_instance.get_metadata1(software_module_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtSoftwareModuleMetadata**](PagedListMgmtSoftwareModuleMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_value1**
> MgmtSoftwareModuleMetadata get_metadata_value1(software_module_id, metadata_key)

Return single meta data value for a specific key of a Software Module

Get a single meta data value for a meta data key. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Return single meta data value for a specific key of a Software Module
    api_response = api_instance.get_metadata_value1(software_module_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_metadata_value1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtSoftwareModuleMetadata**](MgmtSoftwareModuleMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_module**
> MgmtSoftwareModule get_software_module(software_module_id)

Return Software Module by id

Handles the GET request of retrieving a single softwaremodule. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 

try:
    # Return Software Module by id
    api_response = api_instance.get_software_module(software_module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_software_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 

### Return type

[**MgmtSoftwareModule**](MgmtSoftwareModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_modules**
> PagedListMgmtSoftwareModule get_software_modules(offset=offset, limit=limit, sort=sort, q=q)

Return all Software modules

Handles the GET request of retrieving all softwaremodules. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all Software modules
    api_response = api_instance.get_software_modules(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->get_software_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtSoftwareModule**](PagedListMgmtSoftwareModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata1**
> MgmtSoftwareModuleMetadata update_metadata1(body, software_module_id, metadata_key)

Update a single meta data value of a Software Module

Update a single meta data value for speficic key. Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
body = swagger_client.MgmtSoftwareModuleMetadataBodyPut() # MgmtSoftwareModuleMetadataBodyPut | 
software_module_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Update a single meta data value of a Software Module
    api_response = api_instance.update_metadata1(body, software_module_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->update_metadata1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtSoftwareModuleMetadataBodyPut**](MgmtSoftwareModuleMetadataBodyPut.md)|  | 
 **software_module_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtSoftwareModuleMetadata**](MgmtSoftwareModuleMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_software_module**
> MgmtSoftwareModule update_software_module(body, software_module_id)

Update Software Module

Handles the PUT request for a single softwaremodule within Hawkbit. Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
body = swagger_client.MgmtSoftwareModuleRequestBodyPut() # MgmtSoftwareModuleRequestBodyPut | 
software_module_id = 789 # int | 

try:
    # Update Software Module
    api_response = api_instance.update_software_module(body, software_module_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->update_software_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtSoftwareModuleRequestBodyPut**](MgmtSoftwareModuleRequestBodyPut.md)|  | 
 **software_module_id** | **int**|  | 

### Return type

[**MgmtSoftwareModule**](MgmtSoftwareModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifact**
> MgmtArtifact upload_artifact(software_module_id, file=file, filename=filename, md5sum=md5sum, sha1sum=sha1sum, sha256sum=sha256sum)

Upload artifact

Handles POST request for artifact upload. Required Permission: CREATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModulesApi()
software_module_id = 789 # int | 
file = 'file_example' # str |  (optional)
filename = 'filename_example' # str |  (optional)
md5sum = 'md5sum_example' # str |  (optional)
sha1sum = 'sha1sum_example' # str |  (optional)
sha256sum = 'sha256sum_example' # str |  (optional)

try:
    # Upload artifact
    api_response = api_instance.upload_artifact(software_module_id, file=file, filename=filename, md5sum=md5sum, sha1sum=sha1sum, sha256sum=sha256sum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModulesApi->upload_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **file** | **str**|  | [optional] 
 **filename** | **str**|  | [optional] 
 **md5sum** | **str**|  | [optional] 
 **sha1sum** | **str**|  | [optional] 
 **sha256sum** | **str**|  | [optional] 

### Return type

[**MgmtArtifact**](MgmtArtifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

