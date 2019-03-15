# Manifest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**type** | **str** |  | [optional] 
**artifact** | **str** | Artifact file representing the physical content | 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 
**digest** | **str** | sha256 of the Manifest file | 
**schema_version** | **int** | Docker schema version | 
**media_type** | **str** | Docker media type of the file | 
**blobs** | **list[str]** | Blobs that are referenced by this Manifest | 
**config_blob** | **str** | Blob that contains configuration for this Manifest | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


