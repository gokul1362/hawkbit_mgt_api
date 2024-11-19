# swagger_client.RolloutsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve**](RolloutsApi.md#approve) | **POST** /rest/v1/rollouts/{rolloutId}/approve | Approve a Rollout
[**create**](RolloutsApi.md#create) | **POST** /rest/v1/rollouts | Create a new Rollout
[**delete**](RolloutsApi.md#delete) | **DELETE** /rest/v1/rollouts/{rolloutId} | Delete a Rollout
[**deny**](RolloutsApi.md#deny) | **POST** /rest/v1/rollouts/{rolloutId}/deny | Deny a Rollout
[**get_rollout**](RolloutsApi.md#get_rollout) | **GET** /rest/v1/rollouts/{rolloutId} | Return single Rollout
[**get_rollout_group**](RolloutsApi.md#get_rollout_group) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups/{groupId} | Return single rollout group
[**get_rollout_group_targets**](RolloutsApi.md#get_rollout_group_targets) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups/{groupId}/targets | Return all targets related to a specific rollout group
[**get_rollout_groups**](RolloutsApi.md#get_rollout_groups) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups | Return all rollout groups referred to a Rollout
[**get_rollouts**](RolloutsApi.md#get_rollouts) | **GET** /rest/v1/rollouts | Return all Rollouts
[**pause**](RolloutsApi.md#pause) | **POST** /rest/v1/rollouts/{rolloutId}/pause | Pause a Rollout
[**resume**](RolloutsApi.md#resume) | **POST** /rest/v1/rollouts/{rolloutId}/resume | Resume a Rollout
[**retry_rollout**](RolloutsApi.md#retry_rollout) | **POST** /rest/v1/rollouts/{rolloutId}/retry | Retry a rollout
[**start**](RolloutsApi.md#start) | **POST** /rest/v1/rollouts/{rolloutId}/start | Start a Rollout
[**trigger_next_group**](RolloutsApi.md#trigger_next_group) | **POST** /rest/v1/rollouts/{rolloutId}/triggerNextGroup | Force trigger processing next group of a Rollout
[**update**](RolloutsApi.md#update) | **PUT** /rest/v1/rollouts/{rolloutId} | Update Rollout

# **approve**
> approve(rollout_id, remark=remark)

Approve a Rollout

Handles the POST request of approving a created rollout. Only possible if approval workflow is enabled in system configuration and rollout is in state WAITING_FOR_APPROVAL. Required Permission: APPROVE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 
remark = 'remark_example' # str |  (optional)

try:
    # Approve a Rollout
    api_instance.approve(rollout_id, remark=remark)
except ApiException as e:
    print("Exception when calling RolloutsApi->approve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 
 **remark** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> MgmtRolloutResponseBody create(body)

Create a new Rollout

Handles the POST request of creating new rollout. Required Permission: CREATE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
body = swagger_client.MgmtRolloutRestRequestBodyPost() # MgmtRolloutRestRequestBodyPost | 

try:
    # Create a new Rollout
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtRolloutRestRequestBodyPost**](MgmtRolloutRestRequestBodyPost.md)|  | 

### Return type

[**MgmtRolloutResponseBody**](MgmtRolloutResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(rollout_id)

Delete a Rollout

Handles the DELETE request of deleting a rollout. Required Permission: DELETE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Delete a Rollout
    api_instance.delete(rollout_id)
except ApiException as e:
    print("Exception when calling RolloutsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deny**
> deny(rollout_id, remark=remark)

Deny a Rollout

Handles the POST request of denying a created rollout. Only possible if approval workflow is enabled in system configuration and rollout is in state WAITING_FOR_APPROVAL. Required Permission: APPROVE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 
remark = 'remark_example' # str |  (optional)

try:
    # Deny a Rollout
    api_instance.deny(rollout_id, remark=remark)
except ApiException as e:
    print("Exception when calling RolloutsApi->deny: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 
 **remark** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollout**
> MgmtRolloutResponseBody get_rollout(rollout_id)

Return single Rollout

Handles the GET request of retrieving a single rollout. Required Permission: READ_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Return single Rollout
    api_response = api_instance.get_rollout(rollout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->get_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

[**MgmtRolloutResponseBody**](MgmtRolloutResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollout_group**
> MgmtRolloutGroupResponseBody get_rollout_group(rollout_id, group_id)

Return single rollout group

Handles the GET request of a single deploy group of a specific rollout. Required Permission: READ_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 
group_id = 789 # int | 

try:
    # Return single rollout group
    api_response = api_instance.get_rollout_group(rollout_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->get_rollout_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 
 **group_id** | **int**|  | 

### Return type

[**MgmtRolloutGroupResponseBody**](MgmtRolloutGroupResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollout_group_targets**
> PagedListMgmtTarget get_rollout_group_targets(rollout_id, group_id, offset=offset, limit=limit, sort=sort, q=q)

Return all targets related to a specific rollout group

Handles the GET request of retrieving all targets of a single deploy group of a specific rollout. Required Permissions: READ_ROLLOUT, READ_TARGET.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 
group_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all targets related to a specific rollout group
    api_response = api_instance.get_rollout_group_targets(rollout_id, group_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->get_rollout_group_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 
 **group_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtTarget**](PagedListMgmtTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollout_groups**
> PagedListMgmtRolloutGroupResponseBody get_rollout_groups(rollout_id, offset=offset, limit=limit, sort=sort, q=q, representation=representation)

Return all rollout groups referred to a Rollout

Handles the GET request of retrieving all deploy groups of a specific rollout. Required Permission: READ_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)
representation = 'compact' # str |  (optional) (default to compact)

try:
    # Return all rollout groups referred to a Rollout
    api_response = api_instance.get_rollout_groups(rollout_id, offset=offset, limit=limit, sort=sort, q=q, representation=representation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->get_rollout_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 
 **representation** | **str**|  | [optional] [default to compact]

### Return type

[**PagedListMgmtRolloutGroupResponseBody**](PagedListMgmtRolloutGroupResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollouts**
> PagedListMgmtRolloutResponseBody get_rollouts(offset=offset, limit=limit, sort=sort, q=q, representation=representation)

Return all Rollouts

Handles the GET request of retrieving all rollouts. Required Permission: READ_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)
representation = 'compact' # str |  (optional) (default to compact)

try:
    # Return all Rollouts
    api_response = api_instance.get_rollouts(offset=offset, limit=limit, sort=sort, q=q, representation=representation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->get_rollouts: %s\n" % e)
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

[**PagedListMgmtRolloutResponseBody**](PagedListMgmtRolloutResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause**
> pause(rollout_id)

Pause a Rollout

Handles the POST request of pausing a running rollout. Required Permission: HANDLE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Pause a Rollout
    api_instance.pause(rollout_id)
except ApiException as e:
    print("Exception when calling RolloutsApi->pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume**
> resume(rollout_id)

Resume a Rollout

Handles the POST request of resuming a paused rollout. Required Permission: HANDLE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Resume a Rollout
    api_instance.resume(rollout_id)
except ApiException as e:
    print("Exception when calling RolloutsApi->resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_rollout**
> MgmtRolloutResponseBody retry_rollout(rollout_id)

Retry a rollout

Handles the POST request of retrying a rollout. Required Permission: CREATE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Retry a rollout
    api_response = api_instance.retry_rollout(rollout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->retry_rollout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

[**MgmtRolloutResponseBody**](MgmtRolloutResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(rollout_id)

Start a Rollout

Handles the POST request of starting a created rollout. Required Permission: HANDLE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Start a Rollout
    api_instance.start(rollout_id)
except ApiException as e:
    print("Exception when calling RolloutsApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_next_group**
> trigger_next_group(rollout_id)

Force trigger processing next group of a Rollout

Handles the POST request of triggering the next group of a rollout. Required Permission: UPDATE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
rollout_id = 789 # int | 

try:
    # Force trigger processing next group of a Rollout
    api_instance.trigger_next_group(rollout_id)
except ApiException as e:
    print("Exception when calling RolloutsApi->trigger_next_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollout_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> MgmtRolloutResponseBody update(body, rollout_id)

Update Rollout

Handles the UPDATE request for a single Rollout. Required permission: UPDATE_ROLLOUT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolloutsApi()
body = swagger_client.MgmtRolloutRestRequestBodyPut() # MgmtRolloutRestRequestBodyPut | 
rollout_id = 789 # int | 

try:
    # Update Rollout
    api_response = api_instance.update(body, rollout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolloutsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtRolloutRestRequestBodyPut**](MgmtRolloutRestRequestBodyPut.md)|  | 
 **rollout_id** | **int**|  | 

### Return type

[**MgmtRolloutResponseBody**](MgmtRolloutResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

