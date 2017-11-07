class ApiDefine():

    API_NUM1 = "departmentAPI"
    
    NSD_ON_BOARDING = "nsd-on-boarding"
    NS_ID_CREATE = "ns-identifier-create"
    NS_INSTANTIATION = "ns-instantiation"
    NS_TERMINATION   = "ns-termination"
    NS_SCALE        = "ns-scale"
    CREATE_PM_JOB = "crt-pm-job"
    QUERY_PM_JOB = "query-pm-job"
    
    NOTI_OF_LCM  = "noti-of-lcm"



# httpReq.http_hdr.encoding
class ContentEncoding():
    PLAIN   = 0x00,
    DEFLATE = 0x01,
    GZIP    = 0x02

# httpReq.http_hdr.api_type
class ApiType():
    NSD_API_TYPE = 1,
    NSLCM_API_TYPE = 2,
    NSPM_API_TYPE = 3,
    NSFM_API_TYPE = 4,
    VNFPKGM_API_TYPE = 5,
    UNKNOWN_API_TYPE = 6


# httpReq.http_hdr.method
class MethodType():
    
    POST_METHOD_TYPE = 1,
    GET_METHOD_TYPE = 2,
    PUT_METHOD_TYPE = 3,
    PATCH_METHOD_TYPE = 4,
    DELETE_METHOD_TYPE = 5,
    UNKNOWN_METHOD_TYPE = 6
    
# httpReq.http_hdr.op_type
class OPType():
    Create_NSD_Info_OP_TYPE = 1,
    Upload_NSD_OP_TYPE = 2,
    Fetch_NSD_OP_TYPE = 3,
    Update_NSD_Info_OP_TYPE = 4,
    Delete_NSD_OP_TYPE = 5,
    Query_NSD_Info_OP_TYPE = 6,
    Onboard_PNFD_OP_TYPE = 7,
    Update_PNFD_OP_TYPE = 8,
    Delete_PNFD_OP_TYPE = 9,
    Query_PNFD_OP_TYPE = 10,
    Subscribe_OP_TYPE = 11, # also use for NSLCM, NSPM, NSFM, NSPKGM
    Terminate_Subscription_OP_TYPE = 12,
    Query_Subscription_Information_OP_TYPE = 13,
    Notify_OP_TYPE = 14, # also use for NSLCM, NSPM, NSFM, NSPKGM

    # invoke NS lifecycle management operations of NS instances towards the NFVO, 
    # and subscribe to notifications regarding NS lifecycle changes provided by the NFVO. 
    Create_NS_Identifier_OP_TYPE = 15,
    Instantiate_NS_OP_TYPE = 16,
    Scale_NS_OP_TYPE = 17,
    Update_NS_OP_TYPE = 18,
    Query_NS_OP_TYPE = 19,
    Terminate_NS_OP_TYPE = 20,
    Delete_NS_Identifier_OP_TYPE = 21,
    Heal_NS_OP_TYPE = 22,
    Get_Operation_Status_OP_TYPE = 23,

    # providing performance management (measurement results collection and notifications) related to NSs.
    Create_PM_Job_OP_TYPE = 24,
    Query_PM_Job_OP_TYPE = 25,
    Delete_PM_Job_OP_TYPE = 26,
    Create_Threshold_OP_TYPE = 27,
    Query_Threshold_OP_TYPE = 28,
    Delete_Threshold_OP_TYPE = 29,

    # subscribe to notifications regarding NS alarms provided by the NFVO.
    Get_Alarm_List_OP_TYPE = 30,
    Acknowledge_Alarm_OP_TYPE = 31,

    # invoke VNF package management operations towards the NFVO, 
    # and subscribe to notifications regarding VNF package on-boarding or changes provided by the NFVO.
    Onboard_VNF_Package_OP_TYPE = 32,
    Enable_VNF_Package_OP_TYPE = 33,
    Disable_VNF_Package_OP_TYPE = 34,
    Delete_VNF_Package_OP_TYPE = 35,
    Abort_VNF_Package_Deletion_OP_TYPE = 36,
    Query_Onboarded_VNF_Package_OP_TYPE = 37,    # , include obtaining the VNFD
    Fetch_Onboarded_VNF_Package_OP_TYPE = 38,
    Fetch_Onboarded_VNF_Package_Artifacts_OP_TYPE = 39
    
    
class ResourceType():
    # defines all the resource for provided by the NSD management interface.
    NSD_NS_DESCRIPTORS = 1,
    NSD_INDIVIDUAL_NS_DESCRIPTOR = 2,
    NSD_NSD_CONTENT = 3,
    NSD_PNF_DESCRIPTORS = 4,
    NSD_INDIVIDUAL_PNF_DESCRIPTORS = 5,
    NSD_PNFD_CONTENT = 6,
    NSD_SUBSCRIPTIONS = 7,
    NSD_INDIVIDUAL_SUBSCRIPTION = 8,
    NSD_NOTIFICATION_ENDPOINT = 9,


    #defines all the resources provided by the NS lifecycle management interface.
    NSLCM_NS_INSTANCES = 10,
    NSLCM_INDIVIDUAL_NS_INSTANCE = 11,
    NSLCM_INSTANTIATE_NS_TASK = 12,
    NSLCM_SCALE_NS_TASK = 13,
    NSLCM_UPDATE_NS_TASK = 14,
    NSLCM_HEAL_NS_TASK = 15,
    NSLCM_TERMINATE_NS_TASK = 16,
    NSLCM_NS_LCM_OCCURRENCES = 17,
    NSLCM_INDIVIDUAL_NS_LCM_OCCURRENCE = 18,
    NSLCM_RETRY_OPERATION_TASK = 19,
    NSLCM_ROLLBACK_OPERATION_TASK = 20,
    NSLCM_FAIL_OPERATION_TASK = 21,
    NSLCM_CANCEL_OPERATION_TASK = 22,
    NSLCM_SUBSCRIPTIONS = 23,
    NSLCM_INDIVIDUAL_SUBSCRIPTION = 24,
    NSLCM_NOTIFICATION_ENDPOINT = 25,

    # defines all the resources provided by the performance management API.
    NSPM_PM_JOBS = 26,
    NSPM_INDIVIDUAL_PM_JOB = 27,
    NSPM_INDIVIDUAL_PERFORMANCE_REPORT = 28,
    NSPM_THRESHOLDS = 29,
    NSPM_INDIVIDUAL_THRESHOLD = 30,
    NSPM_SUBSCRIPTIONS = 31,
    NSPM_INDIVIDUAL_SUBSCRIPTION = 32,
    NSPM_NOTIFICATION_ENDPOINT = 33,

    # defines all the resources provided by the NS fault management interface.
    NSFM_ALARMS = 34,
    NSFM_INDIVIDUAL_ALARM = 35,
    NSFM_SUBSCRIPTIONS = 36,
    NSFM_INDIVIDUAL_SUBSCRIPTION = 37,
    NSFM_NOTIFICATION_ENDPOINT = 38,

    # defines all the resources provided by the VNF package management interface.
    VNFPKGM_VNF_PACKAGES = 39,
    VNFPKGM_INDIVIDUAL_ONBOARDED_VNF_PACKAGE = 40,
    VNFPKGM_VNFD_IN_AN_INDIVIDUAL_ONBOARDED_VNF_PACKAGE = 50,
    VNFPKGM_ONBOARDED_VNF_PACKAGE_CONTENT = 51,
    VNFPKGM_INDIVIDUAL_ONBOARDED_VNF_PACKAGE_ARTIFACT = 52,
    VNFPKGM_SUBSCRIPTIONS = 53,
    VNFPKGM_INDIVIDUAL_SUBSCRIPTION = 54,
    VNFPKGM_NOTIFICATION_ENDPOINT = 55

    