# swagger_client.SoftwareModuleTypesApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_software_module_types**](SoftwareModuleTypesApi.md#create_software_module_types) | **POST** /rest/v1/softwaremoduletypes | Creates new Software Module Types
[**delete_software_module_type**](SoftwareModuleTypesApi.md#delete_software_module_type) | **DELETE** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Delete Software Module Type by Id
[**get_software_module_type**](SoftwareModuleTypesApi.md#get_software_module_type) | **GET** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Return single Software Module Type
[**get_types**](SoftwareModuleTypesApi.md#get_types) | **GET** /rest/v1/softwaremoduletypes | Return all Software Module Types
[**update_software_module_type**](SoftwareModuleTypesApi.md#update_software_module_type) | **PUT** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Update Software Module Type

# **create_software_module_types**
> list[MgmtSoftwareModuleType] create_software_module_types(body)

Creates new Software Module Types

Handles the POST request of creating new software module types. The request body must always be a list of module types. Required Permission: CREATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModuleTypesApi()
body = [swagger_client.MgmtSoftwareModuleTypeRequestBodyPost()] # list[MgmtSoftwareModuleTypeRequestBodyPost] | 

try:
    # Creates new Software Module Types
    api_response = api_instance.create_software_module_types(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModuleTypesApi->create_software_module_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtSoftwareModuleTypeRequestBodyPost]**](MgmtSoftwareModuleTypeRequestBodyPost.md)|  | 

### Return type

[**list[MgmtSoftwareModuleType]**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_software_module_type**
> delete_software_module_type(software_module_type_id)

Delete Software Module Type by Id

Handles the DELETE request for a single software module type. Required Permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModuleTypesApi()
software_module_type_id = 789 # int | 

try:
    # Delete Software Module Type by Id
    api_instance.delete_software_module_type(software_module_type_id)
except ApiException as e:
    print("Exception when calling SoftwareModuleTypesApi->delete_software_module_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software_module_type**
> MgmtSoftwareModuleType get_software_module_type(software_module_type_id)

Return single Software Module Type

Handles the GET request of retrieving a single software module type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModuleTypesApi()
software_module_type_id = 789 # int | 

try:
    # Return single Software Module Type
    api_response = api_instance.get_software_module_type(software_module_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModuleTypesApi->get_software_module_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_type_id** | **int**|  | 

### Return type

[**MgmtSoftwareModuleType**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_types**
> PagedListMgmtSoftwareModuleType get_types(offset=offset, limit=limit, sort=sort, q=q)

Return all Software Module Types

Handles the GET request of retrieving all software module types. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModuleTypesApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all Software Module Types
    api_response = api_instance.get_types(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModuleTypesApi->get_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtSoftwareModuleType**](PagedListMgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_software_module_type**
> MgmtSoftwareModuleType update_software_module_type(body, software_module_type_id)

Update Software Module Type

Handles the PUT request for a single software module type. Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SoftwareModuleTypesApi()
body = swagger_client.MgmtSoftwareModuleTypeRequestBodyPut() # MgmtSoftwareModuleTypeRequestBodyPut | 
software_module_type_id = 789 # int | 

try:
    # Update Software Module Type
    api_response = api_instance.update_software_module_type(body, software_module_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareModuleTypesApi->update_software_module_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtSoftwareModuleTypeRequestBodyPut**](MgmtSoftwareModuleTypeRequestBodyPut.md)|  | 
 **software_module_type_id** | **int**|  | 

### Return type

[**MgmtSoftwareModuleType**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

