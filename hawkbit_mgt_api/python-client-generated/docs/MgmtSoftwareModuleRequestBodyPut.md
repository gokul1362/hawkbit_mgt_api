# MgmtSoftwareModuleRequestBodyPut

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**locked** | **bool** | Should be set only if change of locked state is requested. If put, the software module locked flag will be set to the requested. Note: unlock (i.e. set this property to false) with extreme care! In general once software module is locked it shall not be unlocked. Note that it could have been assigned / deployed to targets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

