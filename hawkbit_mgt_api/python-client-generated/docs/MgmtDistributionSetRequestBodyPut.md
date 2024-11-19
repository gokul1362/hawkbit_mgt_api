# MgmtDistributionSetRequestBodyPut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the entity | [optional] 
**description** | **str** | The description of the entity | [optional] 
**version** | **str** | Package version | [optional] 
**locked** | **bool** | Should be set only if change of locked state is requested. If put, the distribution set locked flag will be set to the requested. Note: unlock (i.e. set this property to false) with extreme care! In general once distribution set is locked it shall not be unlocked. Note that it could have been assigned / deployed to targets. | [optional] 
**required_migration_step** | **bool** | True if DS is a required migration step for another DS. As a result the DS’s assignment will not be cancelled when another DS is assigned (note: updatable only if DS is not yet assigned to a target) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

