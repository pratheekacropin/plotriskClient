# insights_plotrisk.CropsControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post**](CropsControllerApi.md#create_using_post) | **POST** /api/v1/crops | create
[**list_all_using_get**](CropsControllerApi.md#list_all_using_get) | **GET** /api/v1/crops | listAll


# **create_using_post**
> CropResponse create_using_post(json, org_id=org_id, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.CropsControllerApi(insights_plotrisk.ApiClient(configuration))
json = insights_plotrisk.CropRequest() # CropRequest | json
org_id = 'org_id_example' # str | orgId (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # create
    api_response = api_instance.create_using_post(json, org_id=org_id, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CropsControllerApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**CropRequest**](CropRequest.md)| json | 
 **org_id** | **str**| orgId | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 

### Return type

[**CropResponse**](CropResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_using_get**
> dict(str, object) list_all_using_get(common_names=common_names, direction=direction, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, names=names, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type, varieties=varieties)

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
api_instance = insights_plotrisk.CropsControllerApi(insights_plotrisk.ApiClient(configuration))
common_names = ['common_names_example'] # list[str] |  (optional)
direction = 'direction_example' # str |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
max_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
names = ['names_example'] # list[str] |  (optional)
org_id = 'org_id_example' # str | orgId (optional)
page = 56 # int |  (optional)
select = ['select_example'] # list[str] |  (optional)
size = 56 # int |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)
varieties = ['varieties_example'] # list[str] |  (optional)

try:
    # listAll
    api_response = api_instance.list_all_using_get(common_names=common_names, direction=direction, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, names=names, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type, varieties=varieties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CropsControllerApi->list_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_names** | [**list[str]**](str.md)|  | [optional] 
 **direction** | **str**|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **max_created_date_time** | **datetime**|  | [optional] 
 **max_modified_date_time** | **datetime**|  | [optional] 
 **min_created_date_time** | **datetime**|  | [optional] 
 **min_modified_date_time** | **datetime**|  | [optional] 
 **names** | [**list[str]**](str.md)|  | [optional] 
 **org_id** | **str**| orgId | [optional] 
 **page** | **int**|  | [optional] 
 **select** | [**list[str]**](str.md)|  | [optional] 
 **size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **statuses** | [**list[str]**](str.md)|  | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 
 **varieties** | [**list[str]**](str.md)|  | [optional] 

### Return type

**dict(str, object)**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

