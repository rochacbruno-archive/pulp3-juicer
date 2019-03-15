# ProgressReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message shown to the user for the progress report. | [optional] 
**state** | **str** | The current state of the progress report. The possible values are: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39; and &#39;canceled&#39;. The default is &#39;waiting&#39;. | [optional] 
**total** | **int** | The total count of items to be handled by the ProgressBar. | [optional] 
**done** | **int** | The count of items already processed. Defaults to 0. | [optional] 
**suffix** | **str** | The suffix to be shown with the progress report. | [optional] 
**task** | **str** | The task associated with this progress report. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


