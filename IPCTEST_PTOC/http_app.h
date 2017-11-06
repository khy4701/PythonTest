#ifndef __HTTPF_APP_H__
#define __HTTPF_APP_H__

#define HTTPF_MSG_BUFSIZE                   	4096


#define MTYPE_CLIENT_MODE  500
#define MTYPE_SERVER_MODE  600


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
	int         msgId;          /* httpf상에서 사용하는 fd table index */
	short       ehttpf_idx;     /* 2011.08.17: ehttpf_thread_index */
	int         srcQid;         /* slee Qid */
	char        srcSysId;       /* 1 ~ 8 */
	http_header http_hdr;       //http_hdr.length 가 jsonBody의 길이
	char        jsonBody[HTTPF_MSG_BUFSIZE];
} httpReq;


typedef struct {
#define MTYPE_APP_TO_RESTIF_RES                102
#define MTYPE_RESTIF_TO_APP_RES                103
	long        mtype;
	int         tot_len;        // from msgId to end ~ 
	int         msgId;          /* httpf상에서 사용하는 fd table index */
	short       ehttpf_idx;     /* 2011.08.17: ehttpf_thread_index */
	int         srcQid;         /* slee Qid */
	char        srcSysId;       /* 1 ~ 8 */
	int         nResult;        /* 2011.09.11. int -> short */
	http_header http_hdr;       //http_hdr.length 가 jsonBody의 길이
	char        jsonBody[HTTPF_MSG_BUFSIZE];
} httpRes;

#endif

