# insights_plotrisk
SR Insight Service API Documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import insights_plotrisk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import insights_plotrisk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://https://rn0t0s00e2.execute-api.ap-southeast-1.amazonaws.com/dev*

| Class                                | Method                                                                                     | HTTP request                           | Description |
|--------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------|-------------|
| *CropsControllerApi*                 | [**create_using_post**](docs/CropsControllerApi.md#create_using_post)                      | **POST** /api/v1/crops                 | create      |
| *CropsControllerApi*                 | [**list_all_using_get**](docs/CropsControllerApi.md#list_all_using_get)                    | **GET** /api/v1/crops                  | listAll     |
| *CustomBoundaryControllerApi*        | [**create_batch_using_post**](docs/CustomBoundaryControllerApi.md#create_batch_using_post) | **POST** /api/v1/plotboundary/batch    | createBatch |
| *CustomBoundaryControllerApi*        | [**create_using_post1**](docs/CustomBoundaryControllerApi.md#create_using_post1)           | **POST** /api/v1/plotboundary          | create      |
| *CustomBoundaryControllerApi*        | [**list_all_using_get1**](docs/CustomBoundaryControllerApi.md#list_all_using_get1)         | **GET** /api/v1/plotboundary           | listAll     |
| *EntityAuditCollectionControllerApi* | [**create_using_post2**](docs/EntityAuditCollectionControllerApi.md#create_using_post2)    | **POST** /api/v1/audits                | create      |
| *EntityAuditCollectionControllerApi* | [**list_all_using_get2**](docs/EntityAuditCollectionControllerApi.md#list_all_using_get2)  | **GET** /api/v1/audits                 | listAll     |
| *GenericODataControllerApi*          | [**process_using_get**](docs/GenericODataControllerApi.md#process_using_get)               | **GET** /api/v1/odata/satellitemetrics | process     |
| *WeatherDataControllerApi*           | [**create_using_post3**](docs/WeatherDataControllerApi.md#create_using_post3)              | **POST** /api/v1/weatherdata           | create      |
| *WeatherDataControllerApi*           | [**list_all_using_get3**](docs/WeatherDataControllerApi.md#list_all_using_get3)            | **GET** /api/v1/weatherdata            | listAll     |
| *YieldDataControllerApi*             | [**create_using_post4**](docs/YieldDataControllerApi.md#create_using_post4)                | **POST** /api/v1/yielddata             | create      |
| *YieldDataControllerApi*             | [**list_all_using_get4**](docs/YieldDataControllerApi.md#list_all_using_get4)              | **GET** /api/v1/yielddata              | listAll     |

## Documentation For Models

 - [BoundaryRequest](docs/BoundaryRequest.md)
 - [BoundaryResponse](docs/BoundaryResponse.md)
 - [CropDetail](docs/CropDetail.md)
 - [CropRequest](docs/CropRequest.md)
 - [CropResponse](docs/CropResponse.md)
 - [EntityAuditCollectionRequest](docs/EntityAuditCollectionRequest.md)
 - [EntityAuditCollectionResponse](docs/EntityAuditCollectionResponse.md)
 - [FeatureCollectionReq](docs/FeatureCollectionReq.md)
 - [FeatureCollectionRes](docs/FeatureCollectionRes.md)
 - [FeatureReq](docs/FeatureReq.md)
 - [FeatureRes](docs/FeatureRes.md)
 - [Gdd](docs/Gdd.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryCollection](docs/GeometryCollection.md)
 - [LineString](docs/LineString.md)
 - [MultiLineString](docs/MultiLineString.md)
 - [MultiPoint](docs/MultiPoint.md)
 - [MultiPolygon](docs/MultiPolygon.md)
 - [Point](docs/Point.md)
 - [Polygon](docs/Polygon.md)
 - [Weather](docs/Weather.md)
 - [WeatherDataRequest](docs/WeatherDataRequest.md)
 - [WeatherDataResponse](docs/WeatherDataResponse.md)
 - [YieldRequest](docs/YieldRequest.md)
 - [YieldResponse](docs/YieldResponse.md)
 - [YieldsData](docs/YieldsData.md)


## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



