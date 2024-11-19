# MgmtAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**type** | **str** | Type of action | [optional] 
**status** | **str** | Status of action | [optional] 
**detail_status** | **str** | Detailed status of action | [optional] 
**force_time** | **int** |  | [optional] 
**weight** | **int** | Weight of the action showing the importance of the update | [optional] 
**rollout** | **int** | The ID of the rollout this action was created for | [optional] 
**rollout_name** | **str** | The name of the rollout this action was created for | [optional] 
**last_status_code** | **int** | (Optional) Code provided as part of the last status update that was sent by the device. | [optional] 
**external_ref** | **str** | If created by external system this field contains the external reference for the action | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**id** | **int** | ID of the action | [optional] 
**force_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

