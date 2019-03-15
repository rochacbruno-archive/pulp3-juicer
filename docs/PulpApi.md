# juicer.PulpApi

All URIs are relative to *http://192.168.122.18*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifacts_create**](PulpApi.md#artifacts_create) | **POST** /pulp/api/v3/artifacts/ | 
[**artifacts_delete**](PulpApi.md#artifacts_delete) | **DELETE** {artifact_href} | 
[**artifacts_list**](PulpApi.md#artifacts_list) | **GET** /pulp/api/v3/artifacts/ | 
[**artifacts_read**](PulpApi.md#artifacts_read) | **GET** {artifact_href} | 
[**content_docker_blobs_create**](PulpApi.md#content_docker_blobs_create) | **POST** /pulp/api/v3/content/docker/blobs/ | 
[**content_docker_blobs_list**](PulpApi.md#content_docker_blobs_list) | **GET** /pulp/api/v3/content/docker/blobs/ | 
[**content_docker_blobs_read**](PulpApi.md#content_docker_blobs_read) | **GET** {manifest_blob_href} | 
[**content_docker_manifest_list_tags_create**](PulpApi.md#content_docker_manifest_list_tags_create) | **POST** /pulp/api/v3/content/docker/manifest-list-tags/ | 
[**content_docker_manifest_list_tags_list**](PulpApi.md#content_docker_manifest_list_tags_list) | **GET** /pulp/api/v3/content/docker/manifest-list-tags/ | 
[**content_docker_manifest_list_tags_read**](PulpApi.md#content_docker_manifest_list_tags_read) | **GET** {manifest_list_tag_href} | 
[**content_docker_manifest_lists_create**](PulpApi.md#content_docker_manifest_lists_create) | **POST** /pulp/api/v3/content/docker/manifest-lists/ | 
[**content_docker_manifest_lists_list**](PulpApi.md#content_docker_manifest_lists_list) | **GET** /pulp/api/v3/content/docker/manifest-lists/ | 
[**content_docker_manifest_lists_read**](PulpApi.md#content_docker_manifest_lists_read) | **GET** {manifest_list_href} | 
[**content_docker_manifest_tags_create**](PulpApi.md#content_docker_manifest_tags_create) | **POST** /pulp/api/v3/content/docker/manifest-tags/ | 
[**content_docker_manifest_tags_list**](PulpApi.md#content_docker_manifest_tags_list) | **GET** /pulp/api/v3/content/docker/manifest-tags/ | 
[**content_docker_manifest_tags_read**](PulpApi.md#content_docker_manifest_tags_read) | **GET** {manifest_tag_href} | 
[**content_docker_manifests_create**](PulpApi.md#content_docker_manifests_create) | **POST** /pulp/api/v3/content/docker/manifests/ | 
[**content_docker_manifests_list**](PulpApi.md#content_docker_manifests_list) | **GET** /pulp/api/v3/content/docker/manifests/ | 
[**content_docker_manifests_read**](PulpApi.md#content_docker_manifests_read) | **GET** {image_manifest_href} | 
[**content_file_files_create**](PulpApi.md#content_file_files_create) | **POST** /pulp/api/v3/content/file/files/ | 
[**content_file_files_list**](PulpApi.md#content_file_files_list) | **GET** /pulp/api/v3/content/file/files/ | 
[**content_file_files_read**](PulpApi.md#content_file_files_read) | **GET** {file_content_href} | 
[**content_rpm_errata_create**](PulpApi.md#content_rpm_errata_create) | **POST** /pulp/api/v3/content/rpm/errata/ | A ViewSet for UpdateRecord.
[**content_rpm_errata_list**](PulpApi.md#content_rpm_errata_list) | **GET** /pulp/api/v3/content/rpm/errata/ | A ViewSet for UpdateRecord.
[**content_rpm_errata_read**](PulpApi.md#content_rpm_errata_read) | **GET** {update_record_href} | A ViewSet for UpdateRecord.
[**content_rpm_packages_create**](PulpApi.md#content_rpm_packages_create) | **POST** /pulp/api/v3/content/rpm/packages/ | 
[**content_rpm_packages_list**](PulpApi.md#content_rpm_packages_list) | **GET** /pulp/api/v3/content/rpm/packages/ | A ViewSet for Package.
[**content_rpm_packages_read**](PulpApi.md#content_rpm_packages_read) | **GET** {package_href} | A ViewSet for Package.
[**contentguards_certguard_certguard_create**](PulpApi.md#contentguards_certguard_certguard_create) | **POST** /pulp/api/v3/contentguards/certguard/certguard/ | 
[**contentguards_certguard_certguard_delete**](PulpApi.md#contentguards_certguard_certguard_delete) | **DELETE** {cert_guard_href} | 
[**contentguards_certguard_certguard_list**](PulpApi.md#contentguards_certguard_certguard_list) | **GET** /pulp/api/v3/contentguards/certguard/certguard/ | 
[**contentguards_certguard_certguard_partial_update**](PulpApi.md#contentguards_certguard_certguard_partial_update) | **PATCH** {cert_guard_href} | 
[**contentguards_certguard_certguard_read**](PulpApi.md#contentguards_certguard_certguard_read) | **GET** {cert_guard_href} | 
[**contentguards_certguard_certguard_update**](PulpApi.md#contentguards_certguard_certguard_update) | **PUT** {cert_guard_href} | 
[**distributions_create**](PulpApi.md#distributions_create) | **POST** /pulp/api/v3/distributions/ | 
[**distributions_delete**](PulpApi.md#distributions_delete) | **DELETE** {distribution_href} | 
[**distributions_list**](PulpApi.md#distributions_list) | **GET** /pulp/api/v3/distributions/ | 
[**distributions_partial_update**](PulpApi.md#distributions_partial_update) | **PATCH** {distribution_href} | 
[**distributions_read**](PulpApi.md#distributions_read) | **GET** {distribution_href} | 
[**distributions_update**](PulpApi.md#distributions_update) | **PUT** {distribution_href} | 
[**docker_distributions_create**](PulpApi.md#docker_distributions_create) | **POST** /pulp/api/v3/docker-distributions/ | 
[**docker_distributions_delete**](PulpApi.md#docker_distributions_delete) | **DELETE** {docker_distribution_href} | 
[**docker_distributions_list**](PulpApi.md#docker_distributions_list) | **GET** /pulp/api/v3/docker-distributions/ | 
[**docker_distributions_partial_update**](PulpApi.md#docker_distributions_partial_update) | **PATCH** {docker_distribution_href} | 
[**docker_distributions_read**](PulpApi.md#docker_distributions_read) | **GET** {docker_distribution_href} | 
[**docker_distributions_update**](PulpApi.md#docker_distributions_update) | **PUT** {docker_distribution_href} | 
[**orphans_delete**](PulpApi.md#orphans_delete) | **DELETE** /pulp/api/v3/orphans/ | 
[**publications_delete**](PulpApi.md#publications_delete) | **DELETE** {publication_href} | 
[**publications_list**](PulpApi.md#publications_list) | **GET** /pulp/api/v3/publications/ | 
[**publications_read**](PulpApi.md#publications_read) | **GET** {publication_href} | 
[**publishers_docker_docker_create**](PulpApi.md#publishers_docker_docker_create) | **POST** /pulp/api/v3/publishers/docker/docker/ | 
[**publishers_docker_docker_delete**](PulpApi.md#publishers_docker_docker_delete) | **DELETE** {docker_publisher_href} | 
[**publishers_docker_docker_list**](PulpApi.md#publishers_docker_docker_list) | **GET** /pulp/api/v3/publishers/docker/docker/ | 
[**publishers_docker_docker_partial_update**](PulpApi.md#publishers_docker_docker_partial_update) | **PATCH** {docker_publisher_href} | 
[**publishers_docker_docker_publish**](PulpApi.md#publishers_docker_docker_publish) | **POST** {docker_publisher_href}publish/ | 
[**publishers_docker_docker_read**](PulpApi.md#publishers_docker_docker_read) | **GET** {docker_publisher_href} | 
[**publishers_docker_docker_update**](PulpApi.md#publishers_docker_docker_update) | **PUT** {docker_publisher_href} | 
[**publishers_file_file_create**](PulpApi.md#publishers_file_file_create) | **POST** /pulp/api/v3/publishers/file/file/ | 
[**publishers_file_file_delete**](PulpApi.md#publishers_file_file_delete) | **DELETE** {file_publisher_href} | 
[**publishers_file_file_list**](PulpApi.md#publishers_file_file_list) | **GET** /pulp/api/v3/publishers/file/file/ | 
[**publishers_file_file_partial_update**](PulpApi.md#publishers_file_file_partial_update) | **PATCH** {file_publisher_href} | 
[**publishers_file_file_publish**](PulpApi.md#publishers_file_file_publish) | **POST** {file_publisher_href}publish/ | 
[**publishers_file_file_read**](PulpApi.md#publishers_file_file_read) | **GET** {file_publisher_href} | 
[**publishers_file_file_update**](PulpApi.md#publishers_file_file_update) | **PUT** {file_publisher_href} | 
[**publishers_rpm_rpm_create**](PulpApi.md#publishers_rpm_rpm_create) | **POST** /pulp/api/v3/publishers/rpm/rpm/ | 
[**publishers_rpm_rpm_delete**](PulpApi.md#publishers_rpm_rpm_delete) | **DELETE** {rpm_publisher_href} | 
[**publishers_rpm_rpm_list**](PulpApi.md#publishers_rpm_rpm_list) | **GET** /pulp/api/v3/publishers/rpm/rpm/ | 
[**publishers_rpm_rpm_partial_update**](PulpApi.md#publishers_rpm_rpm_partial_update) | **PATCH** {rpm_publisher_href} | 
[**publishers_rpm_rpm_publish**](PulpApi.md#publishers_rpm_rpm_publish) | **POST** {rpm_publisher_href}publish/ | 
[**publishers_rpm_rpm_read**](PulpApi.md#publishers_rpm_rpm_read) | **GET** {rpm_publisher_href} | 
[**publishers_rpm_rpm_update**](PulpApi.md#publishers_rpm_rpm_update) | **PUT** {rpm_publisher_href} | 
[**remotes_docker_docker_create**](PulpApi.md#remotes_docker_docker_create) | **POST** /pulp/api/v3/remotes/docker/docker/ | 
[**remotes_docker_docker_delete**](PulpApi.md#remotes_docker_docker_delete) | **DELETE** {docker_remote_href} | 
[**remotes_docker_docker_list**](PulpApi.md#remotes_docker_docker_list) | **GET** /pulp/api/v3/remotes/docker/docker/ | 
[**remotes_docker_docker_partial_update**](PulpApi.md#remotes_docker_docker_partial_update) | **PATCH** {docker_remote_href} | 
[**remotes_docker_docker_read**](PulpApi.md#remotes_docker_docker_read) | **GET** {docker_remote_href} | 
[**remotes_docker_docker_sync**](PulpApi.md#remotes_docker_docker_sync) | **POST** {docker_remote_href}sync/ | 
[**remotes_docker_docker_update**](PulpApi.md#remotes_docker_docker_update) | **PUT** {docker_remote_href} | 
[**remotes_file_file_create**](PulpApi.md#remotes_file_file_create) | **POST** /pulp/api/v3/remotes/file/file/ | 
[**remotes_file_file_delete**](PulpApi.md#remotes_file_file_delete) | **DELETE** {file_remote_href} | 
[**remotes_file_file_list**](PulpApi.md#remotes_file_file_list) | **GET** /pulp/api/v3/remotes/file/file/ | 
[**remotes_file_file_partial_update**](PulpApi.md#remotes_file_file_partial_update) | **PATCH** {file_remote_href} | 
[**remotes_file_file_read**](PulpApi.md#remotes_file_file_read) | **GET** {file_remote_href} | 
[**remotes_file_file_sync**](PulpApi.md#remotes_file_file_sync) | **POST** {file_remote_href}sync/ | 
[**remotes_file_file_update**](PulpApi.md#remotes_file_file_update) | **PUT** {file_remote_href} | 
[**remotes_rpm_rpm_create**](PulpApi.md#remotes_rpm_rpm_create) | **POST** /pulp/api/v3/remotes/rpm/rpm/ | 
[**remotes_rpm_rpm_delete**](PulpApi.md#remotes_rpm_rpm_delete) | **DELETE** {rpm_remote_href} | 
[**remotes_rpm_rpm_list**](PulpApi.md#remotes_rpm_rpm_list) | **GET** /pulp/api/v3/remotes/rpm/rpm/ | 
[**remotes_rpm_rpm_partial_update**](PulpApi.md#remotes_rpm_rpm_partial_update) | **PATCH** {rpm_remote_href} | 
[**remotes_rpm_rpm_read**](PulpApi.md#remotes_rpm_rpm_read) | **GET** {rpm_remote_href} | 
[**remotes_rpm_rpm_sync**](PulpApi.md#remotes_rpm_rpm_sync) | **POST** {rpm_remote_href}sync/ | 
[**remotes_rpm_rpm_update**](PulpApi.md#remotes_rpm_rpm_update) | **PUT** {rpm_remote_href} | 
[**repositories_create**](PulpApi.md#repositories_create) | **POST** /pulp/api/v3/repositories/ | 
[**repositories_delete**](PulpApi.md#repositories_delete) | **DELETE** {repository_href} | 
[**repositories_list**](PulpApi.md#repositories_list) | **GET** /pulp/api/v3/repositories/ | 
[**repositories_partial_update**](PulpApi.md#repositories_partial_update) | **PATCH** {repository_href} | 
[**repositories_read**](PulpApi.md#repositories_read) | **GET** {repository_href} | 
[**repositories_update**](PulpApi.md#repositories_update) | **PUT** {repository_href} | 
[**repositories_versions_create**](PulpApi.md#repositories_versions_create) | **POST** {repository_href}versions/ | 
[**repositories_versions_delete**](PulpApi.md#repositories_versions_delete) | **DELETE** {repository_version_href} | 
[**repositories_versions_list**](PulpApi.md#repositories_versions_list) | **GET** {repository_href}versions/ | 
[**repositories_versions_partial_update**](PulpApi.md#repositories_versions_partial_update) | **PATCH** {repository_version_href} | 
[**repositories_versions_read**](PulpApi.md#repositories_versions_read) | **GET** {repository_version_href} | 
[**repositories_versions_update**](PulpApi.md#repositories_versions_update) | **PUT** {repository_version_href} | 
[**status_list**](PulpApi.md#status_list) | **GET** /pulp/api/v3/status/ | 
[**tasks_cancel**](PulpApi.md#tasks_cancel) | **POST** {task_href}cancel/ | 
[**tasks_delete**](PulpApi.md#tasks_delete) | **DELETE** {task_href} | 
[**tasks_list**](PulpApi.md#tasks_list) | **GET** /pulp/api/v3/tasks/ | 
[**tasks_read**](PulpApi.md#tasks_read) | **GET** {task_href} | 
[**uploads_create**](PulpApi.md#uploads_create) | **POST** /pulp/api/v3/uploads/ | 
[**uploads_create_0**](PulpApi.md#uploads_create_0) | **POST** {upload_href} | 
[**uploads_read**](PulpApi.md#uploads_read) | **GET** /pulp/api/v3/uploads/ | 
[**uploads_read_0**](PulpApi.md#uploads_read_0) | **GET** {upload_href} | 
[**uploads_update**](PulpApi.md#uploads_update) | **PUT** /pulp/api/v3/uploads/ | 
[**uploads_update_0**](PulpApi.md#uploads_update_0) | **PUT** {upload_href} | 
[**workers_list**](PulpApi.md#workers_list) | **GET** /pulp/api/v3/workers/ | 
[**workers_read**](PulpApi.md#workers_read) | **GET** {worker_href} | 


# **artifacts_create**
> Artifact artifacts_create(data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Artifact() # Artifact | 

try:
    api_response = api_instance.artifacts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->artifacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Artifact**](Artifact.md)|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_delete**
> artifacts_delete(artifact_href)



Remove Artifact only if it is not associated with any Content.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
artifact_href = 'artifact_href_example' # str | URI of Artifact. e.g.: /pulp/api/v3/artifacts/1/

try:
    api_instance.artifacts_delete(artifact_href)
except ApiException as e:
    print("Exception when calling PulpApi->artifacts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**| URI of Artifact. e.g.: /pulp/api/v3/artifacts/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_list**
> InlineResponse200 artifacts_list(md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
md5 = 'md5_example' # str | Filter results where md5 matches value (optional)
sha1 = 'sha1_example' # str | Filter results where sha1 matches value (optional)
sha224 = 'sha224_example' # str | Filter results where sha224 matches value (optional)
sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
sha384 = 'sha384_example' # str | Filter results where sha384 matches value (optional)
sha512 = 'sha512_example' # str | Filter results where sha512 matches value (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.artifacts_list(md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->artifacts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **md5** | **str**| Filter results where md5 matches value | [optional] 
 **sha1** | **str**| Filter results where sha1 matches value | [optional] 
 **sha224** | **str**| Filter results where sha224 matches value | [optional] 
 **sha256** | **str**| Filter results where sha256 matches value | [optional] 
 **sha384** | **str**| Filter results where sha384 matches value | [optional] 
 **sha512** | **str**| Filter results where sha512 matches value | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artifacts_read**
> Artifact artifacts_read(artifact_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
artifact_href = 'artifact_href_example' # str | URI of Artifact. e.g.: /pulp/api/v3/artifacts/1/

try:
    api_response = api_instance.artifacts_read(artifact_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->artifacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**| URI of Artifact. e.g.: /pulp/api/v3/artifacts/1/ | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_blobs_create**
> Blob content_docker_blobs_create(data)



Create a new ManifestBlob from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Blob() # Blob | 

try:
    api_response = api_instance.content_docker_blobs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_blobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Blob**](Blob.md)|  | 

### Return type

[**Blob**](Blob.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_blobs_list**
> InlineResponse2001 content_docker_blobs_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for ManifestBlobs.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_docker_blobs_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_blobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_blobs_read**
> Blob content_docker_blobs_read(manifest_blob_href)



ViewSet for ManifestBlobs.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
manifest_blob_href = 'manifest_blob_href_example' # str | URI of Manifest Blob. e.g.: /pulp/api/v3/content/docker/blobs/1/

try:
    api_response = api_instance.content_docker_blobs_read(manifest_blob_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_blobs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_blob_href** | **str**| URI of Manifest Blob. e.g.: /pulp/api/v3/content/docker/blobs/1/ | 

### Return type

[**Blob**](Blob.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_list_tags_create**
> ManifestListTag content_docker_manifest_list_tags_create(data)



Create a new ManifestListTag from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.ManifestListTag() # ManifestListTag | 

try:
    api_response = api_instance.content_docker_manifest_list_tags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_list_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ManifestListTag**](ManifestListTag.md)|  | 

### Return type

[**ManifestListTag**](ManifestListTag.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_list_tags_list**
> InlineResponse2002 content_docker_manifest_list_tags_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for ManifestListTag.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_docker_manifest_list_tags_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_list_tags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_list_tags_read**
> ManifestListTag content_docker_manifest_list_tags_read(manifest_list_tag_href)



ViewSet for ManifestListTag.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
manifest_list_tag_href = 'manifest_list_tag_href_example' # str | URI of Manifest List Tag. e.g.: /pulp/api/v3/content/docker/manifest-list-tags/1/

try:
    api_response = api_instance.content_docker_manifest_list_tags_read(manifest_list_tag_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_list_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_list_tag_href** | **str**| URI of Manifest List Tag. e.g.: /pulp/api/v3/content/docker/manifest-list-tags/1/ | 

### Return type

[**ManifestListTag**](ManifestListTag.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_lists_create**
> ManifestList content_docker_manifest_lists_create(data)



Create a new ManifestList from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.ManifestList() # ManifestList | 

try:
    api_response = api_instance.content_docker_manifest_lists_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_lists_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ManifestList**](ManifestList.md)|  | 

### Return type

[**ManifestList**](ManifestList.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_lists_list**
> InlineResponse2003 content_docker_manifest_lists_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for ManifestList.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_docker_manifest_lists_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_lists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_lists_read**
> ManifestList content_docker_manifest_lists_read(manifest_list_href)



ViewSet for ManifestList.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
manifest_list_href = 'manifest_list_href_example' # str | URI of Manifest List. e.g.: /pulp/api/v3/content/docker/manifest-lists/1/

try:
    api_response = api_instance.content_docker_manifest_lists_read(manifest_list_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_lists_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_list_href** | **str**| URI of Manifest List. e.g.: /pulp/api/v3/content/docker/manifest-lists/1/ | 

### Return type

[**ManifestList**](ManifestList.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_tags_create**
> ManifestTag content_docker_manifest_tags_create(data)



Create a new ManifestTag from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.ManifestTag() # ManifestTag | 

try:
    api_response = api_instance.content_docker_manifest_tags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ManifestTag**](ManifestTag.md)|  | 

### Return type

[**ManifestTag**](ManifestTag.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_tags_list**
> InlineResponse2004 content_docker_manifest_tags_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for ManifestTag.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_docker_manifest_tags_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_tags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifest_tags_read**
> ManifestTag content_docker_manifest_tags_read(manifest_tag_href)



ViewSet for ManifestTag.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
manifest_tag_href = 'manifest_tag_href_example' # str | URI of Manifest Tag. e.g.: /pulp/api/v3/content/docker/manifest-tags/1/

try:
    api_response = api_instance.content_docker_manifest_tags_read(manifest_tag_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifest_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_tag_href** | **str**| URI of Manifest Tag. e.g.: /pulp/api/v3/content/docker/manifest-tags/1/ | 

### Return type

[**ManifestTag**](ManifestTag.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifests_create**
> Manifest content_docker_manifests_create(data)



Create a new Manifest from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Manifest() # Manifest | 

try:
    api_response = api_instance.content_docker_manifests_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Manifest**](Manifest.md)|  | 

### Return type

[**Manifest**](Manifest.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifests_list**
> InlineResponse2005 content_docker_manifests_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for Manifest.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_docker_manifests_list(repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_docker_manifests_read**
> Manifest content_docker_manifests_read(image_manifest_href)



ViewSet for Manifest.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
image_manifest_href = 'image_manifest_href_example' # str | URI of Image Manifest. e.g.: /pulp/api/v3/content/docker/manifests/1/

try:
    api_response = api_instance.content_docker_manifests_read(image_manifest_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_docker_manifests_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_manifest_href** | **str**| URI of Image Manifest. e.g.: /pulp/api/v3/content/docker/manifests/1/ | 

### Return type

[**Manifest**](Manifest.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_file_files_create**
> FileContent content_file_files_create(data)



ViewSet for FileContent.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.FileContent() # FileContent | 

try:
    api_response = api_instance.content_file_files_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_file_files_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FileContent**](FileContent.md)|  | 

### Return type

[**FileContent**](FileContent.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_file_files_list**
> InlineResponse2006 content_file_files_list(relative_path=relative_path, digest=digest, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)



ViewSet for FileContent.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
relative_path = 'relative_path_example' # str | Filter results where relative_path matches value (optional)
digest = 'digest_example' # str | Filter results where digest matches value (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.content_file_files_list(relative_path=relative_path, digest=digest, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_file_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relative_path** | **str**| Filter results where relative_path matches value | [optional] 
 **digest** | **str**| Filter results where digest matches value | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_file_files_read**
> FileContent content_file_files_read(file_content_href)



ViewSet for FileContent.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_content_href = 'file_content_href_example' # str | URI of File Content. e.g.: /pulp/api/v3/content/file/files/1/

try:
    api_response = api_instance.content_file_files_read(file_content_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_file_files_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_content_href** | **str**| URI of File Content. e.g.: /pulp/api/v3/content/file/files/1/ | 

### Return type

[**FileContent**](FileContent.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_errata_create**
> UpdateRecord content_rpm_errata_create(data)

A ViewSet for UpdateRecord.

Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/errata/  Also specify queryset and serializer for UpdateRecord.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.UpdateRecord() # UpdateRecord | 

try:
    # A ViewSet for UpdateRecord.
    api_response = api_instance.content_rpm_errata_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_errata_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UpdateRecord**](UpdateRecord.md)|  | 

### Return type

[**UpdateRecord**](UpdateRecord.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_errata_list**
> InlineResponse2007 content_rpm_errata_list(id=id, id__in=id__in, status=status, status__in=status__in, severity=severity, severity__in=severity__in, type=type, type__in=type__in, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)

A ViewSet for UpdateRecord.

Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/errata/  Also specify queryset and serializer for UpdateRecord.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
id = 'id_example' # str | Filter results where id matches value (optional)
id__in = 'id__in_example' # str | Filter results where id is in a comma-separated list of values (optional)
status = 'status_example' # str | Filter results where status matches value (optional)
status__in = 'status__in_example' # str | Filter results where status is in a comma-separated list of values (optional)
severity = 'severity_example' # str | Filter results where severity matches value (optional)
severity__in = 'severity__in_example' # str | Filter results where severity is in a comma-separated list of values (optional)
type = 'type_example' # str | Filter results where type matches value (optional)
type__in = 'type__in_example' # str | Filter results where type is in a comma-separated list of values (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # A ViewSet for UpdateRecord.
    api_response = api_instance.content_rpm_errata_list(id=id, id__in=id__in, status=status, status__in=status__in, severity=severity, severity__in=severity__in, type=type, type__in=type__in, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_errata_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Filter results where id matches value | [optional] 
 **id__in** | **str**| Filter results where id is in a comma-separated list of values | [optional] 
 **status** | **str**| Filter results where status matches value | [optional] 
 **status__in** | **str**| Filter results where status is in a comma-separated list of values | [optional] 
 **severity** | **str**| Filter results where severity matches value | [optional] 
 **severity__in** | **str**| Filter results where severity is in a comma-separated list of values | [optional] 
 **type** | **str**| Filter results where type matches value | [optional] 
 **type__in** | **str**| Filter results where type is in a comma-separated list of values | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_errata_read**
> UpdateRecord content_rpm_errata_read(update_record_href)

A ViewSet for UpdateRecord.

Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/errata/  Also specify queryset and serializer for UpdateRecord.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
update_record_href = 'update_record_href_example' # str | URI of Update Record. e.g.: /pulp/api/v3/content/rpm/errata/1/

try:
    # A ViewSet for UpdateRecord.
    api_response = api_instance.content_rpm_errata_read(update_record_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_errata_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_record_href** | **str**| URI of Update Record. e.g.: /pulp/api/v3/content/rpm/errata/1/ | 

### Return type

[**UpdateRecord**](UpdateRecord.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_packages_create**
> Package content_rpm_packages_create(data)



Create a new Package from a request.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Package() # Package | 

try:
    api_response = api_instance.content_rpm_packages_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_packages_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_packages_list**
> InlineResponse2008 content_rpm_packages_list(name=name, name__in=name__in, epoch=epoch, epoch__in=epoch__in, version=version, version__in=version__in, release=release, release__in=release__in, arch=arch, arch__in=arch__in, pkg_id=pkg_id, pkg_id__in=pkg_id__in, checksum_type=checksum_type, checksum_type__in=checksum_type__in, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)

A ViewSet for Package.

Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str | Filter results where name matches value (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
epoch = 'epoch_example' # str | Filter results where epoch matches value (optional)
epoch__in = 'epoch__in_example' # str | Filter results where epoch is in a comma-separated list of values (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
version__in = 'version__in_example' # str | Filter results where version is in a comma-separated list of values (optional)
release = 'release_example' # str | Filter results where release matches value (optional)
release__in = 'release__in_example' # str | Filter results where release is in a comma-separated list of values (optional)
arch = 'arch_example' # str | Filter results where arch matches value (optional)
arch__in = 'arch__in_example' # str | Filter results where arch is in a comma-separated list of values (optional)
pkg_id = 'pkg_id_example' # str | Filter results where pkgId matches value (optional)
pkg_id__in = 'pkg_id__in_example' # str | Filter results where pkgId is in a comma-separated list of values (optional)
checksum_type = 'checksum_type_example' # str | Filter results where checksum_type matches value (optional)
checksum_type__in = 'checksum_type__in_example' # str | Filter results where checksum_type is in a comma-separated list of values (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # A ViewSet for Package.
    api_response = api_instance.content_rpm_packages_list(name=name, name__in=name__in, epoch=epoch, epoch__in=epoch__in, version=version, version__in=version__in, release=release, release__in=release__in, arch=arch, arch__in=arch__in, pkg_id=pkg_id, pkg_id__in=pkg_id__in, checksum_type=checksum_type, checksum_type__in=checksum_type__in, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_packages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **epoch** | **str**| Filter results where epoch matches value | [optional] 
 **epoch__in** | **str**| Filter results where epoch is in a comma-separated list of values | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **version__in** | **str**| Filter results where version is in a comma-separated list of values | [optional] 
 **release** | **str**| Filter results where release matches value | [optional] 
 **release__in** | **str**| Filter results where release is in a comma-separated list of values | [optional] 
 **arch** | **str**| Filter results where arch matches value | [optional] 
 **arch__in** | **str**| Filter results where arch is in a comma-separated list of values | [optional] 
 **pkg_id** | **str**| Filter results where pkgId matches value | [optional] 
 **pkg_id__in** | **str**| Filter results where pkgId is in a comma-separated list of values | [optional] 
 **checksum_type** | **str**| Filter results where checksum_type matches value | [optional] 
 **checksum_type__in** | **str**| Filter results where checksum_type is in a comma-separated list of values | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_rpm_packages_read**
> Package content_rpm_packages_read(package_href)

A ViewSet for Package.

Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
package_href = 'package_href_example' # str | URI of Package. e.g.: /pulp/api/v3/content/rpm/packages/1/

try:
    # A ViewSet for Package.
    api_response = api_instance.content_rpm_packages_read(package_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->content_rpm_packages_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_href** | **str**| URI of Package. e.g.: /pulp/api/v3/content/rpm/packages/1/ | 

### Return type

[**Package**](Package.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_create**
> CertGuard contentguards_certguard_certguard_create(data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.CertGuard() # CertGuard | 

try:
    api_response = api_instance.contentguards_certguard_certguard_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CertGuard**](CertGuard.md)|  | 

### Return type

[**CertGuard**](CertGuard.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_delete**
> contentguards_certguard_certguard_delete(cert_guard_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
cert_guard_href = 'cert_guard_href_example' # str | URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/

try:
    api_instance.contentguards_certguard_certguard_delete(cert_guard_href)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_guard_href** | **str**| URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_list**
> InlineResponse2009 contentguards_certguard_certguard_list(name=name, name__in=name__in, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.contentguards_certguard_certguard_list(name=name, name__in=name__in, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_partial_update**
> CertGuard contentguards_certguard_certguard_partial_update(cert_guard_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
cert_guard_href = 'cert_guard_href_example' # str | URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/
data = juicer.CertGuard() # CertGuard | 

try:
    api_response = api_instance.contentguards_certguard_certguard_partial_update(cert_guard_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_guard_href** | **str**| URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/ | 
 **data** | [**CertGuard**](CertGuard.md)|  | 

### Return type

[**CertGuard**](CertGuard.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_read**
> CertGuard contentguards_certguard_certguard_read(cert_guard_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
cert_guard_href = 'cert_guard_href_example' # str | URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/

try:
    api_response = api_instance.contentguards_certguard_certguard_read(cert_guard_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_guard_href** | **str**| URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/ | 

### Return type

[**CertGuard**](CertGuard.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contentguards_certguard_certguard_update**
> CertGuard contentguards_certguard_certguard_update(cert_guard_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
cert_guard_href = 'cert_guard_href_example' # str | URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/
data = juicer.CertGuard() # CertGuard | 

try:
    api_response = api_instance.contentguards_certguard_certguard_update(cert_guard_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->contentguards_certguard_certguard_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cert_guard_href** | **str**| URI of Cert Guard. e.g.: /pulp/api/v3/contentguards/certguard/certguard/1/ | 
 **data** | [**CertGuard**](CertGuard.md)|  | 

### Return type

[**CertGuard**](CertGuard.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_create**
> Distribution distributions_create(data)



Trigger an asynchronous create task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_delete**
> distributions_delete(distribution_href)



Provides read and list methods and also provides asynchronous CUD methods to dispatch tasks with reservation that lock all Distributions preventing race conditions during base_path checking.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /pulp/api/v3/distributions/1/

try:
    api_instance.distributions_delete(distribution_href)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /pulp/api/v3/distributions/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_list**
> InlineResponse20010 distributions_list(name=name, name__in=name__in, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, page=page, page_size=page_size)



Provides read and list methods and also provides asynchronous CUD methods to dispatch tasks with reservation that lock all Distributions preventing race conditions during base_path checking.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
base_path = 'base_path_example' # str |  (optional)
base_path__contains = 'base_path__contains_example' # str | Filter results where base_path contains value (optional)
base_path__icontains = 'base_path__icontains_example' # str | Filter results where base_path contains value (optional)
base_path__in = 'base_path__in_example' # str | Filter results where base_path is in a comma-separated list of values (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.distributions_list(name=name, name__in=name__in, base_path=base_path, base_path__contains=base_path__contains, base_path__icontains=base_path__icontains, base_path__in=base_path__in, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **base_path** | **str**|  | [optional] 
 **base_path__contains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__icontains** | **str**| Filter results where base_path contains value | [optional] 
 **base_path__in** | **str**| Filter results where base_path is in a comma-separated list of values | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_partial_update**
> Distribution distributions_partial_update(distribution_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /pulp/api/v3/distributions/1/
data = juicer.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_partial_update(distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /pulp/api/v3/distributions/1/ | 
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_read**
> Distribution distributions_read(distribution_href)



Provides read and list methods and also provides asynchronous CUD methods to dispatch tasks with reservation that lock all Distributions preventing race conditions during base_path checking.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /pulp/api/v3/distributions/1/

try:
    api_response = api_instance.distributions_read(distribution_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /pulp/api/v3/distributions/1/ | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributions_update**
> Distribution distributions_update(distribution_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
distribution_href = 'distribution_href_example' # str | URI of Distribution. e.g.: /pulp/api/v3/distributions/1/
data = juicer.Distribution() # Distribution | 

try:
    api_response = api_instance.distributions_update(distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->distributions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_href** | **str**| URI of Distribution. e.g.: /pulp/api/v3/distributions/1/ | 
 **data** | [**Distribution**](Distribution.md)|  | 

### Return type

[**Distribution**](Distribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_create**
> DockerDistribution docker_distributions_create(data)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.DockerDistribution() # DockerDistribution | 

try:
    api_response = api_instance.docker_distributions_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DockerDistribution**](DockerDistribution.md)|  | 

### Return type

[**DockerDistribution**](DockerDistribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_delete**
> docker_distributions_delete(docker_distribution_href)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_distribution_href = 'docker_distribution_href_example' # str | URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/

try:
    api_instance.docker_distributions_delete(docker_distribution_href)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_distribution_href** | **str**| URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_list**
> InlineResponse20011 docker_distributions_list(page=page, page_size=page_size)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.docker_distributions_list(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_partial_update**
> DockerDistribution docker_distributions_partial_update(docker_distribution_href, data)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_distribution_href = 'docker_distribution_href_example' # str | URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/
data = juicer.DockerDistribution() # DockerDistribution | 

try:
    api_response = api_instance.docker_distributions_partial_update(docker_distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_distribution_href** | **str**| URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/ | 
 **data** | [**DockerDistribution**](DockerDistribution.md)|  | 

### Return type

[**DockerDistribution**](DockerDistribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_read**
> DockerDistribution docker_distributions_read(docker_distribution_href)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_distribution_href = 'docker_distribution_href_example' # str | URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/

try:
    api_response = api_instance.docker_distributions_read(docker_distribution_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_distribution_href** | **str**| URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/ | 

### Return type

[**DockerDistribution**](DockerDistribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **docker_distributions_update**
> DockerDistribution docker_distributions_update(docker_distribution_href, data)



ViewSet for DockerDistribution model.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_distribution_href = 'docker_distribution_href_example' # str | URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/
data = juicer.DockerDistribution() # DockerDistribution | 

try:
    api_response = api_instance.docker_distributions_update(docker_distribution_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->docker_distributions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_distribution_href** | **str**| URI of Docker Distribution. e.g.: /pulp/api/v3/docker-distributions/1/ | 
 **data** | [**DockerDistribution**](DockerDistribution.md)|  | 

### Return type

[**DockerDistribution**](DockerDistribution.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orphans_delete**
> orphans_delete()



Cleans up all the Content and Artifact orphans in the system

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))

try:
    api_instance.orphans_delete()
except ApiException as e:
    print("Exception when calling PulpApi->orphans_delete: %s\n" % e)
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

# **publications_delete**
> publications_delete(publication_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
publication_href = 'publication_href_example' # str | URI of Publication. e.g.: /pulp/api/v3/publications/1/

try:
    api_instance.publications_delete(publication_href)
except ApiException as e:
    print("Exception when calling PulpApi->publications_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_href** | **str**| URI of Publication. e.g.: /pulp/api/v3/publications/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publications_list**
> InlineResponse20012 publications_list(ordering=ordering, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.publications_list(ordering=ordering, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publications_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publications_read**
> Publication publications_read(publication_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
publication_href = 'publication_href_example' # str | URI of Publication. e.g.: /pulp/api/v3/publications/1/

try:
    api_response = api_instance.publications_read(publication_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publication_href** | **str**| URI of Publication. e.g.: /pulp/api/v3/publications/1/ | 

### Return type

[**Publication**](Publication.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_create**
> DockerPublisher publishers_docker_docker_create(data)



A ViewSet for DockerPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.DockerPublisher() # DockerPublisher | 

try:
    api_response = api_instance.publishers_docker_docker_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DockerPublisher**](DockerPublisher.md)|  | 

### Return type

[**DockerPublisher**](DockerPublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_delete**
> AsyncOperationResponse publishers_docker_docker_delete(docker_publisher_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_publisher_href = 'docker_publisher_href_example' # str | URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/

try:
    api_response = api_instance.publishers_docker_docker_delete(docker_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_publisher_href** | **str**| URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_list**
> InlineResponse20013 publishers_docker_docker_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



A ViewSet for DockerPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.publishers_docker_docker_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_partial_update**
> AsyncOperationResponse publishers_docker_docker_partial_update(docker_publisher_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_publisher_href = 'docker_publisher_href_example' # str | URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/
data = juicer.DockerPublisher() # DockerPublisher | 

try:
    api_response = api_instance.publishers_docker_docker_partial_update(docker_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_publisher_href** | **str**| URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/ | 
 **data** | [**DockerPublisher**](DockerPublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_publish**
> AsyncOperationResponse publishers_docker_docker_publish(docker_publisher_href, data)



Trigger an asynchronous task to publish content

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_publisher_href = 'docker_publisher_href_example' # str | URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/
data = juicer.RepositoryPublishURL() # RepositoryPublishURL | 

try:
    api_response = api_instance.publishers_docker_docker_publish(docker_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_publisher_href** | **str**| URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/ | 
 **data** | [**RepositoryPublishURL**](RepositoryPublishURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_read**
> DockerPublisher publishers_docker_docker_read(docker_publisher_href)



A ViewSet for DockerPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_publisher_href = 'docker_publisher_href_example' # str | URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/

try:
    api_response = api_instance.publishers_docker_docker_read(docker_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_publisher_href** | **str**| URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/ | 

### Return type

[**DockerPublisher**](DockerPublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_docker_docker_update**
> AsyncOperationResponse publishers_docker_docker_update(docker_publisher_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_publisher_href = 'docker_publisher_href_example' # str | URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/
data = juicer.DockerPublisher() # DockerPublisher | 

try:
    api_response = api_instance.publishers_docker_docker_update(docker_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_docker_docker_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_publisher_href** | **str**| URI of Docker Publisher. e.g.: /pulp/api/v3/publishers/docker/docker/1/ | 
 **data** | [**DockerPublisher**](DockerPublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_create**
> FilePublisher publishers_file_file_create(data)



ViewSet for File Publishers.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_file_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_delete**
> AsyncOperationResponse publishers_file_file_delete(file_publisher_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/

try:
    api_response = api_instance.publishers_file_file_delete(file_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_list**
> InlineResponse20014 publishers_file_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



ViewSet for File Publishers.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.publishers_file_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_partial_update**
> AsyncOperationResponse publishers_file_file_partial_update(file_publisher_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/
data = juicer.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_file_partial_update(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/ | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_publish**
> AsyncOperationResponse publishers_file_file_publish(file_publisher_href, data)



Trigger an asynchronous task to publish file content.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/
data = juicer.RepositoryPublishURL() # RepositoryPublishURL | 

try:
    api_response = api_instance.publishers_file_file_publish(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/ | 
 **data** | [**RepositoryPublishURL**](RepositoryPublishURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_read**
> FilePublisher publishers_file_file_read(file_publisher_href)



ViewSet for File Publishers.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/

try:
    api_response = api_instance.publishers_file_file_read(file_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/ | 

### Return type

[**FilePublisher**](FilePublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_file_file_update**
> AsyncOperationResponse publishers_file_file_update(file_publisher_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_publisher_href = 'file_publisher_href_example' # str | URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/
data = juicer.FilePublisher() # FilePublisher | 

try:
    api_response = api_instance.publishers_file_file_update(file_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_file_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_publisher_href** | **str**| URI of File Publisher. e.g.: /pulp/api/v3/publishers/file/file/1/ | 
 **data** | [**FilePublisher**](FilePublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_create**
> RpmPublisher publishers_rpm_rpm_create(data)



A ViewSet for RpmPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.RpmPublisher() # RpmPublisher | 

try:
    api_response = api_instance.publishers_rpm_rpm_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RpmPublisher**](RpmPublisher.md)|  | 

### Return type

[**RpmPublisher**](RpmPublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_delete**
> AsyncOperationResponse publishers_rpm_rpm_delete(rpm_publisher_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_publisher_href = 'rpm_publisher_href_example' # str | URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/

try:
    api_response = api_instance.publishers_rpm_rpm_delete(rpm_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_publisher_href** | **str**| URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_list**
> InlineResponse20015 publishers_rpm_rpm_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



A ViewSet for RpmPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.publishers_rpm_rpm_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_partial_update**
> AsyncOperationResponse publishers_rpm_rpm_partial_update(rpm_publisher_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_publisher_href = 'rpm_publisher_href_example' # str | URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/
data = juicer.RpmPublisher() # RpmPublisher | 

try:
    api_response = api_instance.publishers_rpm_rpm_partial_update(rpm_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_publisher_href** | **str**| URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/ | 
 **data** | [**RpmPublisher**](RpmPublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_publish**
> AsyncOperationResponse publishers_rpm_rpm_publish(rpm_publisher_href, data)



Trigger an asynchronous task to publish RPM content.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_publisher_href = 'rpm_publisher_href_example' # str | URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/
data = juicer.RepositoryPublishURL() # RepositoryPublishURL | 

try:
    api_response = api_instance.publishers_rpm_rpm_publish(rpm_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_publisher_href** | **str**| URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/ | 
 **data** | [**RepositoryPublishURL**](RepositoryPublishURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_read**
> RpmPublisher publishers_rpm_rpm_read(rpm_publisher_href)



A ViewSet for RpmPublisher.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_publisher_href = 'rpm_publisher_href_example' # str | URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/

try:
    api_response = api_instance.publishers_rpm_rpm_read(rpm_publisher_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_publisher_href** | **str**| URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/ | 

### Return type

[**RpmPublisher**](RpmPublisher.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publishers_rpm_rpm_update**
> AsyncOperationResponse publishers_rpm_rpm_update(rpm_publisher_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_publisher_href = 'rpm_publisher_href_example' # str | URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/
data = juicer.RpmPublisher() # RpmPublisher | 

try:
    api_response = api_instance.publishers_rpm_rpm_update(rpm_publisher_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->publishers_rpm_rpm_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_publisher_href** | **str**| URI of Rpm Publisher. e.g.: /pulp/api/v3/publishers/rpm/rpm/1/ | 
 **data** | [**RpmPublisher**](RpmPublisher.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_create**
> DockerRemote remotes_docker_docker_create(data)



A ViewSet for DockerRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.DockerRemote() # DockerRemote | 

try:
    api_response = api_instance.remotes_docker_docker_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DockerRemote**](DockerRemote.md)|  | 

### Return type

[**DockerRemote**](DockerRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_delete**
> AsyncOperationResponse remotes_docker_docker_delete(docker_remote_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_remote_href = 'docker_remote_href_example' # str | URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/

try:
    api_response = api_instance.remotes_docker_docker_delete(docker_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_remote_href** | **str**| URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_list**
> InlineResponse20016 remotes_docker_docker_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



A ViewSet for DockerRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.remotes_docker_docker_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_partial_update**
> AsyncOperationResponse remotes_docker_docker_partial_update(docker_remote_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_remote_href = 'docker_remote_href_example' # str | URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/
data = juicer.DockerRemote() # DockerRemote | 

try:
    api_response = api_instance.remotes_docker_docker_partial_update(docker_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_remote_href** | **str**| URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/ | 
 **data** | [**DockerRemote**](DockerRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_read**
> DockerRemote remotes_docker_docker_read(docker_remote_href)



A ViewSet for DockerRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_remote_href = 'docker_remote_href_example' # str | URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/

try:
    api_response = api_instance.remotes_docker_docker_read(docker_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_remote_href** | **str**| URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/ | 

### Return type

[**DockerRemote**](DockerRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_sync**
> AsyncOperationResponse remotes_docker_docker_sync(docker_remote_href, data)



Trigger an asynchronous task to sync content

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_remote_href = 'docker_remote_href_example' # str | URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/
data = juicer.RepositorySyncURL() # RepositorySyncURL | 

try:
    api_response = api_instance.remotes_docker_docker_sync(docker_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_remote_href** | **str**| URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/ | 
 **data** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_docker_docker_update**
> AsyncOperationResponse remotes_docker_docker_update(docker_remote_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
docker_remote_href = 'docker_remote_href_example' # str | URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/
data = juicer.DockerRemote() # DockerRemote | 

try:
    api_response = api_instance.remotes_docker_docker_update(docker_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_docker_docker_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_remote_href** | **str**| URI of Docker Remote. e.g.: /pulp/api/v3/remotes/docker/docker/1/ | 
 **data** | [**DockerRemote**](DockerRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_create**
> FileRemote remotes_file_file_create(data)



ViewSet for File Remotes.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_file_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_delete**
> AsyncOperationResponse remotes_file_file_delete(file_remote_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/

try:
    api_response = api_instance.remotes_file_file_delete(file_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_list**
> InlineResponse20017 remotes_file_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



ViewSet for File Remotes.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.remotes_file_file_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_partial_update**
> AsyncOperationResponse remotes_file_file_partial_update(file_remote_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/
data = juicer.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_file_partial_update(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/ | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_read**
> FileRemote remotes_file_file_read(file_remote_href)



ViewSet for File Remotes.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/

try:
    api_response = api_instance.remotes_file_file_read(file_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/ | 

### Return type

[**FileRemote**](FileRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_sync**
> AsyncOperationResponse remotes_file_file_sync(file_remote_href, data)



Trigger an asynchronous task to sync file content.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/
data = juicer.RepositorySyncURL() # RepositorySyncURL | 

try:
    api_response = api_instance.remotes_file_file_sync(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/ | 
 **data** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_file_file_update**
> AsyncOperationResponse remotes_file_file_update(file_remote_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
file_remote_href = 'file_remote_href_example' # str | URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/
data = juicer.FileRemote() # FileRemote | 

try:
    api_response = api_instance.remotes_file_file_update(file_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_file_file_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_remote_href** | **str**| URI of File Remote. e.g.: /pulp/api/v3/remotes/file/file/1/ | 
 **data** | [**FileRemote**](FileRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_create**
> RpmRemote remotes_rpm_rpm_create(data)



A ViewSet for RpmRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.RpmRemote() # RpmRemote | 

try:
    api_response = api_instance.remotes_rpm_rpm_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RpmRemote**](RpmRemote.md)|  | 

### Return type

[**RpmRemote**](RpmRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_delete**
> AsyncOperationResponse remotes_rpm_rpm_delete(rpm_remote_href)



Trigger an asynchronous delete task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_remote_href = 'rpm_remote_href_example' # str | URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/

try:
    api_response = api_instance.remotes_rpm_rpm_delete(rpm_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_remote_href** | **str**| URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_list**
> InlineResponse20018 remotes_rpm_rpm_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)



A ViewSet for RpmRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_updated__lt = 'last_updated__lt_example' # str | Filter results where _last_updated is less than value (optional)
last_updated__lte = 'last_updated__lte_example' # str | Filter results where _last_updated is less than or equal to value (optional)
last_updated__gt = 'last_updated__gt_example' # str | Filter results where _last_updated is greater than value (optional)
last_updated__gte = 'last_updated__gte_example' # str | Filter results where _last_updated is greater than or equal to value (optional)
last_updated__range = 'last_updated__range_example' # str | Filter results where _last_updated is between two comma separated values (optional)
last_updated = 'last_updated_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.remotes_rpm_rpm_list(name=name, name__in=name__in, last_updated__lt=last_updated__lt, last_updated__lte=last_updated__lte, last_updated__gt=last_updated__gt, last_updated__gte=last_updated__gte, last_updated__range=last_updated__range, last_updated=last_updated, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_updated__lt** | **str**| Filter results where _last_updated is less than value | [optional] 
 **last_updated__lte** | **str**| Filter results where _last_updated is less than or equal to value | [optional] 
 **last_updated__gt** | **str**| Filter results where _last_updated is greater than value | [optional] 
 **last_updated__gte** | **str**| Filter results where _last_updated is greater than or equal to value | [optional] 
 **last_updated__range** | **str**| Filter results where _last_updated is between two comma separated values | [optional] 
 **last_updated** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_partial_update**
> AsyncOperationResponse remotes_rpm_rpm_partial_update(rpm_remote_href, data)



Trigger an asynchronous partial update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_remote_href = 'rpm_remote_href_example' # str | URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/
data = juicer.RpmRemote() # RpmRemote | 

try:
    api_response = api_instance.remotes_rpm_rpm_partial_update(rpm_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_remote_href** | **str**| URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/ | 
 **data** | [**RpmRemote**](RpmRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_read**
> RpmRemote remotes_rpm_rpm_read(rpm_remote_href)



A ViewSet for RpmRemote.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_remote_href = 'rpm_remote_href_example' # str | URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/

try:
    api_response = api_instance.remotes_rpm_rpm_read(rpm_remote_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_remote_href** | **str**| URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/ | 

### Return type

[**RpmRemote**](RpmRemote.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_sync**
> AsyncOperationResponse remotes_rpm_rpm_sync(rpm_remote_href, data)



Trigger an asynchronous task to sync RPM content.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_remote_href = 'rpm_remote_href_example' # str | URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/
data = juicer.RepositorySyncURL() # RepositorySyncURL | 

try:
    api_response = api_instance.remotes_rpm_rpm_sync(rpm_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_remote_href** | **str**| URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/ | 
 **data** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remotes_rpm_rpm_update**
> AsyncOperationResponse remotes_rpm_rpm_update(rpm_remote_href, data)



Trigger an asynchronous update task

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
rpm_remote_href = 'rpm_remote_href_example' # str | URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/
data = juicer.RpmRemote() # RpmRemote | 

try:
    api_response = api_instance.remotes_rpm_rpm_update(rpm_remote_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->remotes_rpm_rpm_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_remote_href** | **str**| URI of Rpm Remote. e.g.: /pulp/api/v3/remotes/rpm/rpm/1/ | 
 **data** | [**RpmRemote**](RpmRemote.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_create**
> Repository repositories_create(data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Repository() # Repository | 

try:
    api_response = api_instance.repositories_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_delete**
> AsyncOperationResponse repositories_delete(repository_href)



Trigger an asynchronous task to delete a repository.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/

try:
    api_response = api_instance.repositories_delete(repository_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_list**
> InlineResponse20019 repositories_list(name=name, name__in=name__in, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.repositories_list(name=name, name__in=name__in, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_partial_update**
> Repository repositories_partial_update(repository_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/
data = juicer.Repository() # Repository | 

try:
    api_response = api_instance.repositories_partial_update(repository_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_read**
> Repository repositories_read(repository_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/

try:
    api_response = api_instance.repositories_read(repository_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 

### Return type

[**Repository**](Repository.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_update**
> AsyncOperationResponse repositories_update(repository_href, data)



Trigger an asynchronous task to updatea repository.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/
data = juicer.Repository() # Repository | 

try:
    api_response = api_instance.repositories_update(repository_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 
 **data** | [**Repository**](Repository.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_create**
> AsyncOperationResponse repositories_versions_create(repository_href, data)



Trigger an asynchronous task to create a new repository version.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/
data = juicer.RepositoryVersionCreate() # RepositoryVersionCreate | 

try:
    api_response = api_instance.repositories_versions_create(repository_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 
 **data** | [**RepositoryVersionCreate**](RepositoryVersionCreate.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_delete**
> AsyncOperationResponse repositories_versions_delete(repository_version_href)



Trigger an asynchronous task to delete a repositroy version.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_delete(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/ | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_list**
> InlineResponse20020 repositories_versions_list(repository_href, ordering=ordering, number=number, number__lt=number__lt, number__lte=number__lte, number__gt=number__gt, number__gte=number__gte, number__range=number__range, created__lt=created__lt, created__lte=created__lte, created__gt=created__gt, created__gte=created__gte, created__range=created__range, content=content, created=created, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_href = 'repository_href_example' # str | URI of Repository. e.g.: /pulp/api/v3/repositories/1/
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
number = 8.14 # float |  (optional)
number__lt = 8.14 # float | Filter results where number is less than value (optional)
number__lte = 8.14 # float | Filter results where number is less than or equal to value (optional)
number__gt = 8.14 # float | Filter results where number is greater than value (optional)
number__gte = 8.14 # float | Filter results where number is greater than or equal to value (optional)
number__range = 8.14 # float | Filter results where number is between two comma separated values (optional)
created__lt = 'created__lt_example' # str | Filter results where _created is less than value (optional)
created__lte = 'created__lte_example' # str | Filter results where _created is less than or equal to value (optional)
created__gt = 'created__gt_example' # str | Filter results where _created is greater than value (optional)
created__gte = 'created__gte_example' # str | Filter results where _created is greater than or equal to value (optional)
created__range = 'created__range_example' # str | Filter results where _created is between two comma separated values (optional)
content = 'content_example' # str | Content Unit referenced by HREF (optional)
created = 'created_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.repositories_versions_list(repository_href, ordering=ordering, number=number, number__lt=number__lt, number__lte=number__lte, number__gt=number__gt, number__gte=number__gte, number__range=number__range, created__lt=created__lt, created__lte=created__lte, created__gt=created__gt, created__gte=created__gte, created__range=created__range, content=content, created=created, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_href** | **str**| URI of Repository. e.g.: /pulp/api/v3/repositories/1/ | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **number** | **float**|  | [optional] 
 **number__lt** | **float**| Filter results where number is less than value | [optional] 
 **number__lte** | **float**| Filter results where number is less than or equal to value | [optional] 
 **number__gt** | **float**| Filter results where number is greater than value | [optional] 
 **number__gte** | **float**| Filter results where number is greater than or equal to value | [optional] 
 **number__range** | **float**| Filter results where number is between two comma separated values | [optional] 
 **created__lt** | **str**| Filter results where _created is less than value | [optional] 
 **created__lte** | **str**| Filter results where _created is less than or equal to value | [optional] 
 **created__gt** | **str**| Filter results where _created is greater than value | [optional] 
 **created__gte** | **str**| Filter results where _created is greater than or equal to value | [optional] 
 **created__range** | **str**| Filter results where _created is between two comma separated values | [optional] 
 **content** | **str**| Content Unit referenced by HREF | [optional] 
 **created** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_partial_update**
> RepositoryVersion repositories_versions_partial_update(repository_version_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/
data = juicer.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_partial_update(repository_version_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/ | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_read**
> RepositoryVersion repositories_versions_read(repository_version_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/

try:
    api_response = api_instance.repositories_versions_read(repository_version_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/ | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_versions_update**
> RepositoryVersion repositories_versions_update(repository_version_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
repository_version_href = 'repository_version_href_example' # str | URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/
data = juicer.RepositoryVersion() # RepositoryVersion | 

try:
    api_response = api_instance.repositories_versions_update(repository_version_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_versions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_version_href** | **str**| URI of Repository Version. e.g.: /pulp/api/v3/repositories/1/versions/1/ | 
 **data** | [**RepositoryVersion**](RepositoryVersion.md)|  | 

### Return type

[**RepositoryVersion**](RepositoryVersion.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_list**
> status_list()



Returns app information including the version of pulpcore and loaded pulp plugins, known workers, database connection status, and messaging connection status

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))

try:
    api_instance.status_list()
except ApiException as e:
    print("Exception when calling PulpApi->status_list: %s\n" % e)
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

# **tasks_cancel**
> Task tasks_cancel(task_href, data)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
task_href = 'task_href_example' # str | URI of Task. e.g.: /pulp/api/v3/tasks/1/
data = juicer.Task() # Task | 

try:
    api_response = api_instance.tasks_cancel(task_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->tasks_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /pulp/api/v3/tasks/1/ | 
 **data** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_delete**
> tasks_delete(task_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
task_href = 'task_href_example' # str | URI of Task. e.g.: /pulp/api/v3/tasks/1/

try:
    api_instance.tasks_delete(task_href)
except ApiException as e:
    print("Exception when calling PulpApi->tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /pulp/api/v3/tasks/1/ | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_list**
> InlineResponse20021 tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, name__contains=name__contains, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, name=name, started_at=started_at, finished_at=finished_at, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
state = 'state_example' # str |  (optional)
state__in = 'state__in_example' # str | Filter results where state is in a comma-separated list of values (optional)
worker = 'worker_example' # str | Foreign Key referenced by HREF (optional)
worker__in = 'worker__in_example' # str | Filter results where worker is in a comma-separated list of values (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
started_at__lt = 'started_at__lt_example' # str | Filter results where started_at is less than value (optional)
started_at__lte = 'started_at__lte_example' # str | Filter results where started_at is less than or equal to value (optional)
started_at__gt = 'started_at__gt_example' # str | Filter results where started_at is greater than value (optional)
started_at__gte = 'started_at__gte_example' # str | Filter results where started_at is greater than or equal to value (optional)
started_at__range = 'started_at__range_example' # str | Filter results where started_at is between two comma separated values (optional)
finished_at__lt = 'finished_at__lt_example' # str | Filter results where finished_at is less than value (optional)
finished_at__lte = 'finished_at__lte_example' # str | Filter results where finished_at is less than or equal to value (optional)
finished_at__gt = 'finished_at__gt_example' # str | Filter results where finished_at is greater than value (optional)
finished_at__gte = 'finished_at__gte_example' # str | Filter results where finished_at is greater than or equal to value (optional)
finished_at__range = 'finished_at__range_example' # str | Filter results where finished_at is between two comma separated values (optional)
parent = 'parent_example' # str | Foreign Key referenced by HREF (optional)
name = 'name_example' # str |  (optional)
started_at = 'started_at_example' # str | ISO 8601 formatted dates are supported (optional)
finished_at = 'finished_at_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.tasks_list(ordering=ordering, state=state, state__in=state__in, worker=worker, worker__in=worker__in, name__contains=name__contains, started_at__lt=started_at__lt, started_at__lte=started_at__lte, started_at__gt=started_at__gt, started_at__gte=started_at__gte, started_at__range=started_at__range, finished_at__lt=finished_at__lt, finished_at__lte=finished_at__lte, finished_at__gt=finished_at__gt, finished_at__gte=finished_at__gte, finished_at__range=finished_at__range, parent=parent, name=name, started_at=started_at, finished_at=finished_at, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **state** | **str**|  | [optional] 
 **state__in** | **str**| Filter results where state is in a comma-separated list of values | [optional] 
 **worker** | **str**| Foreign Key referenced by HREF | [optional] 
 **worker__in** | **str**| Filter results where worker is in a comma-separated list of values | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **started_at__lt** | **str**| Filter results where started_at is less than value | [optional] 
 **started_at__lte** | **str**| Filter results where started_at is less than or equal to value | [optional] 
 **started_at__gt** | **str**| Filter results where started_at is greater than value | [optional] 
 **started_at__gte** | **str**| Filter results where started_at is greater than or equal to value | [optional] 
 **started_at__range** | **str**| Filter results where started_at is between two comma separated values | [optional] 
 **finished_at__lt** | **str**| Filter results where finished_at is less than value | [optional] 
 **finished_at__lte** | **str**| Filter results where finished_at is less than or equal to value | [optional] 
 **finished_at__gt** | **str**| Filter results where finished_at is greater than value | [optional] 
 **finished_at__gte** | **str**| Filter results where finished_at is greater than or equal to value | [optional] 
 **finished_at__range** | **str**| Filter results where finished_at is between two comma separated values | [optional] 
 **parent** | **str**| Foreign Key referenced by HREF | [optional] 
 **name** | **str**|  | [optional] 
 **started_at** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **finished_at** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> Task tasks_read(task_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
task_href = 'task_href_example' # str | URI of Task. e.g.: /pulp/api/v3/tasks/1/

try:
    api_response = api_instance.tasks_read(task_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_href** | **str**| URI of Task. e.g.: /pulp/api/v3/tasks/1/ | 

### Return type

[**Task**](Task.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_create**
> Upload uploads_create(data)



Handle POST requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Upload() # Upload | 

try:
    api_response = api_instance.uploads_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Upload**](Upload.md)|  | 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_create_0**
> Upload uploads_create_0(upload_href, data)



Handle POST requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
upload_href = 'upload_href_example' # str | URI of Upload. e.g.: /pulp/api/v3/uploads/1/
data = juicer.Upload() # Upload | 

try:
    api_response = api_instance.uploads_create_0(upload_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_create_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_href** | **str**| URI of Upload. e.g.: /pulp/api/v3/uploads/1/ | 
 **data** | [**Upload**](Upload.md)|  | 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_read**
> Upload uploads_read()



Handle GET requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))

try:
    api_response = api_instance.uploads_read()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_read_0**
> Upload uploads_read_0(upload_href)



Handle GET requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
upload_href = 'upload_href_example' # str | URI of Upload. e.g.: /pulp/api/v3/uploads/1/

try:
    api_response = api_instance.uploads_read_0(upload_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_read_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_href** | **str**| URI of Upload. e.g.: /pulp/api/v3/uploads/1/ | 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_update**
> Upload uploads_update(data)



Handle PUT requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
data = juicer.Upload() # Upload | 

try:
    api_response = api_instance.uploads_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Upload**](Upload.md)|  | 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploads_update_0**
> Upload uploads_update_0(upload_href, data)



Handle PUT requests.

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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
upload_href = 'upload_href_example' # str | URI of Upload. e.g.: /pulp/api/v3/uploads/1/
data = juicer.Upload() # Upload | 

try:
    api_response = api_instance.uploads_update_0(upload_href, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->uploads_update_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_href** | **str**| URI of Upload. e.g.: /pulp/api/v3/uploads/1/ | 
 **data** | [**Upload**](Upload.md)|  | 

### Return type

[**Upload**](Upload.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workers_list**
> InlineResponse20022 workers_list(name=name, name__in=name__in, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__range=last_heartbeat__range, online=online, missing=missing, last_heartbeat=last_heartbeat, page=page, page_size=page_size)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
name = 'name_example' # str |  (optional)
name__in = 'name__in_example' # str | Filter results where name is in a comma-separated list of values (optional)
last_heartbeat__lt = 'last_heartbeat__lt_example' # str | Filter results where last_heartbeat is less than value (optional)
last_heartbeat__lte = 'last_heartbeat__lte_example' # str | Filter results where last_heartbeat is less than or equal to value (optional)
last_heartbeat__gt = 'last_heartbeat__gt_example' # str | Filter results where last_heartbeat is greater than value (optional)
last_heartbeat__gte = 'last_heartbeat__gte_example' # str | Filter results where last_heartbeat is greater than or equal to value (optional)
last_heartbeat__range = 'last_heartbeat__range_example' # str | Filter results where last_heartbeat is between two comma separated values (optional)
online = 'online_example' # str |  (optional)
missing = 'missing_example' # str |  (optional)
last_heartbeat = 'last_heartbeat_example' # str | ISO 8601 formatted dates are supported (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    api_response = api_instance.workers_list(name=name, name__in=name__in, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__range=last_heartbeat__range, online=online, missing=missing, last_heartbeat=last_heartbeat, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->workers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **name__in** | **str**| Filter results where name is in a comma-separated list of values | [optional] 
 **last_heartbeat__lt** | **str**| Filter results where last_heartbeat is less than value | [optional] 
 **last_heartbeat__lte** | **str**| Filter results where last_heartbeat is less than or equal to value | [optional] 
 **last_heartbeat__gt** | **str**| Filter results where last_heartbeat is greater than value | [optional] 
 **last_heartbeat__gte** | **str**| Filter results where last_heartbeat is greater than or equal to value | [optional] 
 **last_heartbeat__range** | **str**| Filter results where last_heartbeat is between two comma separated values | [optional] 
 **online** | **str**|  | [optional] 
 **missing** | **str**|  | [optional] 
 **last_heartbeat** | **str**| ISO 8601 formatted dates are supported | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workers_read**
> Worker workers_read(worker_href)





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
api_instance = juicer.PulpApi(juicer.ApiClient(configuration))
worker_href = 'worker_href_example' # str | URI of Worker. e.g.: /pulp/api/v3/workers/1/

try:
    api_response = api_instance.workers_read(worker_href)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->workers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker_href** | **str**| URI of Worker. e.g.: /pulp/api/v3/workers/1/ | 

### Return type

[**Worker**](Worker.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

