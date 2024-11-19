# MgmtTargetRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity | 
**description** | **str** | The description of the entity | [optional] 
**controller_id** | **str** | Controller ID | 
**address** | **str** | The last known address URI of the target. Includes information of the target is connected either directly (DDI) through HTTP or indirectly (DMF) through amqp | [optional] 
**security_token** | **str** | Pre-Shared key that allows targets to authenticate at Direct Device Integration API if enabled in the tenant settings | [optional] 
**request_attributes** | **bool** | Request re-transmission of target attributes | [optional] 
**target_type** | **int** | ID of the target type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

