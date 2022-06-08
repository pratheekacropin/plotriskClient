# insights_plotrisk.WeatherDataControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post3**](WeatherDataControllerApi.md#create_using_post3) | **POST** /api/v1/weatherdata | create
[**list_all_using_get3**](WeatherDataControllerApi.md#list_all_using_get3) | **GET** /api/v1/weatherdata | listAll


# **create_using_post3**
> WeatherDataResponse create_using_post3(json, org_id=org_id, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.WeatherDataControllerApi(insights_plotrisk.ApiClient(configuration))
json = insights_plotrisk.WeatherDataRequest() # WeatherDataRequest | json
org_id = 'org_id_example' # str | orgId (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # create
    api_response = api_instance.create_using_post3(json, org_id=org_id, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherDataControllerApi->create_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**WeatherDataRequest**](WeatherDataRequest.md)| json | 
 **org_id** | **str**| orgId | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 

### Return type

[**WeatherDataResponse**](WeatherDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_using_get3**
> dict(str, object) list_all_using_get3(_date=_date, date_from=date_from, date_to=date_to, direction=direction, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, plot_id=plot_id, plot_name=plot_name, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.WeatherDataControllerApi(insights_plotrisk.ApiClient(configuration))
_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
direction = 'direction_example' # str |  (optional)
external_id = 'external_id_example' # str |  (optional)
ids = ['ids_example'] # list[str] |  (optional)
max_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_created_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_modified_date_time = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
org_id = 'org_id_example' # str | orgId (optional)
page = 56 # int |  (optional)
plot_id = 'plot_id_example' # str |  (optional)
plot_name = 'plot_name_example' # str |  (optional)
select = ['select_example'] # list[str] |  (optional)
size = 56 # int |  (optional)
sort_by = 'sort_by_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # listAll
    api_response = api_instance.list_all_using_get3(_date=_date, date_from=date_from, date_to=date_to, direction=direction, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, plot_id=plot_id, plot_name=plot_name, select=select, size=size, sort_by=sort_by, statuses=statuses, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherDataControllerApi->list_all_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **datetime**|  | [optional] 
 **date_from** | **datetime**|  | [optional] 
 **date_to** | **datetime**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **max_created_date_time** | **datetime**|  | [optional] 
 **max_modified_date_time** | **datetime**|  | [optional] 
 **min_created_date_time** | **datetime**|  | [optional] 
 **min_modified_date_time** | **datetime**|  | [optional] 
 **org_id** | **str**| orgId | [optional] 
 **page** | **int**|  | [optional] 
 **plot_id** | **str**|  | [optional] 
 **plot_name** | **str**|  | [optional] 
 **select** | [**list[str]**](str.md)|  | [optional] 
 **size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **statuses** | [**list[str]**](str.md)|  | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 

### Return type

**dict(str, object)**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

