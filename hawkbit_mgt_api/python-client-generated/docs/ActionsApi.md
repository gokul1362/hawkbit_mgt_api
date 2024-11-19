# swagger_client.ActionsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action1**](ActionsApi.md#get_action1) | **GET** /rest/v1/actions/{actionId} | Return action by id
[**get_actions**](ActionsApi.md#get_actions) | **GET** /rest/v1/actions | Return all actions

# **get_action1**
> MgmtAction get_action1(action_id)

Return action by id

Handles the GET request of retrieving a single action by actionId.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi()
action_id = 789 # int | 

try:
    # Return action by id
    api_response = api_instance.get_action1(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->get_action1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **int**|  | 

### Return type

[**MgmtAction**](MgmtAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions**
> PagedListMgmtAction get_actions(offset=offset, limit=limit, sort=sort, q=q, representation=representation)

Return all actions

Handles the GET request of retrieving all actions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)
representation = 'representation_example' # str | The representation mode. Can be \"full\" or \"compact\". Defaults to \"compact\"  (optional)

try:
    # Return all actions
    api_response = api_instance.get_actions(offset=offset, limit=limit, sort=sort, q=q, representation=representation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->get_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 
 **representation** | **str**| The representation mode. Can be \&quot;full\&quot; or \&quot;compact\&quot;. Defaults to \&quot;compact\&quot;  | [optional] 

### Return type

[**PagedListMgmtAction**](PagedListMgmtAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

