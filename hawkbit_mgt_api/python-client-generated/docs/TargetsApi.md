# swagger_client.TargetsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_auto_confirm**](TargetsApi.md#activate_auto_confirm) | **POST** /rest/v1/targets/{targetId}/autoConfirm/activate | Activate auto-confirm on a specific target
[**assign_target_type**](TargetsApi.md#assign_target_type) | **POST** /rest/v1/targets/{targetId}/targettype | Assign target type to a target
[**cancel_action**](TargetsApi.md#cancel_action) | **DELETE** /rest/v1/targets/{targetId}/actions/{actionId} | Cancel action for a specific target
[**create_metadata**](TargetsApi.md#create_metadata) | **POST** /rest/v1/targets/{targetId}/metadata | Create a list of meta data for a specific target
[**create_targets**](TargetsApi.md#create_targets) | **POST** /rest/v1/targets | Create target(s)
[**deactivate_auto_confirm**](TargetsApi.md#deactivate_auto_confirm) | **POST** /rest/v1/targets/{targetId}/autoConfirm/deactivate | Deactivate auto-confirm on a specific target
[**delete_metadata**](TargetsApi.md#delete_metadata) | **DELETE** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Deletes a single meta data entry from a target
[**delete_target**](TargetsApi.md#delete_target) | **DELETE** /rest/v1/targets/{targetId} | Delete target by id
[**get_action**](TargetsApi.md#get_action) | **GET** /rest/v1/targets/{targetId}/actions/{actionId} | Return action by id of a specific target
[**get_action_history**](TargetsApi.md#get_action_history) | **GET** /rest/v1/targets/{targetId}/actions | Return actions for a specific target
[**get_action_status_list**](TargetsApi.md#get_action_status_list) | **GET** /rest/v1/targets/{targetId}/actions/{actionId}/status | Return status of a specific action on a specific target
[**get_assigned_distribution_set**](TargetsApi.md#get_assigned_distribution_set) | **GET** /rest/v1/targets/{targetId}/assignedDS | Return the assigned distribution set of a specific target
[**get_attributes**](TargetsApi.md#get_attributes) | **GET** /rest/v1/targets/{targetId}/attributes | Return attributes of a specific target
[**get_auto_confirm_status**](TargetsApi.md#get_auto_confirm_status) | **GET** /rest/v1/targets/{targetId}/autoConfirm | Return the current auto-confitm state for a specific target
[**get_installed_distribution_set**](TargetsApi.md#get_installed_distribution_set) | **GET** /rest/v1/targets/{targetId}/installedDS | Return installed distribution set of a specific target
[**get_metadata**](TargetsApi.md#get_metadata) | **GET** /rest/v1/targets/{targetId}/metadata | Return metadata for specific target
[**get_metadata_value**](TargetsApi.md#get_metadata_value) | **GET** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Return single metadata value for a specific key of a target
[**get_tags**](TargetsApi.md#get_tags) | **GET** /rest/v1/targets/{targetId}/tags | Return tags for specific target
[**get_target**](TargetsApi.md#get_target) | **GET** /rest/v1/targets/{targetId} | Return target by id
[**get_targets**](TargetsApi.md#get_targets) | **GET** /rest/v1/targets | Return all targets
[**post_assigned_distribution_set**](TargetsApi.md#post_assigned_distribution_set) | **POST** /rest/v1/targets/{targetId}/assignedDS | Assigns a distribution set to a specific target
[**unassign_target_type**](TargetsApi.md#unassign_target_type) | **DELETE** /rest/v1/targets/{targetId}/targettype | Unassign target type from target.
[**update_action**](TargetsApi.md#update_action) | **PUT** /rest/v1/targets/{targetId}/actions/{actionId} | Switch an action from soft to forced
[**update_metadata**](TargetsApi.md#update_metadata) | **PUT** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Updates a single meta data value of a target
[**update_target**](TargetsApi.md#update_target) | **PUT** /rest/v1/targets/{targetId} | Update target by id

# **activate_auto_confirm**
> activate_auto_confirm(target_id, body=body)

Activate auto-confirm on a specific target

Handles the POST request to activate auto-confirmation for a specific target. As a result all current active as well as future actions will automatically be confirmed by mentioning the initiator as triggered person. Actions will be automatically confirmed, as long as auto-confirmation is active. Required Permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
body = swagger_client.MgmtTargetAutoConfirmUpdate() # MgmtTargetAutoConfirmUpdate |  (optional)

try:
    # Activate auto-confirm on a specific target
    api_instance.activate_auto_confirm(target_id, body=body)
except ApiException as e:
    print("Exception when calling TargetsApi->activate_auto_confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **body** | [**MgmtTargetAutoConfirmUpdate**](MgmtTargetAutoConfirmUpdate.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_target_type**
> assign_target_type(body, target_id)

Assign target type to a target

Assign or update the target type of a target. Required permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = swagger_client.MgmtId() # MgmtId | 
target_id = 'target_id_example' # str | 

try:
    # Assign target type to a target
    api_instance.assign_target_type(body, target_id)
except ApiException as e:
    print("Exception when calling TargetsApi->assign_target_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtId**](MgmtId.md)|  | 
 **target_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_action**
> cancel_action(target_id, action_id, force=force)

Cancel action for a specific target

Cancels an active action, only active actions can be deleted. Required Permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
action_id = 789 # int | 
force = false # bool |  (optional) (default to false)

try:
    # Cancel action for a specific target
    api_instance.cancel_action(target_id, action_id, force=force)
except ApiException as e:
    print("Exception when calling TargetsApi->cancel_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **action_id** | **int**|  | 
 **force** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata**
> list[MgmtMetadata] create_metadata(body, target_id)

Create a list of meta data for a specific target

Create a list of meta data entries Required permissions: READ_REPOSITORY and UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = [swagger_client.MgmtMetadata()] # list[MgmtMetadata] | 
target_id = 'target_id_example' # str | 

try:
    # Create a list of meta data for a specific target
    api_response = api_instance.create_metadata(body, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->create_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtMetadata]**](MgmtMetadata.md)|  | 
 **target_id** | **str**|  | 

### Return type

[**list[MgmtMetadata]**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_targets**
> list[MgmtTarget] create_targets(body)

Create target(s)

Handles the POST request of creating new targets. The request body must always be a list of targets. Required Permission: CREATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = [swagger_client.MgmtTargetRequestBody()] # list[MgmtTargetRequestBody] | 

try:
    # Create target(s)
    api_response = api_instance.create_targets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->create_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtTargetRequestBody]**](MgmtTargetRequestBody.md)|  | 

### Return type

[**list[MgmtTarget]**](MgmtTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_auto_confirm**
> deactivate_auto_confirm(target_id)

Deactivate auto-confirm on a specific target

Handles the POST request to deactivate auto-confirmation for a specific target. All active actions will remain unchanged while all future actions need to be confirmed, before processing with the deployment. Required Permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Deactivate auto-confirm on a specific target
    api_instance.deactivate_auto_confirm(target_id)
except ApiException as e:
    print("Exception when calling TargetsApi->deactivate_auto_confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata**
> delete_metadata(target_id, metadata_key)

Deletes a single meta data entry from a target

Delete a single meta data. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Deletes a single meta data entry from a target
    api_instance.delete_metadata(target_id, metadata_key)
except ApiException as e:
    print("Exception when calling TargetsApi->delete_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **metadata_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target**
> delete_target(target_id)

Delete target by id

Handles the DELETE request of deleting a single target. Required Permission: DELETE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Delete target by id
    api_instance.delete_target(target_id)
except ApiException as e:
    print("Exception when calling TargetsApi->delete_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action**
> MgmtAction get_action(target_id, action_id)

Return action by id of a specific target

Handles the GET request of retrieving a specific action on a specific target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
action_id = 789 # int | 

try:
    # Return action by id of a specific target
    api_response = api_instance.get_action(target_id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **action_id** | **int**|  | 

### Return type

[**MgmtAction**](MgmtAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_history**
> PagedListMgmtAction get_action_history(target_id, offset=offset, limit=limit, sort=sort, q=q)

Return actions for a specific target

Handles the GET request of retrieving the full action history of a specific target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return actions for a specific target
    api_response = api_instance.get_action_history(target_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_action_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtAction**](PagedListMgmtAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_action_status_list**
> PagedListMgmtActionStatus get_action_status_list(target_id, action_id, offset=offset, limit=limit, sort=sort)

Return status of a specific action on a specific target

Handles the GET request of retrieving a specific action on a specific target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
action_id = 789 # int | 
offset = 0 # int |  (optional) (default to 0)
limit = 50 # int |  (optional) (default to 50)
sort = 'sort_example' # str |  (optional)

try:
    # Return status of a specific action on a specific target
    api_response = api_instance.get_action_status_list(target_id, action_id, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_action_status_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **action_id** | **int**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **sort** | **str**|  | [optional] 

### Return type

[**PagedListMgmtActionStatus**](PagedListMgmtActionStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_distribution_set**
> MgmtDistributionSet get_assigned_distribution_set(target_id)

Return the assigned distribution set of a specific target

Handles the GET request of retrieving the assigned distribution set of an specific target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return the assigned distribution set of a specific target
    api_response = api_instance.get_assigned_distribution_set(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_assigned_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**MgmtDistributionSet**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> MgmtTargetAttributes get_attributes(target_id)

Return attributes of a specific target

Handles the GET request of retrieving the attributes of a specific target. Reponse is a key/value list. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return attributes of a specific target
    api_response = api_instance.get_attributes(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**MgmtTargetAttributes**](MgmtTargetAttributes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_confirm_status**
> MgmtTargetAutoConfirm get_auto_confirm_status(target_id)

Return the current auto-confitm state for a specific target

Handles the GET request to check the current auto-confirmation state of a target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return the current auto-confitm state for a specific target
    api_response = api_instance.get_auto_confirm_status(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_auto_confirm_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**MgmtTargetAutoConfirm**](MgmtTargetAutoConfirm.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installed_distribution_set**
> MgmtDistributionSet get_installed_distribution_set(target_id)

Return installed distribution set of a specific target

Handles the GET request of retrieving the installed distribution set of an specific target. Required Permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return installed distribution set of a specific target
    api_response = api_instance.get_installed_distribution_set(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_installed_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**MgmtDistributionSet**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> PagedListMgmtMetadata get_metadata(target_id, offset=offset, limit=limit, sort=sort, q=q)

Return metadata for specific target

Get a paged list of meta data for a target. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return metadata for specific target
    api_response = api_instance.get_metadata(target_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtMetadata**](PagedListMgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_value**
> MgmtMetadata get_metadata_value(target_id, metadata_key)

Return single metadata value for a specific key of a target

Get a single meta data value for a meta data key. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Return single metadata value for a specific key of a target
    api_response = api_instance.get_metadata_value(target_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_metadata_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtMetadata**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> list[MgmtTag] get_tags(target_id)

Return tags for specific target

Get a paged list of tags for a target. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return tags for specific target
    api_response = api_instance.get_tags(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**list[MgmtTag]**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target**
> MgmtTarget get_target(target_id)

Return target by id

Handles the GET request of retrieving a single target. Required Permission: READ_TARGET.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Return target by id
    api_response = api_instance.get_target(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

[**MgmtTarget**](MgmtTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_targets**
> PagedListMgmtTarget get_targets(offset=offset, limit=limit, sort=sort, q=q)

Return all targets

Handles the GET request of retrieving all targets. Required permission: READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all targets
    api_response = api_instance.get_targets(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->get_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **post_assigned_distribution_set**
> MgmtTargetAssignmentResponseBody post_assigned_distribution_set(body, target_id, offline=offline)

Assigns a distribution set to a specific target

Handles the POST request for assigning a distribution set to a specific target. Required Permission: READ_REPOSITORY and UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = [swagger_client.MgmtDistributionSetAssignment()] # list[MgmtDistributionSetAssignment] | 
target_id = 'target_id_example' # str | 
offline = 'offline_example' # str | Offline update (set param to true) that is only reported but not managed by the service, e.g. defaults set in factory, manual updates or migrations from other update systems. A completed action is added to the history of the target(s). Target is set to IN_SYNC state as both assigned and installed DS are set. Note: only executed if the target has currently no running update (optional)

try:
    # Assigns a distribution set to a specific target
    api_response = api_instance.post_assigned_distribution_set(body, target_id, offline=offline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->post_assigned_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtDistributionSetAssignment]**](MgmtDistributionSetAssignment.md)|  | 
 **target_id** | **str**|  | 
 **offline** | **str**| Offline update (set param to true) that is only reported but not managed by the service, e.g. defaults set in factory, manual updates or migrations from other update systems. A completed action is added to the history of the target(s). Target is set to IN_SYNC state as both assigned and installed DS are set. Note: only executed if the target has currently no running update | [optional] 

### Return type

[**MgmtTargetAssignmentResponseBody**](MgmtTargetAssignmentResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_target_type**
> unassign_target_type(target_id)

Unassign target type from target.

Remove the target type from a target. The target type will be set to null. Required permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
target_id = 'target_id_example' # str | 

try:
    # Unassign target type from target.
    api_instance.unassign_target_type(target_id)
except ApiException as e:
    print("Exception when calling TargetsApi->unassign_target_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_action**
> MgmtAction update_action(body, target_id, action_id)

Switch an action from soft to forced

Handles the PUT request to switch an action from soft to forced. Required Permission: UPDATE_TARGET.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = swagger_client.MgmtActionRequestBodyPut() # MgmtActionRequestBodyPut | 
target_id = 'target_id_example' # str | 
action_id = 789 # int | 

try:
    # Switch an action from soft to forced
    api_response = api_instance.update_action(body, target_id, action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->update_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtActionRequestBodyPut**](MgmtActionRequestBodyPut.md)|  | 
 **target_id** | **str**|  | 
 **action_id** | **int**|  | 

### Return type

[**MgmtAction**](MgmtAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata**
> MgmtMetadata update_metadata(body, target_id, metadata_key)

Updates a single meta data value of a target

Update a single meta data value for speficic key. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = swagger_client.MgmtMetadataBodyPut() # MgmtMetadataBodyPut | 
target_id = 'target_id_example' # str | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Updates a single meta data value of a target
    api_response = api_instance.update_metadata(body, target_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->update_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtMetadataBodyPut**](MgmtMetadataBodyPut.md)|  | 
 **target_id** | **str**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtMetadata**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target**
> MgmtTarget update_target(body, target_id)

Update target by id

Handles the PUT request of updating a target. Required Permission: UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetsApi()
body = swagger_client.MgmtTargetRequestBody() # MgmtTargetRequestBody | 
target_id = 'target_id_example' # str | 

try:
    # Update target by id
    api_response = api_instance.update_target(body, target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetsApi->update_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTargetRequestBody**](MgmtTargetRequestBody.md)|  | 
 **target_id** | **str**|  | 

### Return type

[**MgmtTarget**](MgmtTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

