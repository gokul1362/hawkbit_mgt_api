# swagger_client.DistributionSetTypesApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mandatory_module**](DistributionSetTypesApi.md#add_mandatory_module) | **POST** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes | Add mandatory Software Module Type to a Distribution Set Type
[**add_optional_module**](DistributionSetTypesApi.md#add_optional_module) | **POST** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes | Add optional Software Module Type to a Distribution Set Type
[**create_distribution_set_types**](DistributionSetTypesApi.md#create_distribution_set_types) | **POST** /rest/v1/distributionsettypes | Create new distribution set types
[**delete_distribution_set_type**](DistributionSetTypesApi.md#delete_distribution_set_type) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId} | Delete Distribution Set Type by Id
[**get_distribution_set_type**](DistributionSetTypesApi.md#get_distribution_set_type) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId} | Return single Distribution Set Type
[**get_distribution_set_types**](DistributionSetTypesApi.md#get_distribution_set_types) | **GET** /rest/v1/distributionsettypes | Return all Distribution Set Types
[**get_mandatory_module**](DistributionSetTypesApi.md#get_mandatory_module) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes/{softwareModuleTypeId} | Return single mandatory Software Module Type in a Distribution Set Type
[**get_mandatory_modules**](DistributionSetTypesApi.md#get_mandatory_modules) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes | Return mandatory Software Module Types in a Distribution Set Type
[**get_optional_module**](DistributionSetTypesApi.md#get_optional_module) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes/{softwareModuleTypeId} | Return single optional Software Module Type in a Distribution Set Type
[**get_optional_modules**](DistributionSetTypesApi.md#get_optional_modules) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes | Return optional Software Module Types in a Distribution Set Type
[**remove_mandatory_module**](DistributionSetTypesApi.md#remove_mandatory_module) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes/{softwareModuleTypeId} | Delete a mandatory module from a Distribution Set Type
[**remove_optional_module**](DistributionSetTypesApi.md#remove_optional_module) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes/{softwareModuleTypeId} | Delete an optional module from a Distribution Set Type
[**update_distribution_set_type**](DistributionSetTypesApi.md#update_distribution_set_type) | **PUT** /rest/v1/distributionsettypes/{distributionSetTypeId} | Update Distribution Set Type

# **add_mandatory_module**
> add_mandatory_module(body, distribution_set_type_id)

Add mandatory Software Module Type to a Distribution Set Type

Handles the POST request for adding a mandatory software module type to a distribution set type.Note that a DS type cannot be changed after it has been used by a DS. Required Permission: UPDATE_REPOSITORY and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
body = swagger_client.MgmtId() # MgmtId | 
distribution_set_type_id = 789 # int | 

try:
    # Add mandatory Software Module Type to a Distribution Set Type
    api_instance.add_mandatory_module(body, distribution_set_type_id)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->add_mandatory_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtId**](MgmtId.md)|  | 
 **distribution_set_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_optional_module**
> add_optional_module(body, distribution_set_type_id)

Add optional Software Module Type to a Distribution Set Type

Handles the POST request for adding an optional software module type to a distribution set type.Note that a DS type cannot be changed after it has been used by a DS. Required Permission: UPDATE_REPOSITORY and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
body = swagger_client.MgmtId() # MgmtId | 
distribution_set_type_id = 789 # int | 

try:
    # Add optional Software Module Type to a Distribution Set Type
    api_instance.add_optional_module(body, distribution_set_type_id)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->add_optional_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtId**](MgmtId.md)|  | 
 **distribution_set_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_distribution_set_types**
> list[MgmtDistributionSetType] create_distribution_set_types(body)

Create new distribution set types

Handles the POST request for creating new distribution set types. The request body must always be a list of types. Required Permission: CREATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
body = [swagger_client.MgmtDistributionSetTypeRequestBodyPost()] # list[MgmtDistributionSetTypeRequestBodyPost] | 

try:
    # Create new distribution set types
    api_response = api_instance.create_distribution_set_types(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->create_distribution_set_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtDistributionSetTypeRequestBodyPost]**](MgmtDistributionSetTypeRequestBodyPost.md)|  | 

### Return type

[**list[MgmtDistributionSetType]**](MgmtDistributionSetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_distribution_set_type**
> delete_distribution_set_type(distribution_set_type_id)

Delete Distribution Set Type by Id

Handles the DELETE request for a single distribution set type. Required Permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 

try:
    # Delete Distribution Set Type by Id
    api_instance.delete_distribution_set_type(distribution_set_type_id)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->delete_distribution_set_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_set_type**
> MgmtDistributionSetType get_distribution_set_type(distribution_set_type_id)

Return single Distribution Set Type

Handles the GET request of retrieving a single distribution set type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 

try:
    # Return single Distribution Set Type
    api_response = api_instance.get_distribution_set_type(distribution_set_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_distribution_set_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 

### Return type

[**MgmtDistributionSetType**](MgmtDistributionSetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_set_types**
> PagedListMgmtDistributionSetType get_distribution_set_types(offset=offset, limit=limit, sort=sort, q=q)

Return all Distribution Set Types

Handles the GET request of retrieving all distribution set types. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all Distribution Set Types
    api_response = api_instance.get_distribution_set_types(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_distribution_set_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtDistributionSetType**](PagedListMgmtDistributionSetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mandatory_module**
> MgmtSoftwareModuleType get_mandatory_module(distribution_set_type_id, software_module_type_id)

Return single mandatory Software Module Type in a Distribution Set Type

Handles the GET request of retrieving the single mandatory software module type in that distribution set type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 
software_module_type_id = 789 # int | 

try:
    # Return single mandatory Software Module Type in a Distribution Set Type
    api_response = api_instance.get_mandatory_module(distribution_set_type_id, software_module_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_mandatory_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 
 **software_module_type_id** | **int**|  | 

### Return type

[**MgmtSoftwareModuleType**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mandatory_modules**
> list[MgmtSoftwareModuleType] get_mandatory_modules(distribution_set_type_id)

Return mandatory Software Module Types in a Distribution Set Type

Handles the GET request of retrieving the list of mandatory software module types in that distribution set type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 

try:
    # Return mandatory Software Module Types in a Distribution Set Type
    api_response = api_instance.get_mandatory_modules(distribution_set_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_mandatory_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 

### Return type

[**list[MgmtSoftwareModuleType]**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_optional_module**
> MgmtSoftwareModuleType get_optional_module(distribution_set_type_id, software_module_type_id)

Return single optional Software Module Type in a Distribution Set Type

Handles the GET request of retrieving the single optional software module type in that distribution set type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 
software_module_type_id = 789 # int | 

try:
    # Return single optional Software Module Type in a Distribution Set Type
    api_response = api_instance.get_optional_module(distribution_set_type_id, software_module_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_optional_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 
 **software_module_type_id** | **int**|  | 

### Return type

[**MgmtSoftwareModuleType**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_optional_modules**
> list[MgmtSoftwareModuleType] get_optional_modules(distribution_set_type_id)

Return optional Software Module Types in a Distribution Set Type

Handles the GET request of retrieving the list of optional software module types in that distribution set type. Required Permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 

try:
    # Return optional Software Module Types in a Distribution Set Type
    api_response = api_instance.get_optional_modules(distribution_set_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->get_optional_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 

### Return type

[**list[MgmtSoftwareModuleType]**](MgmtSoftwareModuleType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mandatory_module**
> remove_mandatory_module(distribution_set_type_id, software_module_type_id)

Delete a mandatory module from a Distribution Set Type

Handles the DELETE request for removing a software module type from a single distribution set type. Required Permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 
software_module_type_id = 789 # int | 

try:
    # Delete a mandatory module from a Distribution Set Type
    api_instance.remove_mandatory_module(distribution_set_type_id, software_module_type_id)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->remove_mandatory_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 
 **software_module_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_optional_module**
> remove_optional_module(distribution_set_type_id, software_module_type_id)

Delete an optional module from a Distribution Set Type

Handles DELETE request for removing an optional module from the distribution set type. Note that a DS type cannot be changed after it has been used by a DS. Required Permission: UPDATE_REPOSITORY and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
distribution_set_type_id = 789 # int | 
software_module_type_id = 789 # int | 

try:
    # Delete an optional module from a Distribution Set Type
    api_instance.remove_optional_module(distribution_set_type_id, software_module_type_id)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->remove_optional_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_type_id** | **int**|  | 
 **software_module_type_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_distribution_set_type**
> MgmtDistributionSetType update_distribution_set_type(body, distribution_set_type_id)

Update Distribution Set Type

Handles the PUT request for a single distribution set type. Required Permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTypesApi()
body = swagger_client.MgmtDistributionSetTypeRequestBodyPut() # MgmtDistributionSetTypeRequestBodyPut | 
distribution_set_type_id = 789 # int | 

try:
    # Update Distribution Set Type
    api_response = api_instance.update_distribution_set_type(body, distribution_set_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTypesApi->update_distribution_set_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtDistributionSetTypeRequestBodyPut**](MgmtDistributionSetTypeRequestBodyPut.md)|  | 
 **distribution_set_type_id** | **int**|  | 

### Return type

[**MgmtDistributionSetType**](MgmtDistributionSetType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

