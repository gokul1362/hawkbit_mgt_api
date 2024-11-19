# swagger_client.TargetTypesApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_compatible_distribution_sets**](TargetTypesApi.md#add_compatible_distribution_sets) | **POST** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes | Adding compatibility of a distribution set type to a target type
[**create_target_types**](TargetTypesApi.md#create_target_types) | **POST** /rest/v1/targettypes | Create target types
[**delete_target_type**](TargetTypesApi.md#delete_target_type) | **DELETE** /rest/v1/targettypes/{targetTypeId} | Delete target type by id
[**get_compatible_distribution_sets**](TargetTypesApi.md#get_compatible_distribution_sets) | **GET** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes | Return list of compatible distribution set types
[**get_target_type**](TargetTypesApi.md#get_target_type) | **GET** /rest/v1/targettypes/{targetTypeId} | Return target type by id
[**get_target_types**](TargetTypesApi.md#get_target_types) | **GET** /rest/v1/targettypes | Return all target types
[**remove_compatible_distribution_set**](TargetTypesApi.md#remove_compatible_distribution_set) | **DELETE** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes/{distributionSetTypeId} | Remove compatibility of distribution set type from the target type
[**update_target_type**](TargetTypesApi.md#update_target_type) | **PUT** /rest/v1/targettypes/{targetTypeId} | Update target type by id

# **add_compatible_distribution_sets**
> add_compatible_distribution_sets(body, target_type_id)

Adding compatibility of a distribution set type to a target type

Handles the POST request for adding compatible distribution set types to a target type. Required Permission: UPDATE_TARGET and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
body = [swagger_client.MgmtDistributionSetTypeAssignment()] # list[MgmtDistributionSetTypeAssignment] | 
target_type_id = 789 # int | 

try:
    # Adding compatibility of a distribution set type to a target type
    api_instance.add_compatible_distribution_sets(body, target_type_id)
except ApiException as e:
    print("Exception when calling TargetTypesApi->add_compatible_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtDistributionSetTypeAssignment]**](MgmtDistributionSetTypeAssignment.md)|  | 
 **target_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target_types**
> list[MgmtTargetType] create_target_types(body)

Create target types

Handles the POST request for creating new target types. The request body must always be a list of types. Required Permission: CREATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
body = [swagger_client.MgmtTargetTypeRequestBodyPost()] # list[MgmtTargetTypeRequestBodyPost] | 

try:
    # Create target types
    api_response = api_instance.create_target_types(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTypesApi->create_target_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtTargetTypeRequestBodyPost]**](MgmtTargetTypeRequestBodyPost.md)|  | 

### Return type

[**list[MgmtTargetType]**](MgmtTargetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target_type**
> delete_target_type(target_type_id)

Delete target type by id

Handles the DELETE request for a single target type. Required Permission: DELETE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
target_type_id = 789 # int | 

try:
    # Delete target type by id
    api_instance.delete_target_type(target_type_id)
except ApiException as e:
    print("Exception when calling TargetTypesApi->delete_target_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatible_distribution_sets**
> list[MgmtDistributionSetType] get_compatible_distribution_sets(target_type_id)

Return list of compatible distribution set types

Handles the GET request of retrieving the list of compatible distribution set types in that target type. Required Permission: READ_TARGET, READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
target_type_id = 789 # int | 

try:
    # Return list of compatible distribution set types
    api_response = api_instance.get_compatible_distribution_sets(target_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTypesApi->get_compatible_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type_id** | **int**|  | 

### Return type

[**list[MgmtDistributionSetType]**](MgmtDistributionSetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_type**
> MgmtTargetType get_target_type(target_type_id)

Return target type by id

Handles the GET request of retrieving a single target type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
target_type_id = 789 # int | 

try:
    # Return target type by id
    api_response = api_instance.get_target_type(target_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTypesApi->get_target_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type_id** | **int**|  | 

### Return type

[**MgmtTargetType**](MgmtTargetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_types**
> PagedListMgmtTargetType get_target_types(offset=offset, limit=limit, sort=sort, q=q)

Return all target types

Handles the GET request of retrieving all target types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all target types
    api_response = api_instance.get_target_types(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTypesApi->get_target_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtTargetType**](PagedListMgmtTargetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_compatible_distribution_set**
> remove_compatible_distribution_set(target_type_id, distribution_set_type_id)

Remove compatibility of distribution set type from the target type

Handles the DELETE request for removing a distribution set type from a single target type. Required Permission: UPDATE_TARGET and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
target_type_id = 789 # int | 
distribution_set_type_id = 789 # int | 

try:
    # Remove compatibility of distribution set type from the target type
    api_instance.remove_compatible_distribution_set(target_type_id, distribution_set_type_id)
except ApiException as e:
    print("Exception when calling TargetTypesApi->remove_compatible_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_type_id** | **int**|  | 
 **distribution_set_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_type**
> MgmtTargetType update_target_type(body, target_type_id)

Update target type by id

Handles the PUT request for a single target type. Required Permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTypesApi()
body = swagger_client.MgmtTargetTypeRequestBodyPut() # MgmtTargetTypeRequestBodyPut | 
target_type_id = 789 # int | 

try:
    # Update target type by id
    api_response = api_instance.update_target_type(body, target_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTypesApi->update_target_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTargetTypeRequestBodyPut**](MgmtTargetTypeRequestBodyPut.md)|  | 
 **target_type_id** | **int**|  | 

### Return type

[**MgmtTargetType**](MgmtTargetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

