# Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**created** | **datetime** | Timestamp of creation. | [optional] 
**job_id** | **str** | ID of the job in rq. | [optional] 
**state** | **str** | The current state of the task. The possible values include: &#39;waiting&#39;, &#39;skipped&#39;, &#39;running&#39;, &#39;completed&#39;, &#39;failed&#39; and &#39;canceled&#39;. | [optional] 
**name** | **str** | The name of task. | 
**started_at** | **datetime** | Timestamp of the when this task started execution. | [optional] 
**finished_at** | **datetime** | Timestamp of the when this task stopped execution. | [optional] 
**non_fatal_errors** | **str** | A JSON Object of non-fatal errors encountered during the execution of this task. | [optional] 
**error** | **str** | A JSON Object of a fatal error encountered during the execution of this task. | [optional] 
**worker** | **str** | The worker associated with this task. This field is empty if a worker is not yet assigned. | [optional] 
**parent** | **str** | The parent task that spawned this task. | [optional] 
**spawned_tasks** | **list[str]** | Any tasks spawned by this task. | [optional] 
**progress_reports** | [**list[ProgressReport]**](ProgressReport.md) |  | [optional] 
**created_resources** | **list[str]** | Resources created by this task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


