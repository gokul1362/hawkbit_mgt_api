# swagger_client.DistributionSetsApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_software_modules**](DistributionSetsApi.md#assign_software_modules) | **POST** /rest/v1/distributionsets/{distributionSetId}/assignedSM | Assign a list of software modules to a distribution set
[**create_assigned_target**](DistributionSetsApi.md#create_assigned_target) | **POST** /rest/v1/distributionsets/{distributionSetId}/assignedTargets | Assigning multiple targets to a single distribution set
[**create_distribution_sets**](DistributionSetsApi.md#create_distribution_sets) | **POST** /rest/v1/distributionsets | Creates new Distribution Sets
[**create_metadata2**](DistributionSetsApi.md#create_metadata2) | **POST** /rest/v1/distributionsets/{distributionSetId}/metadata | Create a list of meta data for a specific distribution set
[**delete_assign_software_modules**](DistributionSetsApi.md#delete_assign_software_modules) | **DELETE** /rest/v1/distributionsets/{distributionSetId}/assignedSM/{softwareModuleId} | Delete the assignment of the software module from the distribution set
[**delete_distribution_set**](DistributionSetsApi.md#delete_distribution_set) | **DELETE** /rest/v1/distributionsets/{distributionSetId} | Delete Distribution Set by Id
[**delete_metadata2**](DistributionSetsApi.md#delete_metadata2) | **DELETE** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Delete a single meta data entry from the distribution set
[**get_actions_count_by_status_for_distribution_set**](DistributionSetsApi.md#get_actions_count_by_status_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/actions | Return Actions count by status for Distribution Set
[**get_assigned_software_modules**](DistributionSetsApi.md#get_assigned_software_modules) | **GET** /rest/v1/distributionsets/{distributionSetId}/assignedSM | Return the assigned software modules of a specific distribution set
[**get_assigned_targets1**](DistributionSetsApi.md#get_assigned_targets1) | **GET** /rest/v1/distributionsets/{distributionSetId}/assignedTargets | Return assigned targets to a specific distribution set
[**get_auto_assign_target_filter_queries**](DistributionSetsApi.md#get_auto_assign_target_filter_queries) | **GET** /rest/v1/distributionsets/{distributionSetId}/autoAssignTargetFilters | Return target filter queries that have the given distribution set as auto assign DS
[**get_auto_assignments_count_for_distribution_set**](DistributionSetsApi.md#get_auto_assignments_count_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/autoassignments | Return Auto Assignments count for Distribution Set
[**get_distribution_set**](DistributionSetsApi.md#get_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId} | Return single Distribution Set
[**get_distribution_sets**](DistributionSetsApi.md#get_distribution_sets) | **GET** /rest/v1/distributionsets | Return all Distribution Sets
[**get_installed_targets**](DistributionSetsApi.md#get_installed_targets) | **GET** /rest/v1/distributionsets/{distributionSetId}/installedTargets | Return installed targets to a specific distribution set
[**get_metadata2**](DistributionSetsApi.md#get_metadata2) | **GET** /rest/v1/distributionsets/{distributionSetId}/metadata | Return meta data for Distribution Set
[**get_metadata_value2**](DistributionSetsApi.md#get_metadata_value2) | **GET** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Return single meta data value for a specific key of a Distribution Set
[**get_rollouts_count_by_status_for_distribution_set**](DistributionSetsApi.md#get_rollouts_count_by_status_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/rollouts | Return Rollouts count by status for Distribution Set
[**get_statistics_for_distribution_set**](DistributionSetsApi.md#get_statistics_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics | Return Rollouts, Actions and Auto Assignments counts by Status for Distribution Set
[**invalidate_distribution_set**](DistributionSetsApi.md#invalidate_distribution_set) | **POST** /rest/v1/distributionsets/{distributionSetId}/invalidate | Invalidate a distribution set
[**update_distribution_set**](DistributionSetsApi.md#update_distribution_set) | **PUT** /rest/v1/distributionsets/{distributionSetId} | Update Distribution Set
[**update_metadata2**](DistributionSetsApi.md#update_metadata2) | **PUT** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Update single meta data value of a distribution set

# **assign_software_modules**
> assign_software_modules(body, distribution_set_id)

Assign a list of software modules to a distribution set

Handles the POST request for assigning multiple software modules to a distribution set.The request body must always be a list of software module IDs. Required permissions: READ_REPOSITORY and UPDATE_REPOSITORY 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = [swagger_client.MgmtSoftwareModuleAssigment()] # list[MgmtSoftwareModuleAssigment] | 
distribution_set_id = 789 # int | 

try:
    # Assign a list of software modules to a distribution set
    api_instance.assign_software_modules(body, distribution_set_id)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->assign_software_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtSoftwareModuleAssigment]**](MgmtSoftwareModuleAssigment.md)|  | 
 **distribution_set_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assigned_target**
> MgmtTargetAssignmentResponseBody create_assigned_target(body, distribution_set_id, offline=offline)

Assigning multiple targets to a single distribution set

Handles the POST request for assigning multiple targets to a distribution set.The request body must always be a list of target IDs. Non-existing targets are silently ignored resulting in a valid response. Required permissions: READ_REPOSITORY and UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = [swagger_client.MgmtTargetAssignmentRequestBody()] # list[MgmtTargetAssignmentRequestBody] | 
distribution_set_id = 789 # int | 
offline = true # bool |  (optional)

try:
    # Assigning multiple targets to a single distribution set
    api_response = api_instance.create_assigned_target(body, distribution_set_id, offline=offline)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->create_assigned_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtTargetAssignmentRequestBody]**](MgmtTargetAssignmentRequestBody.md)|  | 
 **distribution_set_id** | **int**|  | 
 **offline** | **bool**|  | [optional] 

### Return type

[**MgmtTargetAssignmentResponseBody**](MgmtTargetAssignmentResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_distribution_sets**
> list[MgmtDistributionSet] create_distribution_sets(body)

Creates new Distribution Sets

Handles the POST request of creating new distribution sets within Hawkbit. The request body must always be a list of sets. Required permission: CREATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = [swagger_client.MgmtDistributionSetRequestBodyPost()] # list[MgmtDistributionSetRequestBodyPost] | 

try:
    # Creates new Distribution Sets
    api_response = api_instance.create_distribution_sets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->create_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtDistributionSetRequestBodyPost]**](MgmtDistributionSetRequestBodyPost.md)|  | 

### Return type

[**list[MgmtDistributionSet]**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata2**
> list[MgmtMetadata] create_metadata2(body, distribution_set_id)

Create a list of meta data for a specific distribution set

Create a list of meta data entries Required permissions: READ_REPOSITORY and UPDATE_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = [swagger_client.MgmtMetadata()] # list[MgmtMetadata] | 
distribution_set_id = 789 # int | 

try:
    # Create a list of meta data for a specific distribution set
    api_response = api_instance.create_metadata2(body, distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->create_metadata2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MgmtMetadata]**](MgmtMetadata.md)|  | 
 **distribution_set_id** | **int**|  | 

### Return type

[**list[MgmtMetadata]**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assign_software_modules**
> delete_assign_software_modules(distribution_set_id, software_module_id)

Delete the assignment of the software module from the distribution set

Delete an assignment. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
software_module_id = 789 # int | 

try:
    # Delete the assignment of the software module from the distribution set
    api_instance.delete_assign_software_modules(distribution_set_id, software_module_id)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->delete_assign_software_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
 **software_module_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_distribution_set**
> delete_distribution_set(distribution_set_id)

Delete Distribution Set by Id

Handles the DELETE request for a single Distribution Set. Required permission: DELETE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Delete Distribution Set by Id
    api_instance.delete_distribution_set(distribution_set_id)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->delete_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata2**
> delete_metadata2(distribution_set_id, metadata_key)

Delete a single meta data entry from the distribution set

Delete a single meta data. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Delete a single meta data entry from the distribution set
    api_instance.delete_metadata2(distribution_set_id, metadata_key)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->delete_metadata2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_count_by_status_for_distribution_set**
> MgmtDistributionSetStatistics get_actions_count_by_status_for_distribution_set(distribution_set_id)

Return Actions count by status for Distribution Set

Handles the GET request of retrieving Actions count by Status for Distribution Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Return Actions count by status for Distribution Set
    api_response = api_instance.get_actions_count_by_status_for_distribution_set(distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_actions_count_by_status_for_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSetStatistics**](MgmtDistributionSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_software_modules**
> PagedListMgmtSoftwareModule get_assigned_software_modules(distribution_set_id, offset=offset, limit=limit, sort=sort)

Return the assigned software modules of a specific distribution set

Handles the GET request of retrieving a single distribution set. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)

try:
    # Return the assigned software modules of a specific distribution set
    api_response = api_instance.get_assigned_software_modules(distribution_set_id, offset=offset, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_assigned_software_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 

### Return type

[**PagedListMgmtSoftwareModule**](PagedListMgmtSoftwareModule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_targets1**
> PagedListMgmtTarget get_assigned_targets1(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)

Return assigned targets to a specific distribution set

Handles the GET request for retrieving assigned targets of a single distribution set. Required permissions: READ_REPOSITORY and READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return assigned targets to a specific distribution set
    api_response = api_instance.get_assigned_targets1(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_assigned_targets1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
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

# **get_auto_assign_target_filter_queries**
> PagedListMgmtTargetFilterQuery get_auto_assign_target_filter_queries(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)

Return target filter queries that have the given distribution set as auto assign DS

Handles the GET request for retrieving assigned target filter queries of a single distribution set. Required permissions: READ_REPOSITORY and READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return target filter queries that have the given distribution set as auto assign DS
    api_response = api_instance.get_auto_assign_target_filter_queries(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_auto_assign_target_filter_queries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
 **offset** | **str**| The paging offset (default is 0) | [optional] 
 **limit** | **str**| The maximum number of entries in a page (default is 50) | [optional] 
 **sort** | **str**| The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. | [optional] 
 **q** | **str**| Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. | [optional] 

### Return type

[**PagedListMgmtTargetFilterQuery**](PagedListMgmtTargetFilterQuery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_assignments_count_for_distribution_set**
> MgmtDistributionSetStatistics get_auto_assignments_count_for_distribution_set(distribution_set_id)

Return Auto Assignments count for Distribution Set

Handles the GET request of retrieving Auto Assignments count for Distribution Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Return Auto Assignments count for Distribution Set
    api_response = api_instance.get_auto_assignments_count_for_distribution_set(distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_auto_assignments_count_for_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSetStatistics**](MgmtDistributionSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_set**
> MgmtDistributionSet get_distribution_set(distribution_set_id)

Return single Distribution Set

Handles the GET request of retrieving a single distribution set. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Return single Distribution Set
    api_response = api_instance.get_distribution_set(distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSet**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distribution_sets**
> PagedListMgmtDistributionSet get_distribution_sets(offset=offset, limit=limit, sort=sort, q=q)

Return all Distribution Sets

Handles the GET request of retrieving all distribution sets. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return all Distribution Sets
    api_response = api_instance.get_distribution_sets(offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_distribution_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_installed_targets**
> PagedListMgmtTarget get_installed_targets(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)

Return installed targets to a specific distribution set

Handles the GET request for retrieving installed targets of a single distribution set. Required permissions: READ_REPOSITORY and READ_TARGET

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return installed targets to a specific distribution set
    api_response = api_instance.get_installed_targets(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_installed_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
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

# **get_metadata2**
> PagedListMgmtMetadata get_metadata2(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)

Return meta data for Distribution Set

Get a paged list of meta data for a distribution set. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
offset = 'offset_example' # str | The paging offset (default is 0) (optional)
limit = 'limit_example' # str | The maximum number of entries in a page (default is 50) (optional)
sort = 'sort_example' # str | The query parameter sort allows to define the sort order for the result of a query. A sort criteria consists of the name of a field and the sort direction (ASC for ascending and DESC descending). The sequence of the sort criteria (multiple can be used) defines the sort order of the entities in the result. (optional)
q = 'q_example' # str | Query fields based on the Feed Item Query Language (FIQL). See Entity Definitions for available fields. (optional)

try:
    # Return meta data for Distribution Set
    api_response = api_instance.get_metadata2(distribution_set_id, offset=offset, limit=limit, sort=sort, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_metadata2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
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

# **get_metadata_value2**
> MgmtMetadata get_metadata_value2(distribution_set_id, metadata_key)

Return single meta data value for a specific key of a Distribution Set

Get a single meta data value for a meta data key. Required permission: READ_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Return single meta data value for a specific key of a Distribution Set
    api_response = api_instance.get_metadata_value2(distribution_set_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_metadata_value2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtMetadata**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rollouts_count_by_status_for_distribution_set**
> MgmtDistributionSetStatistics get_rollouts_count_by_status_for_distribution_set(distribution_set_id)

Return Rollouts count by status for Distribution Set

Handles the GET request of retrieving Rollouts count by Status for Distribution Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Return Rollouts count by status for Distribution Set
    api_response = api_instance.get_rollouts_count_by_status_for_distribution_set(distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_rollouts_count_by_status_for_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSetStatistics**](MgmtDistributionSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_for_distribution_set**
> MgmtDistributionSetStatistics get_statistics_for_distribution_set(distribution_set_id)

Return Rollouts, Actions and Auto Assignments counts by Status for Distribution Set

Handles the GET request of retrieving Rollouts, Actions and Auto Assignments counts by Status for Distribution Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
distribution_set_id = 789 # int | 

try:
    # Return Rollouts, Actions and Auto Assignments counts by Status for Distribution Set
    api_response = api_instance.get_statistics_for_distribution_set(distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->get_statistics_for_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSetStatistics**](MgmtDistributionSetStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_distribution_set**
> invalidate_distribution_set(body, distribution_set_id)

Invalidate a distribution set

Invalidate a distribution set. Once a distribution set is invalidated, it can not be valid again. An invalidated distribution set cannot be assigned to targets anymore. The distribution set that is going to be invalidated will be removed from all auto assignments. Furthermore, the user can choose to cancel all rollouts and (force) cancel all actions connected to this distribution set. Required permission: UPDATE_REPOSITORY, UPDATE_TARGET 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = swagger_client.MgmtInvalidateDistributionSetRequestBody() # MgmtInvalidateDistributionSetRequestBody | 
distribution_set_id = 789 # int | 

try:
    # Invalidate a distribution set
    api_instance.invalidate_distribution_set(body, distribution_set_id)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->invalidate_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtInvalidateDistributionSetRequestBody**](MgmtInvalidateDistributionSetRequestBody.md)|  | 
 **distribution_set_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_distribution_set**
> MgmtDistributionSet update_distribution_set(body, distribution_set_id)

Update Distribution Set

Handles the UPDATE request for a single Distribution Set. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = swagger_client.MgmtDistributionSetRequestBodyPut() # MgmtDistributionSetRequestBodyPut | 
distribution_set_id = 789 # int | 

try:
    # Update Distribution Set
    api_response = api_instance.update_distribution_set(body, distribution_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->update_distribution_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtDistributionSetRequestBodyPut**](MgmtDistributionSetRequestBodyPut.md)|  | 
 **distribution_set_id** | **int**|  | 

### Return type

[**MgmtDistributionSet**](MgmtDistributionSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata2**
> MgmtMetadata update_metadata2(body, distribution_set_id, metadata_key)

Update single meta data value of a distribution set

Update a single meta data value for speficic key. Required permission: UPDATE_REPOSITORY

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DistributionSetsApi()
body = swagger_client.MgmtMetadataBodyPut() # MgmtMetadataBodyPut | 
distribution_set_id = 789 # int | 
metadata_key = 'metadata_key_example' # str | 

try:
    # Update single meta data value of a distribution set
    api_response = api_instance.update_metadata2(body, distribution_set_id, metadata_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionSetsApi->update_metadata2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtMetadataBodyPut**](MgmtMetadataBodyPut.md)|  | 
 **distribution_set_id** | **int**|  | 
 **metadata_key** | **str**|  | 

### Return type

[**MgmtMetadata**](MgmtMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

