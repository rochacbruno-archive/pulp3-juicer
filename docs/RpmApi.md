# juicer.RpmApi

All URIs are relative to *http://192.168.122.18*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpm_upload_create**](RpmApi.md#rpm_upload_create) | **POST** /rpm/upload/ | 


# **rpm_upload_create**
> rpm_upload_create()



Upload an RPM package.

### Example
```python
from __future__ import print_function
import time
import juicer
from juicer.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = juicer.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = juicer.RpmApi(juicer.ApiClient(configuration))

try:
    api_instance.rpm_upload_create()
except ApiException as e:
    print("Exception when calling RpmApi->rpm_upload_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

