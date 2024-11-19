# MgmtTarget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**controller_id** | **str** | Controller ID | 
**update_status** | **str** | If the target is in sync | [optional] 
**last_controller_request_at** | **int** | Timestamp of the last controller request | [optional] 
**installed_at** | **int** | Install timestamp | [optional] 
**ip_address** | **str** | Last known IP address of the target. Only presented if IP address of the target itself is known (connected directly through DDI API) | [optional] 
**address** | **str** | The last known address URI of the target. Includes information of the target is connected either directly (DDI) through HTTP or indirectly (DMF) through amqp. | [optional] 
**poll_status** | [**MgmtPollStatus**](MgmtPollStatus.md) |  | [optional] 
**security_token** | **str** | Pre-Shared key that allows targets to authenticate at Direct Device Integration API if enabled in the tenant settings | [optional] 
**request_attributes** | **bool** | Request re-transmission of target attributes | [optional] 
**target_type** | **int** | ID of the target type | [optional] 
**target_type_name** | **str** | Name of the target type | [optional] 
**auto_confirm_active** | **bool** | Present if user consent flow active. Indicates if auto-confirm is active | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

