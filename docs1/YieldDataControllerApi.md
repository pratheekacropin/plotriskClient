# insights_plotrisk.YieldDataControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post4**](YieldDataControllerApi.md#create_using_post4) | **POST** /api/v1/yielddata | create
[**list_all_using_get4**](YieldDataControllerApi.md#list_all_using_get4) | **GET** /api/v1/yielddata | listAll


# **create_using_post4**
> YieldResponse create_using_post4(json, org_id=org_id, tenant_type=tenant_type)

create

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
api_instance = insights_plotrisk.YieldDataControllerApi(insights_plotrisk.ApiClient(configuration))
json = insights_plotrisk.YieldRequest() # YieldRequest | json
org_id = 'org_id_example' # str | orgId (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # create
    api_response = api_instance.create_using_post4(json, org_id=org_id, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YieldDataControllerApi->create_using_post4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**YieldRequest**](YieldRequest.md)| json | 
 **org_id** | **str**| orgId | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 

### Return type

[**YieldResponse**](YieldResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_using_get4**
> dict(str, object) list_all_using_get4(boundary_id=boundary_id, direction=direction, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)

listAll

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
api_instance = insights_plotrisk.YieldDataControllerApi(insights_plotrisk.ApiClient(configuration))
boundary_id = 'boundary_id_example' # str |  (optional)
direction = 'direction_example' # str |  (optional)
external_id = 'external_id_example' # str |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
max_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
org_id = 'org_id_example' # str | orgId (optional)
page = 56 # int |  (optional)
select = ['select_example'] # list[str] |  (optional)
size = 56 # int |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
tenant_type = 'tenant_type_example' # str |  (optional)

try:
    # listAll
    api_response = api_instance.list_all_using_get4(boundary_id=boundary_id, direction=direction, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YieldDataControllerApi->list_all_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_id** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **max_created_date_time** | **datetime**|  | [optional] 
 **max_modified_date_time** | **datetime**|  | [optional] 
 **min_created_date_time** | **datetime**|  | [optional] 
 **min_modified_date_time** | **datetime**|  | [optional] 
 **org_id** | **str**| orgId | [optional] 
 **page** | **int**|  | [optional] 
 **select** | [**list[str]**](str.md)|  | [optional] 
 **size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **statuses** | [**list[str]**](str.md)|  | [optional] 
 **tenant_type** | **str**|  | [optional] 

### Return type

**dict(str, object)**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

