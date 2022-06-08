# insights_plotrisk.EntityAuditCollectionControllerApi

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post2**](EntityAuditCollectionControllerApi.md#create_using_post2) | **POST** /api/v1/audits | create
[**list_all_using_get2**](EntityAuditCollectionControllerApi.md#list_all_using_get2) | **GET** /api/v1/audits | listAll


# **create_using_post2**
> EntityAuditCollectionResponse create_using_post2(json, org_id=org_id, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.EntityAuditCollectionControllerApi(insights_plotrisk.ApiClient(configuration))
json = insights_plotrisk.EntityAuditCollectionRequest() # EntityAuditCollectionRequest | json
org_id = 'org_id_example' # str | orgId (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # create
    api_response = api_instance.create_using_post2(json, org_id=org_id, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityAuditCollectionControllerApi->create_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json** | [**EntityAuditCollectionRequest**](EntityAuditCollectionRequest.md)| json | 
 **org_id** | **str**| orgId | [optional] 
 **tenant_type** | **str**| TenantType | [optional] 

### Return type

[**EntityAuditCollectionResponse**](EntityAuditCollectionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_using_get2**
> dict(str, object) list_all_using_get2(action_type=action_type, direction=direction, entity_id=entity_id, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, status=status, statuses=statuses, tenant_type=tenant_type)

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
api_instance = insights_plotrisk.EntityAuditCollectionControllerApi(insights_plotrisk.ApiClient(configuration))
action_type = 'action_type_example' # str |  (optional)
direction = 'direction_example' # str |  (optional)
entity_id = 'entity_id_example' # str |  (optional)
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
status = 'status_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
tenant_type = 'tenant_type_example' # str | TenantType (optional)

try:
    # listAll
    api_response = api_instance.list_all_using_get2(action_type=action_type, direction=direction, entity_id=entity_id, external_id=external_id, ids=ids, max_created_date_time=max_created_date_time, max_modified_date_time=max_modified_date_time, min_created_date_time=min_created_date_time, min_modified_date_time=min_modified_date_time, org_id=org_id, page=page, select=select, size=size, sort_by=sort_by, status=status, statuses=statuses, tenant_type=tenant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntityAuditCollectionControllerApi->list_all_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **entity_id** | **str**|  | [optional] 
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
 **status** | **str**|  | [optional] 
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

