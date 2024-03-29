# pulp3-juicer

[![Build Status](https://travis-ci.com/rochacbruno/pulp3-juicer.svg?branch=master)](https://travis-ci.com/rochacbruno/pulp3-juicer)


Why Smash the Pulp by hand when you can use a Juicer?

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v3
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/rochacbruno/pulp3-juicer.git
```

Then import the package:
```python
import juicer 
```

### From source


```sh
git clone https://github.com/rochacbruno/pulp3-juicer.git
cd pulp3-juicer
python setup.py install --user
```

Then import the package:
```python
import juicer
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import juicer
from juicer.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
juicer.configuration.username = 'admin'
juicer.configuration.password = 'admin'

# create an instance of the API class
api_instance = juicer.PulpApi()

try:
    api_response = api_instance.repositories_create(juicer.Repository(name='foo'))
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PulpApi->repositories_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://192.168.122.18*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PulpApi* | [**artifacts_create**](docs/PulpApi.md#artifacts_create) | **POST** /pulp/api/v3/artifacts/ | 
*PulpApi* | [**artifacts_delete**](docs/PulpApi.md#artifacts_delete) | **DELETE** {artifact_href} | 
*PulpApi* | [**artifacts_list**](docs/PulpApi.md#artifacts_list) | **GET** /pulp/api/v3/artifacts/ | 
*PulpApi* | [**artifacts_read**](docs/PulpApi.md#artifacts_read) | **GET** {artifact_href} | 
*PulpApi* | [**content_docker_blobs_create**](docs/PulpApi.md#content_docker_blobs_create) | **POST** /pulp/api/v3/content/docker/blobs/ | 
*PulpApi* | [**content_docker_blobs_list**](docs/PulpApi.md#content_docker_blobs_list) | **GET** /pulp/api/v3/content/docker/blobs/ | 
*PulpApi* | [**content_docker_blobs_read**](docs/PulpApi.md#content_docker_blobs_read) | **GET** {manifest_blob_href} | 
*PulpApi* | [**content_docker_manifest_list_tags_create**](docs/PulpApi.md#content_docker_manifest_list_tags_create) | **POST** /pulp/api/v3/content/docker/manifest-list-tags/ | 
*PulpApi* | [**content_docker_manifest_list_tags_list**](docs/PulpApi.md#content_docker_manifest_list_tags_list) | **GET** /pulp/api/v3/content/docker/manifest-list-tags/ | 
*PulpApi* | [**content_docker_manifest_list_tags_read**](docs/PulpApi.md#content_docker_manifest_list_tags_read) | **GET** {manifest_list_tag_href} | 
*PulpApi* | [**content_docker_manifest_lists_create**](docs/PulpApi.md#content_docker_manifest_lists_create) | **POST** /pulp/api/v3/content/docker/manifest-lists/ | 
*PulpApi* | [**content_docker_manifest_lists_list**](docs/PulpApi.md#content_docker_manifest_lists_list) | **GET** /pulp/api/v3/content/docker/manifest-lists/ | 
*PulpApi* | [**content_docker_manifest_lists_read**](docs/PulpApi.md#content_docker_manifest_lists_read) | **GET** {manifest_list_href} | 
*PulpApi* | [**content_docker_manifest_tags_create**](docs/PulpApi.md#content_docker_manifest_tags_create) | **POST** /pulp/api/v3/content/docker/manifest-tags/ | 
*PulpApi* | [**content_docker_manifest_tags_list**](docs/PulpApi.md#content_docker_manifest_tags_list) | **GET** /pulp/api/v3/content/docker/manifest-tags/ | 
*PulpApi* | [**content_docker_manifest_tags_read**](docs/PulpApi.md#content_docker_manifest_tags_read) | **GET** {manifest_tag_href} | 
*PulpApi* | [**content_docker_manifests_create**](docs/PulpApi.md#content_docker_manifests_create) | **POST** /pulp/api/v3/content/docker/manifests/ | 
*PulpApi* | [**content_docker_manifests_list**](docs/PulpApi.md#content_docker_manifests_list) | **GET** /pulp/api/v3/content/docker/manifests/ | 
*PulpApi* | [**content_docker_manifests_read**](docs/PulpApi.md#content_docker_manifests_read) | **GET** {image_manifest_href} | 
*PulpApi* | [**content_file_files_create**](docs/PulpApi.md#content_file_files_create) | **POST** /pulp/api/v3/content/file/files/ | 
*PulpApi* | [**content_file_files_list**](docs/PulpApi.md#content_file_files_list) | **GET** /pulp/api/v3/content/file/files/ | 
*PulpApi* | [**content_file_files_read**](docs/PulpApi.md#content_file_files_read) | **GET** {file_content_href} | 
*PulpApi* | [**content_rpm_errata_create**](docs/PulpApi.md#content_rpm_errata_create) | **POST** /pulp/api/v3/content/rpm/errata/ | A ViewSet for UpdateRecord.
*PulpApi* | [**content_rpm_errata_list**](docs/PulpApi.md#content_rpm_errata_list) | **GET** /pulp/api/v3/content/rpm/errata/ | A ViewSet for UpdateRecord.
*PulpApi* | [**content_rpm_errata_read**](docs/PulpApi.md#content_rpm_errata_read) | **GET** {update_record_href} | A ViewSet for UpdateRecord.
*PulpApi* | [**content_rpm_packages_create**](docs/PulpApi.md#content_rpm_packages_create) | **POST** /pulp/api/v3/content/rpm/packages/ | 
*PulpApi* | [**content_rpm_packages_list**](docs/PulpApi.md#content_rpm_packages_list) | **GET** /pulp/api/v3/content/rpm/packages/ | A ViewSet for Package.
*PulpApi* | [**content_rpm_packages_read**](docs/PulpApi.md#content_rpm_packages_read) | **GET** {package_href} | A ViewSet for Package.
*PulpApi* | [**contentguards_certguard_certguard_create**](docs/PulpApi.md#contentguards_certguard_certguard_create) | **POST** /pulp/api/v3/contentguards/certguard/certguard/ | 
*PulpApi* | [**contentguards_certguard_certguard_delete**](docs/PulpApi.md#contentguards_certguard_certguard_delete) | **DELETE** {cert_guard_href} | 
*PulpApi* | [**contentguards_certguard_certguard_list**](docs/PulpApi.md#contentguards_certguard_certguard_list) | **GET** /pulp/api/v3/contentguards/certguard/certguard/ | 
*PulpApi* | [**contentguards_certguard_certguard_partial_update**](docs/PulpApi.md#contentguards_certguard_certguard_partial_update) | **PATCH** {cert_guard_href} | 
*PulpApi* | [**contentguards_certguard_certguard_read**](docs/PulpApi.md#contentguards_certguard_certguard_read) | **GET** {cert_guard_href} | 
*PulpApi* | [**contentguards_certguard_certguard_update**](docs/PulpApi.md#contentguards_certguard_certguard_update) | **PUT** {cert_guard_href} | 
*PulpApi* | [**distributions_create**](docs/PulpApi.md#distributions_create) | **POST** /pulp/api/v3/distributions/ | 
*PulpApi* | [**distributions_delete**](docs/PulpApi.md#distributions_delete) | **DELETE** {distribution_href} | 
*PulpApi* | [**distributions_list**](docs/PulpApi.md#distributions_list) | **GET** /pulp/api/v3/distributions/ | 
*PulpApi* | [**distributions_partial_update**](docs/PulpApi.md#distributions_partial_update) | **PATCH** {distribution_href} | 
*PulpApi* | [**distributions_read**](docs/PulpApi.md#distributions_read) | **GET** {distribution_href} | 
*PulpApi* | [**distributions_update**](docs/PulpApi.md#distributions_update) | **PUT** {distribution_href} | 
*PulpApi* | [**docker_distributions_create**](docs/PulpApi.md#docker_distributions_create) | **POST** /pulp/api/v3/docker-distributions/ | 
*PulpApi* | [**docker_distributions_delete**](docs/PulpApi.md#docker_distributions_delete) | **DELETE** {docker_distribution_href} | 
*PulpApi* | [**docker_distributions_list**](docs/PulpApi.md#docker_distributions_list) | **GET** /pulp/api/v3/docker-distributions/ | 
*PulpApi* | [**docker_distributions_partial_update**](docs/PulpApi.md#docker_distributions_partial_update) | **PATCH** {docker_distribution_href} | 
*PulpApi* | [**docker_distributions_read**](docs/PulpApi.md#docker_distributions_read) | **GET** {docker_distribution_href} | 
*PulpApi* | [**docker_distributions_update**](docs/PulpApi.md#docker_distributions_update) | **PUT** {docker_distribution_href} | 
*PulpApi* | [**orphans_delete**](docs/PulpApi.md#orphans_delete) | **DELETE** /pulp/api/v3/orphans/ | 
*PulpApi* | [**publications_delete**](docs/PulpApi.md#publications_delete) | **DELETE** {publication_href} | 
*PulpApi* | [**publications_list**](docs/PulpApi.md#publications_list) | **GET** /pulp/api/v3/publications/ | 
*PulpApi* | [**publications_read**](docs/PulpApi.md#publications_read) | **GET** {publication_href} | 
*PulpApi* | [**publishers_docker_docker_create**](docs/PulpApi.md#publishers_docker_docker_create) | **POST** /pulp/api/v3/publishers/docker/docker/ | 
*PulpApi* | [**publishers_docker_docker_delete**](docs/PulpApi.md#publishers_docker_docker_delete) | **DELETE** {docker_publisher_href} | 
*PulpApi* | [**publishers_docker_docker_list**](docs/PulpApi.md#publishers_docker_docker_list) | **GET** /pulp/api/v3/publishers/docker/docker/ | 
*PulpApi* | [**publishers_docker_docker_partial_update**](docs/PulpApi.md#publishers_docker_docker_partial_update) | **PATCH** {docker_publisher_href} | 
*PulpApi* | [**publishers_docker_docker_publish**](docs/PulpApi.md#publishers_docker_docker_publish) | **POST** {docker_publisher_href}publish/ | 
*PulpApi* | [**publishers_docker_docker_read**](docs/PulpApi.md#publishers_docker_docker_read) | **GET** {docker_publisher_href} | 
*PulpApi* | [**publishers_docker_docker_update**](docs/PulpApi.md#publishers_docker_docker_update) | **PUT** {docker_publisher_href} | 
*PulpApi* | [**publishers_file_file_create**](docs/PulpApi.md#publishers_file_file_create) | **POST** /pulp/api/v3/publishers/file/file/ | 
*PulpApi* | [**publishers_file_file_delete**](docs/PulpApi.md#publishers_file_file_delete) | **DELETE** {file_publisher_href} | 
*PulpApi* | [**publishers_file_file_list**](docs/PulpApi.md#publishers_file_file_list) | **GET** /pulp/api/v3/publishers/file/file/ | 
*PulpApi* | [**publishers_file_file_partial_update**](docs/PulpApi.md#publishers_file_file_partial_update) | **PATCH** {file_publisher_href} | 
*PulpApi* | [**publishers_file_file_publish**](docs/PulpApi.md#publishers_file_file_publish) | **POST** {file_publisher_href}publish/ | 
*PulpApi* | [**publishers_file_file_read**](docs/PulpApi.md#publishers_file_file_read) | **GET** {file_publisher_href} | 
*PulpApi* | [**publishers_file_file_update**](docs/PulpApi.md#publishers_file_file_update) | **PUT** {file_publisher_href} | 
*PulpApi* | [**publishers_rpm_rpm_create**](docs/PulpApi.md#publishers_rpm_rpm_create) | **POST** /pulp/api/v3/publishers/rpm/rpm/ | 
*PulpApi* | [**publishers_rpm_rpm_delete**](docs/PulpApi.md#publishers_rpm_rpm_delete) | **DELETE** {rpm_publisher_href} | 
*PulpApi* | [**publishers_rpm_rpm_list**](docs/PulpApi.md#publishers_rpm_rpm_list) | **GET** /pulp/api/v3/publishers/rpm/rpm/ | 
*PulpApi* | [**publishers_rpm_rpm_partial_update**](docs/PulpApi.md#publishers_rpm_rpm_partial_update) | **PATCH** {rpm_publisher_href} | 
*PulpApi* | [**publishers_rpm_rpm_publish**](docs/PulpApi.md#publishers_rpm_rpm_publish) | **POST** {rpm_publisher_href}publish/ | 
*PulpApi* | [**publishers_rpm_rpm_read**](docs/PulpApi.md#publishers_rpm_rpm_read) | **GET** {rpm_publisher_href} | 
*PulpApi* | [**publishers_rpm_rpm_update**](docs/PulpApi.md#publishers_rpm_rpm_update) | **PUT** {rpm_publisher_href} | 
*PulpApi* | [**remotes_docker_docker_create**](docs/PulpApi.md#remotes_docker_docker_create) | **POST** /pulp/api/v3/remotes/docker/docker/ | 
*PulpApi* | [**remotes_docker_docker_delete**](docs/PulpApi.md#remotes_docker_docker_delete) | **DELETE** {docker_remote_href} | 
*PulpApi* | [**remotes_docker_docker_list**](docs/PulpApi.md#remotes_docker_docker_list) | **GET** /pulp/api/v3/remotes/docker/docker/ | 
*PulpApi* | [**remotes_docker_docker_partial_update**](docs/PulpApi.md#remotes_docker_docker_partial_update) | **PATCH** {docker_remote_href} | 
*PulpApi* | [**remotes_docker_docker_read**](docs/PulpApi.md#remotes_docker_docker_read) | **GET** {docker_remote_href} | 
*PulpApi* | [**remotes_docker_docker_sync**](docs/PulpApi.md#remotes_docker_docker_sync) | **POST** {docker_remote_href}sync/ | 
*PulpApi* | [**remotes_docker_docker_update**](docs/PulpApi.md#remotes_docker_docker_update) | **PUT** {docker_remote_href} | 
*PulpApi* | [**remotes_file_file_create**](docs/PulpApi.md#remotes_file_file_create) | **POST** /pulp/api/v3/remotes/file/file/ | 
*PulpApi* | [**remotes_file_file_delete**](docs/PulpApi.md#remotes_file_file_delete) | **DELETE** {file_remote_href} | 
*PulpApi* | [**remotes_file_file_list**](docs/PulpApi.md#remotes_file_file_list) | **GET** /pulp/api/v3/remotes/file/file/ | 
*PulpApi* | [**remotes_file_file_partial_update**](docs/PulpApi.md#remotes_file_file_partial_update) | **PATCH** {file_remote_href} | 
*PulpApi* | [**remotes_file_file_read**](docs/PulpApi.md#remotes_file_file_read) | **GET** {file_remote_href} | 
*PulpApi* | [**remotes_file_file_sync**](docs/PulpApi.md#remotes_file_file_sync) | **POST** {file_remote_href}sync/ | 
*PulpApi* | [**remotes_file_file_update**](docs/PulpApi.md#remotes_file_file_update) | **PUT** {file_remote_href} | 
*PulpApi* | [**remotes_rpm_rpm_create**](docs/PulpApi.md#remotes_rpm_rpm_create) | **POST** /pulp/api/v3/remotes/rpm/rpm/ | 
*PulpApi* | [**remotes_rpm_rpm_delete**](docs/PulpApi.md#remotes_rpm_rpm_delete) | **DELETE** {rpm_remote_href} | 
*PulpApi* | [**remotes_rpm_rpm_list**](docs/PulpApi.md#remotes_rpm_rpm_list) | **GET** /pulp/api/v3/remotes/rpm/rpm/ | 
*PulpApi* | [**remotes_rpm_rpm_partial_update**](docs/PulpApi.md#remotes_rpm_rpm_partial_update) | **PATCH** {rpm_remote_href} | 
*PulpApi* | [**remotes_rpm_rpm_read**](docs/PulpApi.md#remotes_rpm_rpm_read) | **GET** {rpm_remote_href} | 
*PulpApi* | [**remotes_rpm_rpm_sync**](docs/PulpApi.md#remotes_rpm_rpm_sync) | **POST** {rpm_remote_href}sync/ | 
*PulpApi* | [**remotes_rpm_rpm_update**](docs/PulpApi.md#remotes_rpm_rpm_update) | **PUT** {rpm_remote_href} | 
*PulpApi* | [**repositories_create**](docs/PulpApi.md#repositories_create) | **POST** /pulp/api/v3/repositories/ | 
*PulpApi* | [**repositories_delete**](docs/PulpApi.md#repositories_delete) | **DELETE** {repository_href} | 
*PulpApi* | [**repositories_list**](docs/PulpApi.md#repositories_list) | **GET** /pulp/api/v3/repositories/ | 
*PulpApi* | [**repositories_partial_update**](docs/PulpApi.md#repositories_partial_update) | **PATCH** {repository_href} | 
*PulpApi* | [**repositories_read**](docs/PulpApi.md#repositories_read) | **GET** {repository_href} | 
*PulpApi* | [**repositories_update**](docs/PulpApi.md#repositories_update) | **PUT** {repository_href} | 
*PulpApi* | [**repositories_versions_create**](docs/PulpApi.md#repositories_versions_create) | **POST** {repository_href}versions/ | 
*PulpApi* | [**repositories_versions_delete**](docs/PulpApi.md#repositories_versions_delete) | **DELETE** {repository_version_href} | 
*PulpApi* | [**repositories_versions_list**](docs/PulpApi.md#repositories_versions_list) | **GET** {repository_href}versions/ | 
*PulpApi* | [**repositories_versions_partial_update**](docs/PulpApi.md#repositories_versions_partial_update) | **PATCH** {repository_version_href} | 
*PulpApi* | [**repositories_versions_read**](docs/PulpApi.md#repositories_versions_read) | **GET** {repository_version_href} | 
*PulpApi* | [**repositories_versions_update**](docs/PulpApi.md#repositories_versions_update) | **PUT** {repository_version_href} | 
*PulpApi* | [**status_list**](docs/PulpApi.md#status_list) | **GET** /pulp/api/v3/status/ | 
*PulpApi* | [**tasks_cancel**](docs/PulpApi.md#tasks_cancel) | **POST** {task_href}cancel/ | 
*PulpApi* | [**tasks_delete**](docs/PulpApi.md#tasks_delete) | **DELETE** {task_href} | 
*PulpApi* | [**tasks_list**](docs/PulpApi.md#tasks_list) | **GET** /pulp/api/v3/tasks/ | 
*PulpApi* | [**tasks_read**](docs/PulpApi.md#tasks_read) | **GET** {task_href} | 
*PulpApi* | [**uploads_create**](docs/PulpApi.md#uploads_create) | **POST** /pulp/api/v3/uploads/ | 
*PulpApi* | [**uploads_create_0**](docs/PulpApi.md#uploads_create_0) | **POST** {upload_href} | 
*PulpApi* | [**uploads_read**](docs/PulpApi.md#uploads_read) | **GET** /pulp/api/v3/uploads/ | 
*PulpApi* | [**uploads_read_0**](docs/PulpApi.md#uploads_read_0) | **GET** {upload_href} | 
*PulpApi* | [**uploads_update**](docs/PulpApi.md#uploads_update) | **PUT** /pulp/api/v3/uploads/ | 
*PulpApi* | [**uploads_update_0**](docs/PulpApi.md#uploads_update_0) | **PUT** {upload_href} | 
*PulpApi* | [**workers_list**](docs/PulpApi.md#workers_list) | **GET** /pulp/api/v3/workers/ | 
*PulpApi* | [**workers_read**](docs/PulpApi.md#workers_read) | **GET** {worker_href} | 
*RpmApi* | [**rpm_upload_create**](docs/RpmApi.md#rpm_upload_create) | **POST** /rpm/upload/ | 


## Documentation For Models

 - [Artifact](docs/Artifact.md)
 - [AsyncOperationResponse](docs/AsyncOperationResponse.md)
 - [Blob](docs/Blob.md)
 - [CertGuard](docs/CertGuard.md)
 - [Distribution](docs/Distribution.md)
 - [DockerDistribution](docs/DockerDistribution.md)
 - [DockerPublisher](docs/DockerPublisher.md)
 - [DockerRemote](docs/DockerRemote.md)
 - [FileContent](docs/FileContent.md)
 - [FilePublisher](docs/FilePublisher.md)
 - [FileRemote](docs/FileRemote.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Manifest](docs/Manifest.md)
 - [ManifestList](docs/ManifestList.md)
 - [ManifestListTag](docs/ManifestListTag.md)
 - [ManifestTag](docs/ManifestTag.md)
 - [Package](docs/Package.md)
 - [ProgressReport](docs/ProgressReport.md)
 - [Publication](docs/Publication.md)
 - [Repository](docs/Repository.md)
 - [RepositoryPublishURL](docs/RepositoryPublishURL.md)
 - [RepositorySyncURL](docs/RepositorySyncURL.md)
 - [RepositoryVersion](docs/RepositoryVersion.md)
 - [RepositoryVersionCreate](docs/RepositoryVersionCreate.md)
 - [RpmPublisher](docs/RpmPublisher.md)
 - [RpmRemote](docs/RpmRemote.md)
 - [Task](docs/Task.md)
 - [UpdateRecord](docs/UpdateRecord.md)
 - [Upload](docs/Upload.md)
 - [Worker](docs/Worker.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

Bruno Rocha - Pulp QE - @rochacbruno
