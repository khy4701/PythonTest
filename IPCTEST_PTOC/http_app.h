#ifndef __HTTPF_APP_H__
#define __HTTPF_APP_H__

#define HTTPF_MSG_BUFSIZE                   	4096


#define MTYPE_CLIENT_MODE  500
#define MTYPE_SERVER_MODE  600
#include <stdint.h>

typedef long    genq_mtype_t;   // 2011.05.26
typedef struct general_qmsg{
        genq_mtype_t    mtype;
#define MAX_GEN_QMSG_LEN        (32768-sizeof(long))  
            char            body[MAX_GEN_QMSG_LEN];
} GeneralQMsgType;
#define GEN_QMSG_LEN(length)    (sizeof (genq_mtype_t) + length + 1)

typedef struct _http_info {
    /*added .2016.12.16 */
#if 0
    char    req_url[MAX_HTTP_REQUEST_URL_SIZE];
    char    ref_id[MAX_HTTP_USERNAME_SIZE];
    char    extern_id[MAX_HTTP_USERNAME_SIZE];
    char    scs_id[MAX_HTTP_USERNAME_SIZE];
#endif
#define MAX_IP_LEN  48
    char    nfvo_ip[MAX_IP_LEN];
    int     nfvo_port;
} http_info;


typedef struct _http_header {
    int         method;
    int         api_type;
    int         op_type;
    int         length;
    char        encoding;
} http_header;


#define HTTPF_RES_MSG_SIZE(datalen)     (sizeof(httpRes) - HTTPF_MSG_BUFSIZE + datalen)
typedef struct {
#define MTYPE_APP_TO_RESTIF_REQ                100
#define MTYPE_RESTIF_TO_APP_REQ                101
    long        mtype;
    int         tot_len;
    int         msgId;          /* httpf�󿡼� ����ϴ� fd table index */
    short       ehttpf_idx;     /* 2011.08.17: ehttpf_thread_index */
    uint32_t    tid;            /* transaction ID 2017.11.06 */
    int         srcQid;         /* slee Qid */
    char        srcSysId;       /* 1 ~ 8 */
    http_info   info;
    http_header http_hdr;       //http_hdr.length �� jsonBody�� ����
    char        jsonBody[HTTPF_MSG_BUFSIZE];
} httpReq;


typedef struct {
#define MTYPE_APP_TO_RESTIF_RES                102
#define MTYPE_RESTIF_TO_APP_RES                103
    long        mtype;
    int         tot_len;        // from msgId to end ~ 
    int         msgId;          /* httpf�󿡼� ����ϴ� fd table index */
    short       ehttpf_idx;     /* 2011.08.17: ehttpf_thread_index */
    uint32_t    tid;            /* transaction ID 2017.11.06 */
    int         srcQid;         /* slee Qid */
    char        srcSysId;       /* 1 ~ 8 */
    int         nResult;        /* 2011.09.11. int -> short */
    http_header http_hdr;       //http_hdr.length �� jsonBody�� ����
    char        jsonBody[HTTPF_MSG_BUFSIZE];
} httpRes;

#endif

