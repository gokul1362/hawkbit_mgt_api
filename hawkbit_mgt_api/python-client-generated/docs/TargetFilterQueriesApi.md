# swagger_client.TargetFilterQueriesApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter**](TargetFilterQueriesApi.md#create_filter) | **POST** /rest/v1/targetfilters | Create target filter
[**delete_assigned_distribution_set**](TargetFilterQueriesApi.md#delete_assigned_distribution_set) | **DELETE** /rest/v1/targetfilters/{filterId}/autoAssignDS | Remove Distribution Set for auto assignment of a target filter
[**delete_filter**](TargetFilterQueriesApi.md#delete_filter) | **DELETE** /rest/v1/targetfilters/{filterId} | Delete target filter by id
[**get_assigned_distribution_set1**](TargetFilterQueriesApi.md#get_assigned_distribution_set1) | **GET** /rest/v1/targetfilters/{filterId}/autoAssignDS | Return distribution set for auto assignment of a specific target filter
[**get_filter**](TargetFilterQueriesApi.md#get_filter) | **GET** /rest/v1/targetfilters/{filterId} | Return target filter query by id
[**get_filters**](TargetFilterQueriesApi.md#get_filters) | **GET** /rest/v1/targetfilters | Return all target filter queries
[**post_assigned_distribution_set1**](TargetFilterQueriesApi.md#post_assigned_distribution_set1) | **POST** /rest/v1/targetfilters/{filterId}/autoAssignDS | Set auto assignment of distribution set for a target filter query
[**update_filter**](TargetFilterQueriesApi.md#update_filter) | **PUT** /rest/v1/targetfilters/{filterId} | Updates target filter query by id

# **create_filter**
> MgmtTargetFilterQuery create_filter(body)

Create target filter

Handles the POST request to create a new target filter query. Required permission: CREATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
body = swagger_client.MgmtTargetFilterQueryRequestBody() # MgmtTargetFilterQueryRequestBody | 

try:
    # Create target filter
    api_response = api_instance.create_filter(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->create_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTargetFilterQueryRequestBody**](MgmtTargetFilterQueryRequestBody.md)|  | 

### Return type

[**MgmtTargetFilterQuery**](MgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assigned_distribution_set**
> delete_assigned_distribution_set(filter_id)

Remove Distribution Set for auto assignment of a target filter

Removes the auto assign distribution set from the target filter query. Required permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
filter_id = 789 # int | 

try:
    # Remove Distribution Set for auto assignment of a target filter
    api_instance.delete_assigned_distribution_set(filter_id)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->delete_assigned_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter**
> delete_filter(filter_id)

Delete target filter by id

Handles the DELETE request of deleting a target filter query. Required permission: DELETE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
filter_id = 789 # int | 

try:
    # Delete target filter by id
    api_instance.delete_filter(filter_id)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->delete_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_distribution_set1**
> MgmtDistributionSet get_assigned_distribution_set1(filter_id)

Return distribution set for auto assignment of a specific target filter

Handles the GET request of retrieving the auto assign distribution set. Required permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
filter_id = 789 # int | 

try:
    # Return distribution set for auto assignment of a specific target filter
    api_response = api_instance.get_assigned_distribution_set1(filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->get_assigned_distribution_set1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  | 

### Return type

[**MgmtDistributionSet**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filter**
> MgmtTargetFilterQuery get_filter(filter_id)

Return target filter query by id

Handles the GET request of retrieving a single target filter query. Required permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
filter_id = 789 # int | 

try:
    # Return target filter query by id
    api_response = api_instance.get_filter(filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->get_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_id** | **int**|  | 

### Return type

[**MgmtTargetFilterQuery**](MgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters**
> PagedListMgmtTargetFilterQuery get_filters(offset=offset, limit=limit, sort=sort, q=q, representation=representation)

Return all target filter queries

Handles the GET request of retrieving all target filter queries. Required permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)
representation = 'compact' # str |  (optional) (default to compact)

try:
    # Return all target filter queries
    api_response = api_instance.get_filters(offset=offset, limit=limit, sort=sort, q=q, representation=representation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->get_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 
 **representation** | **str**|  | [optional] [default to compact]

### Return type

[**PagedListMgmtTargetFilterQuery**](PagedListMgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_assigned_distribution_set1**
> MgmtTargetFilterQuery post_assigned_distribution_set1(body, filter_id)

Set auto assignment of distribution set for a target filter query

Handles the POST request of setting the auto assign distribution set for a target filter query. Required permissions: UPDATE_TARGET and READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
body = swagger_client.MgmtDistributionSetAutoAssignment() # MgmtDistributionSetAutoAssignment | 
filter_id = 789 # int | 

try:
    # Set auto assignment of distribution set for a target filter query
    api_response = api_instance.post_assigned_distribution_set1(body, filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->post_assigned_distribution_set1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtDistributionSetAutoAssignment**](MgmtDistributionSetAutoAssignment.md)|  | 
 **filter_id** | **int**|  | 

### Return type

[**MgmtTargetFilterQuery**](MgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filter**
> MgmtTargetFilterQuery update_filter(body, filter_id)

Updates target filter query by id

Handles the PUT request of updating a target filter query. Required permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetFilterQueriesApi()
body = swagger_client.MgmtTargetFilterQueryRequestBody() # MgmtTargetFilterQueryRequestBody | 
filter_id = 789 # int | 

try:
    # Updates target filter query by id
    api_response = api_instance.update_filter(body, filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetFilterQueriesApi->update_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTargetFilterQueryRequestBody**](MgmtTargetFilterQueryRequestBody.md)|  | 
 **filter_id** | **int**|  | 

### Return type

[**MgmtTargetFilterQuery**](MgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

