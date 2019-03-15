# Package

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**href** | **str** |  | [optional] 
**artifact** | **str** | Artifact file representing the physical content | 
**name** | **str** | Name of the package | 
**epoch** | **str** | The package&#39;s epoch | [optional] 
**version** | **str** | The version of the package. For example, &#39;2.8.0&#39; | 
**release** | **str** | The release of a particular version of the package. e.g. &#39;1.el7&#39; or &#39;3.f24&#39; | 
**arch** | **str** | The target architecture for a package.For example, &#39;x86_64&#39;, &#39;i686&#39;, or &#39;noarch&#39; | 
**pkg_id** | **str** | Checksum of the package file | 
**checksum_type** | **str** | Type of checksum, e.g. &#39;sha256&#39;, &#39;md5&#39; | 
**summary** | **str** | Short description of the packaged software | [optional] 
**description** | **str** | In-depth description of the packaged software | [optional] 
**url** | **str** | URL with more information about the packaged software | [optional] 
**changelogs** | **str** | Changelogs that package contains | [optional] [default to '[]']
**files** | **str** | Files that package contains | [optional] [default to '[]']
**requires** | **str** | Capabilities the package requires | [optional] [default to '[]']
**provides** | **str** | Capabilities the package provides | [optional] [default to '[]']
**conflicts** | **str** | Capabilities the package conflicts | [optional] [default to '[]']
**obsoletes** | **str** | Capabilities the package obsoletes | [optional] [default to '[]']
**suggests** | **str** | Capabilities the package suggests | [optional] [default to '[]']
**enhances** | **str** | Capabilities the package enhances | [optional] [default to '[]']
**recommends** | **str** | Capabilities the package recommends | [optional] [default to '[]']
**supplements** | **str** | Capabilities the package supplements | [optional] [default to '[]']
**location_base** | **str** | Base location of this package | [optional] 
**location_href** | **str** | Relative location of package to the repodata | 
**rpm_buildhost** | **str** | Hostname of the system that built the package | [optional] 
**rpm_group** | **str** | RPM group (See: http://fedoraproject.org/wiki/RPMGroups) | [optional] 
**rpm_license** | **str** | License term applicable to the package software (GPLv2, etc.) | [optional] 
**rpm_packager** | **str** | Person or persons responsible for creating the package | [optional] 
**rpm_sourcerpm** | **str** | Name of the source package (srpm) the package was built from | [optional] 
**rpm_vendor** | **str** | Name of the organization that produced the package | [optional] 
**rpm_header_start** | **int** | First byte of the header | 
**rpm_header_end** | **int** | Last byte of the header | 
**size_archive** | **int** | Size, in bytes, of the archive portion of the original package file | 
**size_installed** | **int** | Total size, in bytes, of every file installed by this package | 
**size_package** | **int** | Size, in bytes, of the package | 
**time_build** | **int** | Time the package was built in seconds since the epoch | 
**time_file** | **int** | The &#39;file&#39; time attribute in the primary XML - file mtime in seconds since the epoch. | 
**relative_path** | **str** | File name of the package | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


