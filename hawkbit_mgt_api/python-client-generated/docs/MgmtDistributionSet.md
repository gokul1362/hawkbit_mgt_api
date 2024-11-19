# MgmtDistributionSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Entity was originally created by (User, AMQP-Controller, anonymous etc.) | [optional] 
**created_at** | **int** | Entity was originally created at (timestamp UTC in milliseconds) | [optional] 
**last_modified_by** | **str** | Entity was last modified by (User, AMQP-Controller, anonymous etc.) | [optional] 
**last_modified_at** | **int** | Entity was last modified at (timestamp UTC in milliseconds) | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**version** | **str** | Package version | [optional] 
**type** | **str** | The type of the distribution set | [optional] 
**type_name** | **str** | The type name of the distribution set | [optional] 
**complete** | **bool** | True of the distribution set software module setup is complete as defined by the distribution set type | [optional] 
**locked** | **bool** | If the distribution set is locked | [optional] 
**deleted** | **bool** | Deleted flag, used for soft deleted entities | [optional] 
**valid** | **bool** | True by default and false after the distribution set is invalidated by the user | [optional] 
**required_migration_step** | **bool** | True if DS is a required migration step for another DS. As a result the DS’s assignment will not be cancelled when another DS is assigned (note: updatable only if DS is not yet assigned to a target) | [optional] 
**modules** | [**list[MgmtSoftwareModule]**](MgmtSoftwareModule.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**id** | **int** | The technical identifier of the entity | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

