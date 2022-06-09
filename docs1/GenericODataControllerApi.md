# insights_plotrisk.GenericODataControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_using_get**](GenericODataControllerApi.md#process_using_get) | **GET** /api/v1/odata/satellitemetrics | process


# **process_using_get**
> process_using_get()

process

### Example
```python
from __future__ import print_function
import time
import insights_plotrisk
from insights_plotrisk.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT
configuration = insights_plotrisk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = insights_plotrisk.GenericODataControllerApi(insights_plotrisk.ApiClient(configuration))

try:
    # process
    api_instance.process_using_get()
except ApiException as e:
    print("Exception when calling GenericODataControllerApi->process_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

