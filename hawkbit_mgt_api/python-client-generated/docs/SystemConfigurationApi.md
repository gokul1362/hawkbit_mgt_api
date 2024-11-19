# swagger_client.SystemConfigurationApi

All URIs are relative to *http://localhost:59874*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tenant_configuration_value**](SystemConfigurationApi.md#delete_tenant_configuration_value) | **DELETE** /rest/v1/system/configs/{keyName} | Delete a tenant specific configuration value
[**get_tenant_configuration**](SystemConfigurationApi.md#get_tenant_configuration) | **GET** /rest/v1/system/configs | Return all tenant specific configuration values
[**get_tenant_configuration_value**](SystemConfigurationApi.md#get_tenant_configuration_value) | **GET** /rest/v1/system/configs/{keyName} | Return a tenant specific configuration value
[**update_tenant_configuration**](SystemConfigurationApi.md#update_tenant_configuration) | **PUT** /rest/v1/system/configs | Batch update of tenant configuration.
[**update_tenant_configuration_value**](SystemConfigurationApi.md#update_tenant_configuration_value) | **PUT** /rest/v1/system/configs/{keyName} | Update a tenant specific configuration value.

# **delete_tenant_configuration_value**
> delete_tenant_configuration_value(key_name)

Delete a tenant specific configuration value

The DELETE request removes a tenant specific configuration value for the tenant. Afterwards the global default value is used. Required Permission: TENANT_CONFIGURATION

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemConfigurationApi()
key_name = 'key_name_example' # str | 

try:
    # Delete a tenant specific configuration value
    api_instance.delete_tenant_configuration_value(key_name)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->delete_tenant_configuration_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_configuration**
> dict(str, MgmtSystemTenantConfigurationValue) get_tenant_configuration()

Return all tenant specific configuration values

The GET request returns a list of all possible configuration keys for the tenant. Required Permission: READ_TENANT_CONFIGURATION

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemConfigurationApi()

try:
    # Return all tenant specific configuration values
    api_response = api_instance.get_tenant_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->get_tenant_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, MgmtSystemTenantConfigurationValue)**](MgmtSystemTenantConfigurationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_configuration_value**
> MgmtSystemTenantConfigurationValue get_tenant_configuration_value(key_name)

Return a tenant specific configuration value

The GET request returns the configuration value of a specific configuration key for the tenant. Required Permission: READ_TENANT_CONFIGURATION

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemConfigurationApi()
key_name = 'key_name_example' # str | 

try:
    # Return a tenant specific configuration value
    api_response = api_instance.get_tenant_configuration_value(key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->get_tenant_configuration_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_name** | **str**|  | 

### Return type

[**MgmtSystemTenantConfigurationValue**](MgmtSystemTenantConfigurationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_configuration**
> list[MgmtSystemTenantConfigurationValue] update_tenant_configuration(body)

Batch update of tenant configuration.

The PUT request updates the whole configuration for the tenant. Required Permission: TENANT_CONFIGURATION

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemConfigurationApi()
body = NULL # dict(str, object) | 

try:
    # Batch update of tenant configuration.
    api_response = api_instance.update_tenant_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->update_tenant_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 

### Return type

[**list[MgmtSystemTenantConfigurationValue]**](MgmtSystemTenantConfigurationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_configuration_value**
> MgmtSystemTenantConfigurationValue update_tenant_configuration_value(body, key_name)

Update a tenant specific configuration value.

The PUT request changes a configuration value of a specific configuration key for the tenant. Required Permission: TENANT_CONFIGURATION

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemConfigurationApi()
body = swagger_client.MgmtSystemTenantConfigurationValueRequest() # MgmtSystemTenantConfigurationValueRequest | 
key_name = 'key_name_example' # str | 

try:
    # Update a tenant specific configuration value.
    api_response = api_instance.update_tenant_configuration_value(body, key_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->update_tenant_configuration_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MgmtSystemTenantConfigurationValueRequest**](MgmtSystemTenantConfigurationValueRequest.md)|  | 
 **key_name** | **str**|  | 

### Return type

[**MgmtSystemTenantConfigurationValue**](MgmtSystemTenantConfigurationValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/hal+json
 - **Accept**: application/json, application/hal+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

