# MgmtRolloutRestRequestBodyPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**success_condition** | [**MgmtRolloutCondition**](MgmtRolloutCondition.md) |  | [optional] 
**success_action** | [**MgmtRolloutSuccessAction**](MgmtRolloutSuccessAction.md) |  | [optional] 
**error_condition** | [**MgmtRolloutCondition**](MgmtRolloutCondition.md) |  | [optional] 
**error_action** | [**MgmtRolloutErrorAction**](MgmtRolloutErrorAction.md) |  | [optional] 
**target_filter_query** | **str** | Target filter query language expression | [optional] 
**distribution_set_id** | **int** | The ID of distribution set of this rollout | [optional] 
**amount_groups** | **int** | The amount of groups the rollout should split targets into | [optional] 
**forcetime** | **int** | Force time in milliseconds | [optional] 
**start_at** | **int** | Start at timestamp of Rollout | [optional] 
**weight** | **int** | Weight of the resulting Actions | [optional] 
**dynamic** | **bool** |  | [optional] 
**dynamic_group_template** | [**MgmtDynamicRolloutGroupTemplate**](MgmtDynamicRolloutGroupTemplate.md) |  | [optional] 
**confirmation_required** | **bool** | (Available with user consent flow active) If the confirmation is required for this rollout. Value will be used if confirmation options are missing in the rollout group definitions. Confirmation is required per default | [optional] 
**type** | **str** | The type of this rollout | [optional] 
**groups** | [**list[MgmtRolloutGroup]**](MgmtRolloutGroup.md) | The list of group definitions | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

