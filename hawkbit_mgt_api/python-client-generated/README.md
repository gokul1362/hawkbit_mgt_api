# swagger-client
Eclipse hawkBit™ is a domain-independent back-end framework for rolling out software updates to constrained edge devices as well as more powerful controllers and gateways connected to IP based networking infrastructure. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
action_id = 789 # int | 

try:
    # Return action by id
    api_response = api_instance.get_action1(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionsApi->get_action1: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ActionsApi(swagger_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *http://localhost:59874*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActionsApi* | [**get_action1**](docs/ActionsApi.md#get_action1) | **GET** /rest/v1/actions/{actionId} | Return action by id
*ActionsApi* | [**get_actions**](docs/ActionsApi.md#get_actions) | **GET** /rest/v1/actions | Return all actions
*BasicAuthenticationApi* | [**validate_basic_auth**](docs/BasicAuthenticationApi.md#validate_basic_auth) | **GET** /rest/v1/userinfo | 
*DistributionSetTagsApi* | [**assign_distribution_sets**](docs/DistributionSetTagsApi.md#assign_distribution_sets) | **POST** /rest/v1/distributionsettags/{distributionsetTagId}/assigned | Assign distribution sets to the given tag id
*DistributionSetTagsApi* | [**create_distribution_set_tags**](docs/DistributionSetTagsApi.md#create_distribution_set_tags) | **POST** /rest/v1/distributionsettags | Creates new Distribution Set Tags
*DistributionSetTagsApi* | [**delete_distribution_set_tag**](docs/DistributionSetTagsApi.md#delete_distribution_set_tag) | **DELETE** /rest/v1/distributionsettags/{distributionsetTagId} | Delete a single distribution set tag
*DistributionSetTagsApi* | [**get_assigned_distribution_sets**](docs/DistributionSetTagsApi.md#get_assigned_distribution_sets) | **GET** /rest/v1/distributionsettags/{distributionsetTagId}/assigned | Return all assigned distribution sets by given tag Id
*DistributionSetTagsApi* | [**get_distribution_set_tag**](docs/DistributionSetTagsApi.md#get_distribution_set_tag) | **GET** /rest/v1/distributionsettags/{distributionsetTagId} | Return single Distribution Set Tag
*DistributionSetTagsApi* | [**get_distribution_set_tags**](docs/DistributionSetTagsApi.md#get_distribution_set_tags) | **GET** /rest/v1/distributionsettags | Return all Distribution Set Tags
*DistributionSetTagsApi* | [**toggle_tag_assignment1**](docs/DistributionSetTagsApi.md#toggle_tag_assignment1) | **POST** /rest/v1/distributionsettags/{distributionsetTagId}/assigned/toggleTagAssignment | Toggle the assignment of distribution sets by the given tag id
*DistributionSetTagsApi* | [**unassign_distribution_set**](docs/DistributionSetTagsApi.md#unassign_distribution_set) | **DELETE** /rest/v1/distributionsettags/{distributionsetTagId}/assigned/{distributionsetId} | Unassign one distribution set from the given tag id
*DistributionSetTagsApi* | [**update_distribution_set_tag**](docs/DistributionSetTagsApi.md#update_distribution_set_tag) | **PUT** /rest/v1/distributionsettags/{distributionsetTagId} | Update Distribution Set Tag
*DistributionSetTypesApi* | [**add_mandatory_module**](docs/DistributionSetTypesApi.md#add_mandatory_module) | **POST** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes | Add mandatory Software Module Type to a Distribution Set Type
*DistributionSetTypesApi* | [**add_optional_module**](docs/DistributionSetTypesApi.md#add_optional_module) | **POST** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes | Add optional Software Module Type to a Distribution Set Type
*DistributionSetTypesApi* | [**create_distribution_set_types**](docs/DistributionSetTypesApi.md#create_distribution_set_types) | **POST** /rest/v1/distributionsettypes | Create new distribution set types
*DistributionSetTypesApi* | [**delete_distribution_set_type**](docs/DistributionSetTypesApi.md#delete_distribution_set_type) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId} | Delete Distribution Set Type by Id
*DistributionSetTypesApi* | [**get_distribution_set_type**](docs/DistributionSetTypesApi.md#get_distribution_set_type) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId} | Return single Distribution Set Type
*DistributionSetTypesApi* | [**get_distribution_set_types**](docs/DistributionSetTypesApi.md#get_distribution_set_types) | **GET** /rest/v1/distributionsettypes | Return all Distribution Set Types
*DistributionSetTypesApi* | [**get_mandatory_module**](docs/DistributionSetTypesApi.md#get_mandatory_module) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes/{softwareModuleTypeId} | Return single mandatory Software Module Type in a Distribution Set Type
*DistributionSetTypesApi* | [**get_mandatory_modules**](docs/DistributionSetTypesApi.md#get_mandatory_modules) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes | Return mandatory Software Module Types in a Distribution Set Type
*DistributionSetTypesApi* | [**get_optional_module**](docs/DistributionSetTypesApi.md#get_optional_module) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes/{softwareModuleTypeId} | Return single optional Software Module Type in a Distribution Set Type
*DistributionSetTypesApi* | [**get_optional_modules**](docs/DistributionSetTypesApi.md#get_optional_modules) | **GET** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes | Return optional Software Module Types in a Distribution Set Type
*DistributionSetTypesApi* | [**remove_mandatory_module**](docs/DistributionSetTypesApi.md#remove_mandatory_module) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId}/mandatorymoduletypes/{softwareModuleTypeId} | Delete a mandatory module from a Distribution Set Type
*DistributionSetTypesApi* | [**remove_optional_module**](docs/DistributionSetTypesApi.md#remove_optional_module) | **DELETE** /rest/v1/distributionsettypes/{distributionSetTypeId}/optionalmoduletypes/{softwareModuleTypeId} | Delete an optional module from a Distribution Set Type
*DistributionSetTypesApi* | [**update_distribution_set_type**](docs/DistributionSetTypesApi.md#update_distribution_set_type) | **PUT** /rest/v1/distributionsettypes/{distributionSetTypeId} | Update Distribution Set Type
*DistributionSetsApi* | [**assign_software_modules**](docs/DistributionSetsApi.md#assign_software_modules) | **POST** /rest/v1/distributionsets/{distributionSetId}/assignedSM | Assign a list of software modules to a distribution set
*DistributionSetsApi* | [**create_assigned_target**](docs/DistributionSetsApi.md#create_assigned_target) | **POST** /rest/v1/distributionsets/{distributionSetId}/assignedTargets | Assigning multiple targets to a single distribution set
*DistributionSetsApi* | [**create_distribution_sets**](docs/DistributionSetsApi.md#create_distribution_sets) | **POST** /rest/v1/distributionsets | Creates new Distribution Sets
*DistributionSetsApi* | [**create_metadata2**](docs/DistributionSetsApi.md#create_metadata2) | **POST** /rest/v1/distributionsets/{distributionSetId}/metadata | Create a list of meta data for a specific distribution set
*DistributionSetsApi* | [**delete_assign_software_modules**](docs/DistributionSetsApi.md#delete_assign_software_modules) | **DELETE** /rest/v1/distributionsets/{distributionSetId}/assignedSM/{softwareModuleId} | Delete the assignment of the software module from the distribution set
*DistributionSetsApi* | [**delete_distribution_set**](docs/DistributionSetsApi.md#delete_distribution_set) | **DELETE** /rest/v1/distributionsets/{distributionSetId} | Delete Distribution Set by Id
*DistributionSetsApi* | [**delete_metadata2**](docs/DistributionSetsApi.md#delete_metadata2) | **DELETE** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Delete a single meta data entry from the distribution set
*DistributionSetsApi* | [**get_actions_count_by_status_for_distribution_set**](docs/DistributionSetsApi.md#get_actions_count_by_status_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/actions | Return Actions count by status for Distribution Set
*DistributionSetsApi* | [**get_assigned_software_modules**](docs/DistributionSetsApi.md#get_assigned_software_modules) | **GET** /rest/v1/distributionsets/{distributionSetId}/assignedSM | Return the assigned software modules of a specific distribution set
*DistributionSetsApi* | [**get_assigned_targets1**](docs/DistributionSetsApi.md#get_assigned_targets1) | **GET** /rest/v1/distributionsets/{distributionSetId}/assignedTargets | Return assigned targets to a specific distribution set
*DistributionSetsApi* | [**get_auto_assign_target_filter_queries**](docs/DistributionSetsApi.md#get_auto_assign_target_filter_queries) | **GET** /rest/v1/distributionsets/{distributionSetId}/autoAssignTargetFilters | Return target filter queries that have the given distribution set as auto assign DS
*DistributionSetsApi* | [**get_auto_assignments_count_for_distribution_set**](docs/DistributionSetsApi.md#get_auto_assignments_count_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/autoassignments | Return Auto Assignments count for Distribution Set
*DistributionSetsApi* | [**get_distribution_set**](docs/DistributionSetsApi.md#get_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId} | Return single Distribution Set
*DistributionSetsApi* | [**get_distribution_sets**](docs/DistributionSetsApi.md#get_distribution_sets) | **GET** /rest/v1/distributionsets | Return all Distribution Sets
*DistributionSetsApi* | [**get_installed_targets**](docs/DistributionSetsApi.md#get_installed_targets) | **GET** /rest/v1/distributionsets/{distributionSetId}/installedTargets | Return installed targets to a specific distribution set
*DistributionSetsApi* | [**get_metadata2**](docs/DistributionSetsApi.md#get_metadata2) | **GET** /rest/v1/distributionsets/{distributionSetId}/metadata | Return meta data for Distribution Set
*DistributionSetsApi* | [**get_metadata_value2**](docs/DistributionSetsApi.md#get_metadata_value2) | **GET** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Return single meta data value for a specific key of a Distribution Set
*DistributionSetsApi* | [**get_rollouts_count_by_status_for_distribution_set**](docs/DistributionSetsApi.md#get_rollouts_count_by_status_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics/rollouts | Return Rollouts count by status for Distribution Set
*DistributionSetsApi* | [**get_statistics_for_distribution_set**](docs/DistributionSetsApi.md#get_statistics_for_distribution_set) | **GET** /rest/v1/distributionsets/{distributionSetId}/statistics | Return Rollouts, Actions and Auto Assignments counts by Status for Distribution Set
*DistributionSetsApi* | [**invalidate_distribution_set**](docs/DistributionSetsApi.md#invalidate_distribution_set) | **POST** /rest/v1/distributionsets/{distributionSetId}/invalidate | Invalidate a distribution set
*DistributionSetsApi* | [**update_distribution_set**](docs/DistributionSetsApi.md#update_distribution_set) | **PUT** /rest/v1/distributionsets/{distributionSetId} | Update Distribution Set
*DistributionSetsApi* | [**update_metadata2**](docs/DistributionSetsApi.md#update_metadata2) | **PUT** /rest/v1/distributionsets/{distributionSetId}/metadata/{metadataKey} | Update single meta data value of a distribution set
*DownloadArtifactApi* | [**download_artifact1**](docs/DownloadArtifactApi.md#download_artifact1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId}/download | 
*RolloutsApi* | [**approve**](docs/RolloutsApi.md#approve) | **POST** /rest/v1/rollouts/{rolloutId}/approve | Approve a Rollout
*RolloutsApi* | [**create**](docs/RolloutsApi.md#create) | **POST** /rest/v1/rollouts | Create a new Rollout
*RolloutsApi* | [**delete**](docs/RolloutsApi.md#delete) | **DELETE** /rest/v1/rollouts/{rolloutId} | Delete a Rollout
*RolloutsApi* | [**deny**](docs/RolloutsApi.md#deny) | **POST** /rest/v1/rollouts/{rolloutId}/deny | Deny a Rollout
*RolloutsApi* | [**get_rollout**](docs/RolloutsApi.md#get_rollout) | **GET** /rest/v1/rollouts/{rolloutId} | Return single Rollout
*RolloutsApi* | [**get_rollout_group**](docs/RolloutsApi.md#get_rollout_group) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups/{groupId} | Return single rollout group
*RolloutsApi* | [**get_rollout_group_targets**](docs/RolloutsApi.md#get_rollout_group_targets) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups/{groupId}/targets | Return all targets related to a specific rollout group
*RolloutsApi* | [**get_rollout_groups**](docs/RolloutsApi.md#get_rollout_groups) | **GET** /rest/v1/rollouts/{rolloutId}/deploygroups | Return all rollout groups referred to a Rollout
*RolloutsApi* | [**get_rollouts**](docs/RolloutsApi.md#get_rollouts) | **GET** /rest/v1/rollouts | Return all Rollouts
*RolloutsApi* | [**pause**](docs/RolloutsApi.md#pause) | **POST** /rest/v1/rollouts/{rolloutId}/pause | Pause a Rollout
*RolloutsApi* | [**resume**](docs/RolloutsApi.md#resume) | **POST** /rest/v1/rollouts/{rolloutId}/resume | Resume a Rollout
*RolloutsApi* | [**retry_rollout**](docs/RolloutsApi.md#retry_rollout) | **POST** /rest/v1/rollouts/{rolloutId}/retry | Retry a rollout
*RolloutsApi* | [**start**](docs/RolloutsApi.md#start) | **POST** /rest/v1/rollouts/{rolloutId}/start | Start a Rollout
*RolloutsApi* | [**trigger_next_group**](docs/RolloutsApi.md#trigger_next_group) | **POST** /rest/v1/rollouts/{rolloutId}/triggerNextGroup | Force trigger processing next group of a Rollout
*RolloutsApi* | [**update**](docs/RolloutsApi.md#update) | **PUT** /rest/v1/rollouts/{rolloutId} | Update Rollout
*SoftwareModuleTypesApi* | [**create_software_module_types**](docs/SoftwareModuleTypesApi.md#create_software_module_types) | **POST** /rest/v1/softwaremoduletypes | Creates new Software Module Types
*SoftwareModuleTypesApi* | [**delete_software_module_type**](docs/SoftwareModuleTypesApi.md#delete_software_module_type) | **DELETE** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Delete Software Module Type by Id
*SoftwareModuleTypesApi* | [**get_software_module_type**](docs/SoftwareModuleTypesApi.md#get_software_module_type) | **GET** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Return single Software Module Type
*SoftwareModuleTypesApi* | [**get_types**](docs/SoftwareModuleTypesApi.md#get_types) | **GET** /rest/v1/softwaremoduletypes | Return all Software Module Types
*SoftwareModuleTypesApi* | [**update_software_module_type**](docs/SoftwareModuleTypesApi.md#update_software_module_type) | **PUT** /rest/v1/softwaremoduletypes/{softwareModuleTypeId} | Update Software Module Type
*SoftwareModulesApi* | [**create_metadata1**](docs/SoftwareModulesApi.md#create_metadata1) | **POST** /rest/v1/softwaremodules/{softwareModuleId}/metadata | Creates a list of meta data for a specific Software Module
*SoftwareModulesApi* | [**create_software_modules**](docs/SoftwareModulesApi.md#create_software_modules) | **POST** /rest/v1/softwaremodules | Create Software Module(s)
*SoftwareModulesApi* | [**delete_artifact**](docs/SoftwareModulesApi.md#delete_artifact) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId} | Delete artifact by Id
*SoftwareModulesApi* | [**delete_metadata1**](docs/SoftwareModulesApi.md#delete_metadata1) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Delete single meta data entry from the software module
*SoftwareModulesApi* | [**delete_software_module**](docs/SoftwareModulesApi.md#delete_software_module) | **DELETE** /rest/v1/softwaremodules/{softwareModuleId} | Delete Software Module by Id
*SoftwareModulesApi* | [**get_artifact**](docs/SoftwareModulesApi.md#get_artifact) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId} | Return single Artifact meta data
*SoftwareModulesApi* | [**get_artifacts**](docs/SoftwareModulesApi.md#get_artifacts) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts | Return all meta data of artifacts assigned to a software module
*SoftwareModulesApi* | [**get_metadata1**](docs/SoftwareModulesApi.md#get_metadata1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/metadata | Return meta data for a Software Module
*SoftwareModulesApi* | [**get_metadata_value1**](docs/SoftwareModulesApi.md#get_metadata_value1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Return single meta data value for a specific key of a Software Module
*SoftwareModulesApi* | [**get_software_module**](docs/SoftwareModulesApi.md#get_software_module) | **GET** /rest/v1/softwaremodules/{softwareModuleId} | Return Software Module by id
*SoftwareModulesApi* | [**get_software_modules**](docs/SoftwareModulesApi.md#get_software_modules) | **GET** /rest/v1/softwaremodules | Return all Software modules
*SoftwareModulesApi* | [**update_metadata1**](docs/SoftwareModulesApi.md#update_metadata1) | **PUT** /rest/v1/softwaremodules/{softwareModuleId}/metadata/{metadataKey} | Update a single meta data value of a Software Module
*SoftwareModulesApi* | [**update_software_module**](docs/SoftwareModulesApi.md#update_software_module) | **PUT** /rest/v1/softwaremodules/{softwareModuleId} | Update Software Module
*SoftwareModulesApi* | [**upload_artifact**](docs/SoftwareModulesApi.md#upload_artifact) | **POST** /rest/v1/softwaremodules/{softwareModuleId}/artifacts | Upload artifact
*SystemConfigurationApi* | [**delete_tenant_configuration_value**](docs/SystemConfigurationApi.md#delete_tenant_configuration_value) | **DELETE** /rest/v1/system/configs/{keyName} | Delete a tenant specific configuration value
*SystemConfigurationApi* | [**get_tenant_configuration**](docs/SystemConfigurationApi.md#get_tenant_configuration) | **GET** /rest/v1/system/configs | Return all tenant specific configuration values
*SystemConfigurationApi* | [**get_tenant_configuration_value**](docs/SystemConfigurationApi.md#get_tenant_configuration_value) | **GET** /rest/v1/system/configs/{keyName} | Return a tenant specific configuration value
*SystemConfigurationApi* | [**update_tenant_configuration**](docs/SystemConfigurationApi.md#update_tenant_configuration) | **PUT** /rest/v1/system/configs | Batch update of tenant configuration.
*SystemConfigurationApi* | [**update_tenant_configuration_value**](docs/SystemConfigurationApi.md#update_tenant_configuration_value) | **PUT** /rest/v1/system/configs/{keyName} | Update a tenant specific configuration value.
*TargetFilterQueriesApi* | [**create_filter**](docs/TargetFilterQueriesApi.md#create_filter) | **POST** /rest/v1/targetfilters | Create target filter
*TargetFilterQueriesApi* | [**delete_assigned_distribution_set**](docs/TargetFilterQueriesApi.md#delete_assigned_distribution_set) | **DELETE** /rest/v1/targetfilters/{filterId}/autoAssignDS | Remove Distribution Set for auto assignment of a target filter
*TargetFilterQueriesApi* | [**delete_filter**](docs/TargetFilterQueriesApi.md#delete_filter) | **DELETE** /rest/v1/targetfilters/{filterId} | Delete target filter by id
*TargetFilterQueriesApi* | [**get_assigned_distribution_set1**](docs/TargetFilterQueriesApi.md#get_assigned_distribution_set1) | **GET** /rest/v1/targetfilters/{filterId}/autoAssignDS | Return distribution set for auto assignment of a specific target filter
*TargetFilterQueriesApi* | [**get_filter**](docs/TargetFilterQueriesApi.md#get_filter) | **GET** /rest/v1/targetfilters/{filterId} | Return target filter query by id
*TargetFilterQueriesApi* | [**get_filters**](docs/TargetFilterQueriesApi.md#get_filters) | **GET** /rest/v1/targetfilters | Return all target filter queries
*TargetFilterQueriesApi* | [**post_assigned_distribution_set1**](docs/TargetFilterQueriesApi.md#post_assigned_distribution_set1) | **POST** /rest/v1/targetfilters/{filterId}/autoAssignDS | Set auto assignment of distribution set for a target filter query
*TargetFilterQueriesApi* | [**update_filter**](docs/TargetFilterQueriesApi.md#update_filter) | **PUT** /rest/v1/targetfilters/{filterId} | Updates target filter query by id
*TargetTagsApi* | [**assign_targets**](docs/TargetTagsApi.md#assign_targets) | **POST** /rest/v1/targettags/{targetTagId}/assigned | Assign target(s) to given tagId and return targets
*TargetTagsApi* | [**assign_targets_by_controller_ids**](docs/TargetTagsApi.md#assign_targets_by_controller_ids) | **PUT** /rest/v1/targettags/{targetTagId}/assigned | Assign target(s) to given tagId
*TargetTagsApi* | [**create_target_tags**](docs/TargetTagsApi.md#create_target_tags) | **POST** /rest/v1/targettags | Create target tag(s)
*TargetTagsApi* | [**delete_target_tag**](docs/TargetTagsApi.md#delete_target_tag) | **DELETE** /rest/v1/targettags/{targetTagId} | Delete target tag by id
*TargetTagsApi* | [**get_assigned_targets**](docs/TargetTagsApi.md#get_assigned_targets) | **GET** /rest/v1/targettags/{targetTagId}/assigned | Return assigned targets for tag
*TargetTagsApi* | [**get_target_tag**](docs/TargetTagsApi.md#get_target_tag) | **GET** /rest/v1/targettags/{targetTagId} | Return target tag by id
*TargetTagsApi* | [**get_target_tags**](docs/TargetTagsApi.md#get_target_tags) | **GET** /rest/v1/targettags | Return all target tags
*TargetTagsApi* | [**toggle_tag_assignment**](docs/TargetTagsApi.md#toggle_tag_assignment) | **POST** /rest/v1/targettags/{targetTagId}/assigned/toggleTagAssignment | Toggles target tag assignment
*TargetTagsApi* | [**unassign_target**](docs/TargetTagsApi.md#unassign_target) | **DELETE** /rest/v1/targettags/{targetTagId}/assigned/{controllerId} | Unassign target from a given tagId
*TargetTagsApi* | [**update_target_tag**](docs/TargetTagsApi.md#update_target_tag) | **PUT** /rest/v1/targettags/{targetTagId} | Update target tag by id
*TargetTypesApi* | [**add_compatible_distribution_sets**](docs/TargetTypesApi.md#add_compatible_distribution_sets) | **POST** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes | Adding compatibility of a distribution set type to a target type
*TargetTypesApi* | [**create_target_types**](docs/TargetTypesApi.md#create_target_types) | **POST** /rest/v1/targettypes | Create target types
*TargetTypesApi* | [**delete_target_type**](docs/TargetTypesApi.md#delete_target_type) | **DELETE** /rest/v1/targettypes/{targetTypeId} | Delete target type by id
*TargetTypesApi* | [**get_compatible_distribution_sets**](docs/TargetTypesApi.md#get_compatible_distribution_sets) | **GET** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes | Return list of compatible distribution set types
*TargetTypesApi* | [**get_target_type**](docs/TargetTypesApi.md#get_target_type) | **GET** /rest/v1/targettypes/{targetTypeId} | Return target type by id
*TargetTypesApi* | [**get_target_types**](docs/TargetTypesApi.md#get_target_types) | **GET** /rest/v1/targettypes | Return all target types
*TargetTypesApi* | [**remove_compatible_distribution_set**](docs/TargetTypesApi.md#remove_compatible_distribution_set) | **DELETE** /rest/v1/targettypes/{targetTypeId}/compatibledistributionsettypes/{distributionSetTypeId} | Remove compatibility of distribution set type from the target type
*TargetTypesApi* | [**update_target_type**](docs/TargetTypesApi.md#update_target_type) | **PUT** /rest/v1/targettypes/{targetTypeId} | Update target type by id
*TargetsApi* | [**activate_auto_confirm**](docs/TargetsApi.md#activate_auto_confirm) | **POST** /rest/v1/targets/{targetId}/autoConfirm/activate | Activate auto-confirm on a specific target
*TargetsApi* | [**assign_target_type**](docs/TargetsApi.md#assign_target_type) | **POST** /rest/v1/targets/{targetId}/targettype | Assign target type to a target
*TargetsApi* | [**cancel_action**](docs/TargetsApi.md#cancel_action) | **DELETE** /rest/v1/targets/{targetId}/actions/{actionId} | Cancel action for a specific target
*TargetsApi* | [**create_metadata**](docs/TargetsApi.md#create_metadata) | **POST** /rest/v1/targets/{targetId}/metadata | Create a list of meta data for a specific target
*TargetsApi* | [**create_targets**](docs/TargetsApi.md#create_targets) | **POST** /rest/v1/targets | Create target(s)
*TargetsApi* | [**deactivate_auto_confirm**](docs/TargetsApi.md#deactivate_auto_confirm) | **POST** /rest/v1/targets/{targetId}/autoConfirm/deactivate | Deactivate auto-confirm on a specific target
*TargetsApi* | [**delete_metadata**](docs/TargetsApi.md#delete_metadata) | **DELETE** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Deletes a single meta data entry from a target
*TargetsApi* | [**delete_target**](docs/TargetsApi.md#delete_target) | **DELETE** /rest/v1/targets/{targetId} | Delete target by id
*TargetsApi* | [**get_action**](docs/TargetsApi.md#get_action) | **GET** /rest/v1/targets/{targetId}/actions/{actionId} | Return action by id of a specific target
*TargetsApi* | [**get_action_history**](docs/TargetsApi.md#get_action_history) | **GET** /rest/v1/targets/{targetId}/actions | Return actions for a specific target
*TargetsApi* | [**get_action_status_list**](docs/TargetsApi.md#get_action_status_list) | **GET** /rest/v1/targets/{targetId}/actions/{actionId}/status | Return status of a specific action on a specific target
*TargetsApi* | [**get_assigned_distribution_set**](docs/TargetsApi.md#get_assigned_distribution_set) | **GET** /rest/v1/targets/{targetId}/assignedDS | Return the assigned distribution set of a specific target
*TargetsApi* | [**get_attributes**](docs/TargetsApi.md#get_attributes) | **GET** /rest/v1/targets/{targetId}/attributes | Return attributes of a specific target
*TargetsApi* | [**get_auto_confirm_status**](docs/TargetsApi.md#get_auto_confirm_status) | **GET** /rest/v1/targets/{targetId}/autoConfirm | Return the current auto-confitm state for a specific target
*TargetsApi* | [**get_installed_distribution_set**](docs/TargetsApi.md#get_installed_distribution_set) | **GET** /rest/v1/targets/{targetId}/installedDS | Return installed distribution set of a specific target
*TargetsApi* | [**get_metadata**](docs/TargetsApi.md#get_metadata) | **GET** /rest/v1/targets/{targetId}/metadata | Return metadata for specific target
*TargetsApi* | [**get_metadata_value**](docs/TargetsApi.md#get_metadata_value) | **GET** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Return single metadata value for a specific key of a target
*TargetsApi* | [**get_tags**](docs/TargetsApi.md#get_tags) | **GET** /rest/v1/targets/{targetId}/tags | Return tags for specific target
*TargetsApi* | [**get_target**](docs/TargetsApi.md#get_target) | **GET** /rest/v1/targets/{targetId} | Return target by id
*TargetsApi* | [**get_targets**](docs/TargetsApi.md#get_targets) | **GET** /rest/v1/targets | Return all targets
*TargetsApi* | [**post_assigned_distribution_set**](docs/TargetsApi.md#post_assigned_distribution_set) | **POST** /rest/v1/targets/{targetId}/assignedDS | Assigns a distribution set to a specific target
*TargetsApi* | [**unassign_target_type**](docs/TargetsApi.md#unassign_target_type) | **DELETE** /rest/v1/targets/{targetId}/targettype | Unassign target type from target.
*TargetsApi* | [**update_action**](docs/TargetsApi.md#update_action) | **PUT** /rest/v1/targets/{targetId}/actions/{actionId} | Switch an action from soft to forced
*TargetsApi* | [**update_metadata**](docs/TargetsApi.md#update_metadata) | **PUT** /rest/v1/targets/{targetId}/metadata/{metadataKey} | Updates a single meta data value of a target
*TargetsApi* | [**update_target**](docs/TargetsApi.md#update_target) | **PUT** /rest/v1/targets/{targetId} | Update target by id

## Documentation For Models

 - [ExceptionInfo](docs/ExceptionInfo.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [MgmtAction](docs/MgmtAction.md)
 - [MgmtActionId](docs/MgmtActionId.md)
 - [MgmtActionRequestBodyPut](docs/MgmtActionRequestBodyPut.md)
 - [MgmtActionStatus](docs/MgmtActionStatus.md)
 - [MgmtArtifact](docs/MgmtArtifact.md)
 - [MgmtArtifactHash](docs/MgmtArtifactHash.md)
 - [MgmtAssignedDistributionSetRequestBody](docs/MgmtAssignedDistributionSetRequestBody.md)
 - [MgmtAssignedTargetRequestBody](docs/MgmtAssignedTargetRequestBody.md)
 - [MgmtDistributionSet](docs/MgmtDistributionSet.md)
 - [MgmtDistributionSetAssignment](docs/MgmtDistributionSetAssignment.md)
 - [MgmtDistributionSetAssignments](docs/MgmtDistributionSetAssignments.md)
 - [MgmtDistributionSetAutoAssignment](docs/MgmtDistributionSetAutoAssignment.md)
 - [MgmtDistributionSetRequestBodyPost](docs/MgmtDistributionSetRequestBodyPost.md)
 - [MgmtDistributionSetRequestBodyPut](docs/MgmtDistributionSetRequestBodyPut.md)
 - [MgmtDistributionSetStatistics](docs/MgmtDistributionSetStatistics.md)
 - [MgmtDistributionSetTagAssigmentResult](docs/MgmtDistributionSetTagAssigmentResult.md)
 - [MgmtDistributionSetType](docs/MgmtDistributionSetType.md)
 - [MgmtDistributionSetTypeAssignment](docs/MgmtDistributionSetTypeAssignment.md)
 - [MgmtDistributionSetTypeRequestBodyPost](docs/MgmtDistributionSetTypeRequestBodyPost.md)
 - [MgmtDistributionSetTypeRequestBodyPut](docs/MgmtDistributionSetTypeRequestBodyPut.md)
 - [MgmtDynamicRolloutGroupTemplate](docs/MgmtDynamicRolloutGroupTemplate.md)
 - [MgmtId](docs/MgmtId.md)
 - [MgmtInvalidateDistributionSetRequestBody](docs/MgmtInvalidateDistributionSetRequestBody.md)
 - [MgmtMaintenanceWindowRequestBody](docs/MgmtMaintenanceWindowRequestBody.md)
 - [MgmtMetadata](docs/MgmtMetadata.md)
 - [MgmtMetadataBodyPut](docs/MgmtMetadataBodyPut.md)
 - [MgmtPollStatus](docs/MgmtPollStatus.md)
 - [MgmtRolloutCondition](docs/MgmtRolloutCondition.md)
 - [MgmtRolloutErrorAction](docs/MgmtRolloutErrorAction.md)
 - [MgmtRolloutGroup](docs/MgmtRolloutGroup.md)
 - [MgmtRolloutGroupResponseBody](docs/MgmtRolloutGroupResponseBody.md)
 - [MgmtRolloutResponseBody](docs/MgmtRolloutResponseBody.md)
 - [MgmtRolloutRestRequestBodyPost](docs/MgmtRolloutRestRequestBodyPost.md)
 - [MgmtRolloutRestRequestBodyPut](docs/MgmtRolloutRestRequestBodyPut.md)
 - [MgmtRolloutSuccessAction](docs/MgmtRolloutSuccessAction.md)
 - [MgmtSoftwareModule](docs/MgmtSoftwareModule.md)
 - [MgmtSoftwareModuleAssigment](docs/MgmtSoftwareModuleAssigment.md)
 - [MgmtSoftwareModuleMetadata](docs/MgmtSoftwareModuleMetadata.md)
 - [MgmtSoftwareModuleMetadataBodyPut](docs/MgmtSoftwareModuleMetadataBodyPut.md)
 - [MgmtSoftwareModuleRequestBodyPost](docs/MgmtSoftwareModuleRequestBodyPost.md)
 - [MgmtSoftwareModuleRequestBodyPut](docs/MgmtSoftwareModuleRequestBodyPut.md)
 - [MgmtSoftwareModuleType](docs/MgmtSoftwareModuleType.md)
 - [MgmtSoftwareModuleTypeAssigment](docs/MgmtSoftwareModuleTypeAssigment.md)
 - [MgmtSoftwareModuleTypeRequestBodyPost](docs/MgmtSoftwareModuleTypeRequestBodyPost.md)
 - [MgmtSoftwareModuleTypeRequestBodyPut](docs/MgmtSoftwareModuleTypeRequestBodyPut.md)
 - [MgmtSystemTenantConfigurationValue](docs/MgmtSystemTenantConfigurationValue.md)
 - [MgmtSystemTenantConfigurationValueRequest](docs/MgmtSystemTenantConfigurationValueRequest.md)
 - [MgmtTag](docs/MgmtTag.md)
 - [MgmtTagRequestBodyPut](docs/MgmtTagRequestBodyPut.md)
 - [MgmtTarget](docs/MgmtTarget.md)
 - [MgmtTargetAssignmentRequestBody](docs/MgmtTargetAssignmentRequestBody.md)
 - [MgmtTargetAssignmentResponseBody](docs/MgmtTargetAssignmentResponseBody.md)
 - [MgmtTargetAttributes](docs/MgmtTargetAttributes.md)
 - [MgmtTargetAutoConfirm](docs/MgmtTargetAutoConfirm.md)
 - [MgmtTargetAutoConfirmUpdate](docs/MgmtTargetAutoConfirmUpdate.md)
 - [MgmtTargetFilterQuery](docs/MgmtTargetFilterQuery.md)
 - [MgmtTargetFilterQueryRequestBody](docs/MgmtTargetFilterQueryRequestBody.md)
 - [MgmtTargetRequestBody](docs/MgmtTargetRequestBody.md)
 - [MgmtTargetTagAssigmentResult](docs/MgmtTargetTagAssigmentResult.md)
 - [MgmtTargetType](docs/MgmtTargetType.md)
 - [MgmtTargetTypeRequestBodyPost](docs/MgmtTargetTypeRequestBodyPost.md)
 - [MgmtTargetTypeRequestBodyPut](docs/MgmtTargetTypeRequestBodyPut.md)
 - [MgmtUserInfo](docs/MgmtUserInfo.md)
 - [PagedListMgmtAction](docs/PagedListMgmtAction.md)
 - [PagedListMgmtActionStatus](docs/PagedListMgmtActionStatus.md)
 - [PagedListMgmtDistributionSet](docs/PagedListMgmtDistributionSet.md)
 - [PagedListMgmtDistributionSetType](docs/PagedListMgmtDistributionSetType.md)
 - [PagedListMgmtMetadata](docs/PagedListMgmtMetadata.md)
 - [PagedListMgmtRolloutGroupResponseBody](docs/PagedListMgmtRolloutGroupResponseBody.md)
 - [PagedListMgmtRolloutResponseBody](docs/PagedListMgmtRolloutResponseBody.md)
 - [PagedListMgmtSoftwareModule](docs/PagedListMgmtSoftwareModule.md)
 - [PagedListMgmtSoftwareModuleMetadata](docs/PagedListMgmtSoftwareModuleMetadata.md)
 - [PagedListMgmtSoftwareModuleType](docs/PagedListMgmtSoftwareModuleType.md)
 - [PagedListMgmtTag](docs/PagedListMgmtTag.md)
 - [PagedListMgmtTarget](docs/PagedListMgmtTarget.md)
 - [PagedListMgmtTargetFilterQuery](docs/PagedListMgmtTargetFilterQuery.md)
 - [PagedListMgmtTargetType](docs/PagedListMgmtTargetType.md)
 - [SoftwareModuleIdArtifactsBody](docs/SoftwareModuleIdArtifactsBody.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

