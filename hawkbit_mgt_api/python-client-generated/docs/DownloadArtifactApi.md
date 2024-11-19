# swagger_client.DownloadArtifactApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_artifact1**](DownloadArtifactApi.md#download_artifact1) | **GET** /rest/v1/softwaremodules/{softwareModuleId}/artifacts/{artifactId}/download | 

# **download_artifact1**
> object download_artifact1(software_module_id, artifact_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadArtifactApi()
software_module_id = 789 # int | 
artifact_id = 789 # int | 

try:
    api_response = api_instance.download_artifact1(software_module_id, artifact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadArtifactApi->download_artifact1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_module_id** | **int**|  | 
 **artifact_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

