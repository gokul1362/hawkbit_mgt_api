# MgmtRolloutResponseBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**target_filter_query** | **str** | Target filter query language expression | [optional] 
**distribution_set_id** | **int** | The ID of distribution set of this rollout | [optional] 
**status** | **str** | The status of this rollout | 
**total_targets** | **int** | The total targets of a rollout | 
**total_targets_per_status** | **dict(str, int)** | The total targets per status | [optional] 
**total_groups** | **int** | The total number of groups created by this rollout | [optional] 
**start_at** | **int** | Start at timestamp of Rollout | [optional] 
**forcetime** | **int** | Forcetime in milliseconds | [optional] 
**deleted** | **bool** | Deleted flag, used for soft deleted entities | [optional] 
**type** | **str** | The type of this rollout | [optional] 
**weight** | **int** | Weight of the resulting Actions | [optional] 
**dynamic** | **bool** | If this rollout is dynamic or static | [optional] 
**approval_remark** | **str** |  | [optional] 
**approve_decided_by** | **str** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**id** | **int** | Rollout id | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

