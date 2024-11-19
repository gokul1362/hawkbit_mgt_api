# MgmtTargetAssignmentRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The technical identifier of the entity | 
**forcetime** | **int** | Forcetime in milliseconds | [optional] 
**type** | **str** | The type of the assignment | [optional] 
**maintenance_window** | [**MgmtMaintenanceWindowRequestBody**](MgmtMaintenanceWindowRequestBody.md) |  | [optional] 
**weight** | **int** | Importance of the assignment | [optional] 
**confirmation_required** | **bool** | (Available with user consent flow active) Defines, if the confirmation is required for an action. Confirmation is required per default | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

