# swagger_client.BasicAuthenticationApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_basic_auth**](BasicAuthenticationApi.md#validate_basic_auth) | **GET** /rest/v1/userinfo | 

# **validate_basic_auth**
> MgmtUserInfo validate_basic_auth()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BasicAuthenticationApi()

try:
    api_response = api_instance.validate_basic_auth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicAuthenticationApi->validate_basic_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MgmtUserInfo**](MgmtUserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

