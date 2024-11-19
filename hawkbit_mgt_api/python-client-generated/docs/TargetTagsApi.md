# swagger_client.TargetTagsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_targets**](TargetTagsApi.md#assign_targets) | **POST** /rest/v1/targettags/{targetTagId}/assigned | Assign target(s) to given tagId and return targets
[**assign_targets_by_controller_ids**](TargetTagsApi.md#assign_targets_by_controller_ids) | **PUT** /rest/v1/targettags/{targetTagId}/assigned | Assign target(s) to given tagId
[**create_target_tags**](TargetTagsApi.md#create_target_tags) | **POST** /rest/v1/targettags | Create target tag(s)
[**delete_target_tag**](TargetTagsApi.md#delete_target_tag) | **DELETE** /rest/v1/targettags/{targetTagId} | Delete target tag by id
[**get_assigned_targets**](TargetTagsApi.md#get_assigned_targets) | **GET** /rest/v1/targettags/{targetTagId}/assigned | Return assigned targets for tag
[**get_target_tag**](TargetTagsApi.md#get_target_tag) | **GET** /rest/v1/targettags/{targetTagId} | Return target tag by id
[**get_target_tags**](TargetTagsApi.md#get_target_tags) | **GET** /rest/v1/targettags | Return all target tags
[**toggle_tag_assignment**](TargetTagsApi.md#toggle_tag_assignment) | **POST** /rest/v1/targettags/{targetTagId}/assigned/toggleTagAssignment | Toggles target tag assignment
[**unassign_target**](TargetTagsApi.md#unassign_target) | **DELETE** /rest/v1/targettags/{targetTagId}/assigned/{controllerId} | Unassign target from a given tagId
[**update_target_tag**](TargetTagsApi.md#update_target_tag) | **PUT** /rest/v1/targettags/{targetTagId} | Update target tag by id

# **assign_targets**
> list[MgmtTarget] assign_targets(body, target_tag_id)

Assign target(s) to given tagId and return targets

Handles the POST request of target assignment. Already assigned target will be ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
body = [swagger_client.MgmtAssignedTargetRequestBody()] # list[MgmtAssignedTargetRequestBody] | 
target_tag_id = 789 # int | 

try:
    # Assign target(s) to given tagId and return targets
    api_response = api_instance.assign_targets(body, target_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->assign_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtAssignedTargetRequestBody]**](MgmtAssignedTargetRequestBody.md)|  | 
 **target_tag_id** | **int**|  | 

### Return type

[**list[MgmtTarget]**](MgmtTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_targets_by_controller_ids**
> assign_targets_by_controller_ids(body, target_tag_id)

Assign target(s) to given tagId

Handles the POST request of target assignment. Already assigned target will be ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
body = 'body_example' # str | 
target_tag_id = 789 # int | 

try:
    # Assign target(s) to given tagId
    api_instance.assign_targets_by_controller_ids(body, target_tag_id)
except ApiException as e:
    print("Exception when calling TargetTagsApi->assign_targets_by_controller_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **target_tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_target_tags**
> list[MgmtTag] create_target_tags(body)

Create target tag(s)

Handles the POST request of creating new target tag. The request body must always be a list of target tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
body = [swagger_client.MgmtTagRequestBodyPut()] # list[MgmtTagRequestBodyPut] | 

try:
    # Create target tag(s)
    api_response = api_instance.create_target_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->create_target_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtTagRequestBodyPut]**](MgmtTagRequestBodyPut.md)|  | 

### Return type

[**list[MgmtTag]**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target_tag**
> delete_target_tag(target_tag_id)

Delete target tag by id

Handles the DELETE request of deleting a single target tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
target_tag_id = 789 # int | 

try:
    # Delete target tag by id
    api_instance.delete_target_tag(target_tag_id)
except ApiException as e:
    print("Exception when calling TargetTagsApi->delete_target_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_targets**
> PagedListMgmtTarget get_assigned_targets(target_tag_id, offset=offset, limit=limit, sort=sort, q=q)

Return assigned targets for tag

Handles the GET request of retrieving a list of assigned targets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
target_tag_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return assigned targets for tag
    api_response = api_instance.get_assigned_targets(target_tag_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->get_assigned_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_tag_id** | **int**|  | 
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

# **get_target_tag**
> MgmtTag get_target_tag(target_tag_id)

Return target tag by id

Handles the GET request of retrieving a single target tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
target_tag_id = 789 # int | 

try:
    # Return target tag by id
    api_response = api_instance.get_target_tag(target_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->get_target_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_tag_id** | **int**|  | 

### Return type

[**MgmtTag**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_tags**
> PagedListMgmtTag get_target_tags(offset=offset, limit=limit, sort=sort, q=q)

Return all target tags

Handles the GET request of retrieving all target tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all target tags
    api_response = api_instance.get_target_tags(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->get_target_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtTag**](PagedListMgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_tag_assignment**
> MgmtTargetTagAssigmentResult toggle_tag_assignment(body, target_tag_id)

Toggles target tag assignment

Handles the POST request of toggle target assignment. The request body must always be a list of controller ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
body = [swagger_client.MgmtAssignedTargetRequestBody()] # list[MgmtAssignedTargetRequestBody] | 
target_tag_id = 789 # int | 

try:
    # Toggles target tag assignment
    api_response = api_instance.toggle_tag_assignment(body, target_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->toggle_tag_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtAssignedTargetRequestBody]**](MgmtAssignedTargetRequestBody.md)|  | 
 **target_tag_id** | **int**|  | 

### Return type

[**MgmtTargetTagAssigmentResult**](MgmtTargetTagAssigmentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_target**
> unassign_target(target_tag_id, controller_id)

Unassign target from a given tagId

Handles the DELETE request to unassign the given target.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
target_tag_id = 789 # int | 
controller_id = 'controller_id_example' # str | 

try:
    # Unassign target from a given tagId
    api_instance.unassign_target(target_tag_id, controller_id)
except ApiException as e:
    print("Exception when calling TargetTagsApi->unassign_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_tag_id** | **int**|  | 
 **controller_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_tag**
> MgmtTag update_target_tag(body, target_tag_id)

Update target tag by id

Handles the PUT request of updating a target tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TargetTagsApi()
body = swagger_client.MgmtTagRequestBodyPut() # MgmtTagRequestBodyPut | 
target_tag_id = 789 # int | 

try:
    # Update target tag by id
    api_response = api_instance.update_target_tag(body, target_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TargetTagsApi->update_target_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTagRequestBodyPut**](MgmtTagRequestBodyPut.md)|  | 
 **target_tag_id** | **int**|  | 

### Return type

[**MgmtTag**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

