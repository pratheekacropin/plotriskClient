# insights_plotrisk.CustomBoundaryControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_using_post**](CustomBoundaryControllerApi.md#create_batch_using_post) | **POST** /api/v1/plotboundary/batch | createBatch
[**create_using_post1**](CustomBoundaryControllerApi.md#create_using_post1) | **POST** /api/v1/plotboundary | create
[**list_all_using_get1**](CustomBoundaryControllerApi.md#list_all_using_get1) | **GET** /api/v1/plotboundary | listAll


# **create_batch_using_post**
> list[BoundaryResponse] create_batch_using_post(boundary_request_list, tenant_type, org_id=org_id)

createBatch

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
api_instance = insights_plotrisk.CustomBoundaryControllerApi(insights_plotrisk.ApiClient(configuration))
boundary_request_list = [insights_plotrisk.BoundaryRequest()] # list[BoundaryRequest] | boundaryRequestList
tenant_type = 'tenant_type_example' # str | TenantType
org_id = 'org_id_example' # str | orgId (optional)

try:
    # createBatch
    api_response = api_instance.create_batch_using_post(boundary_request_list, tenant_type, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomBoundaryControllerApi->create_batch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_request_list** | [**list[BoundaryRequest]**](BoundaryRequest.md)| boundaryRequestList | 
 **tenant_type** | **str**| TenantType | 
 **org_id** | **str**| orgId | [optional] 

### Return type

[**list[BoundaryResponse]**](BoundaryResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post1**
> BoundaryResponse create_using_post1(json, tenant_type, org_id=org_id)

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
api_instance = insights_plotrisk.CustomBoundaryControllerApi(insights_plotrisk.ApiClient(configuration))
json = insights_plotrisk.BoundaryRequest() # BoundaryRequest | json
tenant_type = 'tenant_type_example' # str | TenantType
org_id = 'org_id_example' # str | orgId (optional)

try:
    # create
    api_response = api_instance.create_using_post1(json, tenant_type, org_id=org_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomBoundaryControllerApi->create_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**BoundaryRequest**](BoundaryRequest.md)| json | 
 **tenant_type** | **str**| TenantType | 
 **org_id** | **str**| orgId | [optional] 

### Return type

[**BoundaryResponse**](BoundaryResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_using_get1**
> dict(str, object) list_all_using_get1(direction=direction, external_ids=external_ids, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, parent_ids=parent_ids, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.CustomBoundaryControllerApi(insights_plotrisk.ApiClient(configuration))
direction = 'direction_example' # str |  (optional)
external_ids = ['external_ids_example'] # list[str] |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
max_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
org_id = 'org_id_example' # str | orgId (optional)
page = 56 # int |  (optional)
parent_ids = ['parent_ids_example'] # list[str] |  (optional)
select = ['select_example'] # list[str] |  (optional)
size = 56 # int |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
tenant_type = 'tenant_type_example' # str |  (optional)

try:
    # listAll
    api_response = api_instance.list_all_using_get1(direction=direction, external_ids=external_ids, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, parent_ids=parent_ids, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomBoundaryControllerApi->list_all_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direction** | **str**|  | [optional] 
 **external_ids** | [**list[str]**](str.md)|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **max_created_date_time** | **datetime**|  | [optional] 
 **max_modified_date_time** | **datetime**|  | [optional] 
 **min_created_date_time** | **datetime**|  | [optional] 
 **min_modified_date_time** | **datetime**|  | [optional] 
 **org_id** | **str**| orgId | [optional] 
 **page** | **int**|  | [optional] 
 **parent_ids** | [**list[str]**](str.md)|  | [optional] 
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

