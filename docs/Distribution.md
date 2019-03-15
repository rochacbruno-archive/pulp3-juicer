# Distribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**name** | **str** | A unique distribution name. Ex, &#x60;rawhide&#x60; and &#x60;stable&#x60;. | 
**publisher** | **str** | Publications created by this publisher and repository are automaticallyserved as defined by this distribution | [optional] 
**publication** | **str** | The publication being served as defined by this distribution | [optional] 
**repository** | **str** | Publications created by this repository and publisher are automaticallyserved as defined by this distribution | [optional] 
**content_guard** | **str** | An optional content-guard. | [optional] 
**remote** | **str** | Remote that can be used to fetch content when using pull-through caching. | [optional] 
**base_path** | **str** | The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \&quot;foo\&quot; and \&quot;foo/bar\&quot;) | 
**base_url** | **str** | The URL for accessing the publication as defined by this distribution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


