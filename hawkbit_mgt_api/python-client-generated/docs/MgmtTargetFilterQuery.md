# MgmtTargetFilterQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**name** | **str** | The name of the entity | [optional] 
**query** | **str** | Target filter query expression | [optional] 
**auto_assign_distribution_set** | **int** |  | [optional] 
**auto_assign_action_type** | **str** | Auto assign distribution set id | [optional] 
**auto_assign_weight** | **int** | Weight of the resulting Actions | [optional] 
**confirmation_required** | **bool** | (Available with user consent flow active) Defines, if the confirmation is required for an action. Confirmation is required per default. | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**id** | **int** | The technical identifier of the entity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

