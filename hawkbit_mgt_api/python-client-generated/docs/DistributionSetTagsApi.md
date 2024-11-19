# swagger_client.DistributionSetTagsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_distribution_sets**](DistributionSetTagsApi.md#assign_distribution_sets) | **POST** /rest/v1/distributionsettags/{distributionsetTagId}/assigned | Assign distribution sets to the given tag id
[**create_distribution_set_tags**](DistributionSetTagsApi.md#create_distribution_set_tags) | **POST** /rest/v1/distributionsettags | Creates new Distribution Set Tags
[**delete_distribution_set_tag**](DistributionSetTagsApi.md#delete_distribution_set_tag) | **DELETE** /rest/v1/distributionsettags/{distributionsetTagId} | Delete a single distribution set tag
[**get_assigned_distribution_sets**](DistributionSetTagsApi.md#get_assigned_distribution_sets) | **GET** /rest/v1/distributionsettags/{distributionsetTagId}/assigned | Return all assigned distribution sets by given tag Id
[**get_distribution_set_tag**](DistributionSetTagsApi.md#get_distribution_set_tag) | **GET** /rest/v1/distributionsettags/{distributionsetTagId} | Return single Distribution Set Tag
[**get_distribution_set_tags**](DistributionSetTagsApi.md#get_distribution_set_tags) | **GET** /rest/v1/distributionsettags | Return all Distribution Set Tags
[**toggle_tag_assignment1**](DistributionSetTagsApi.md#toggle_tag_assignment1) | **POST** /rest/v1/distributionsettags/{distributionsetTagId}/assigned/toggleTagAssignment | Toggle the assignment of distribution sets by the given tag id
[**unassign_distribution_set**](DistributionSetTagsApi.md#unassign_distribution_set) | **DELETE** /rest/v1/distributionsettags/{distributionsetTagId}/assigned/{distributionsetId} | Unassign one distribution set from the given tag id
[**update_distribution_set_tag**](DistributionSetTagsApi.md#update_distribution_set_tag) | **PUT** /rest/v1/distributionsettags/{distributionsetTagId} | Update Distribution Set Tag

# **assign_distribution_sets**
> list[MgmtDistributionSet] assign_distribution_sets(body, distributionset_tag_id)

Assign distribution sets to the given tag id

Handles the POST request of distribution assignment. Already assigned distribution will be ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
body = [swagger_client.MgmtAssignedDistributionSetRequestBody()] # list[MgmtAssignedDistributionSetRequestBody] | 
distributionset_tag_id = 789 # int | 

try:
    # Assign distribution sets to the given tag id
    api_response = api_instance.assign_distribution_sets(body, distributionset_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->assign_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtAssignedDistributionSetRequestBody]**](MgmtAssignedDistributionSetRequestBody.md)|  | 
 **distributionset_tag_id** | **int**|  | 

### Return type

[**list[MgmtDistributionSet]**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_distribution_set_tags**
> list[MgmtTag] create_distribution_set_tags(body)

Creates new Distribution Set Tags

Handles the POST request of creating new distribution set tag. The request body must always be a list of distribution set tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
body = [swagger_client.MgmtTagRequestBodyPut()] # list[MgmtTagRequestBodyPut] | 

try:
    # Creates new Distribution Set Tags
    api_response = api_instance.create_distribution_set_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->create_distribution_set_tags: %s\n" % e)
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

# **delete_distribution_set_tag**
> delete_distribution_set_tag(distributionset_tag_id)

Delete a single distribution set tag

Handles the DELETE request of deleting a single distribution set tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
distributionset_tag_id = 789 # int | 

try:
    # Delete a single distribution set tag
    api_instance.delete_distribution_set_tag(distributionset_tag_id)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->delete_distribution_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distributionset_tag_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_distribution_sets**
> PagedListMgmtDistributionSet get_assigned_distribution_sets(distributionset_tag_id, offset=offset, limit=limit, sort=sort, q=q)

Return all assigned distribution sets by given tag Id

Handles the GET request of retrieving a list of assigned distributions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
distributionset_tag_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all assigned distribution sets by given tag Id
    api_response = api_instance.get_assigned_distribution_sets(distributionset_tag_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->get_assigned_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distributionset_tag_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtDistributionSet**](PagedListMgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_set_tag**
> MgmtTag get_distribution_set_tag(distributionset_tag_id)

Return single Distribution Set Tag

Handles the GET request of retrieving a single distribution set tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
distributionset_tag_id = 789 # int | 

try:
    # Return single Distribution Set Tag
    api_response = api_instance.get_distribution_set_tag(distributionset_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->get_distribution_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distributionset_tag_id** | **int**|  | 

### Return type

[**MgmtTag**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_set_tags**
> PagedListMgmtTag get_distribution_set_tags(offset=offset, limit=limit, sort=sort, q=q)

Return all Distribution Set Tags

Handles the GET request of retrieving all distribution set tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all Distribution Set Tags
    api_response = api_instance.get_distribution_set_tags(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->get_distribution_set_tags: %s\n" % e)
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

# **toggle_tag_assignment1**
> MgmtDistributionSetTagAssigmentResult toggle_tag_assignment1(body, distributionset_tag_id)

Toggle the assignment of distribution sets by the given tag id

Handles the POST request of toggle distribution assignment. The request body must always be a list of distribution set ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
body = [swagger_client.MgmtAssignedDistributionSetRequestBody()] # list[MgmtAssignedDistributionSetRequestBody] | 
distributionset_tag_id = 789 # int | 

try:
    # Toggle the assignment of distribution sets by the given tag id
    api_response = api_instance.toggle_tag_assignment1(body, distributionset_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->toggle_tag_assignment1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtAssignedDistributionSetRequestBody]**](MgmtAssignedDistributionSetRequestBody.md)|  | 
 **distributionset_tag_id** | **int**|  | 

### Return type

[**MgmtDistributionSetTagAssigmentResult**](MgmtDistributionSetTagAssigmentResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_distribution_set**
> unassign_distribution_set(distributionset_tag_id, distributionset_id)

Unassign one distribution set from the given tag id

Handles the DELETE request of unassign the given distribution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
distributionset_tag_id = 789 # int | 
distributionset_id = 789 # int | 

try:
    # Unassign one distribution set from the given tag id
    api_instance.unassign_distribution_set(distributionset_tag_id, distributionset_id)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->unassign_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distributionset_tag_id** | **int**|  | 
 **distributionset_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_distribution_set_tag**
> MgmtTag update_distribution_set_tag(body, distributionset_tag_id)

Update Distribution Set Tag

Handles the PUT request of updating a distribution set tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetTagsApi()
body = swagger_client.MgmtTagRequestBodyPut() # MgmtTagRequestBodyPut | 
distributionset_tag_id = 789 # int | 

try:
    # Update Distribution Set Tag
    api_response = api_instance.update_distribution_set_tag(body, distributionset_tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetTagsApi->update_distribution_set_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtTagRequestBodyPut**](MgmtTagRequestBodyPut.md)|  | 
 **distributionset_tag_id** | **int**|  | 

### Return type

[**MgmtTag**](MgmtTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

