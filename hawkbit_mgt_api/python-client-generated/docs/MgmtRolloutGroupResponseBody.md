# MgmtRolloutGroupResponseBody

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
**target_filter_query** | **str** | The name of the entity | [optional] 
**target_percentage** | **float** | Percentage of remaining and matching targets that should be added to this group | [optional] 
**confirmation_required** | **bool** | (Available with user consent flow active) If the confirmation is required for this rollout group. Confirmation is required per default | [optional] 
**dynamic** | **bool** | If the rollout group is dynamic | [optional] 
**status** | **str** | The status of this rollout | 
**total_targets** | **int** | The total targets of a rollout | [optional] 
**total_targets_per_status** | **dict(str, int)** | The total targets per status | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**id** | **int** | Rollouts id | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

