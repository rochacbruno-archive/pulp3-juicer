# DockerRemote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** | A unique name for this remote. | 
**url** | **str** | The URL of an external content source. | 
**validate** | **bool** | If True, the plugin will validate imported artifacts. | [optional] 
**ssl_ca_certificate** | **str** | A PEM encoded CA certificate used to validate the server certificate presented by the remote server. | [optional] 
**ssl_client_certificate** | **str** | A PEM encoded client certificate used for authentication. | [optional] 
**ssl_client_key** | **str** | A PEM encoded private key used for authentication. | [optional] 
**ssl_validation** | **bool** | If True, SSL peer validation must be performed. | [optional] 
**proxy_url** | **str** | The proxy URL. Format: scheme://user:password@host:port | [optional] 
**username** | **str** | The username to be used for authentication when syncing. | [optional] 
**password** | **str** | The password to be used for authentication when syncing. | [optional] 
**last_updated** | **datetime** | Timestamp of the most recent update of the remote. | [optional] 
**download_concurrency** | **int** | Total number of simultaneous connections. | [optional] 
**policy** | **str** | The policy to use when downloading content. The possible values include: &#39;immediate&#39;, &#39;on_demand&#39;, and &#39;cache_only&#39;. &#39;immediate&#39; is the default. | [optional] [default to 'immediate']
**upstream_name** | **str** | Name of the upstream repository | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


