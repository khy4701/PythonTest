#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/msg.h>
#include <assert.h>
#include <string.h>
#include <errno.h>
#include <time.h>
#include "http_app.h"
//#include <pthread.h>
//
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

int QueueKey = 12345;
int RestKey = 54322;

//pthread_t threads[5];

//void *thread_main(void *);

int main(){

//	QUEUE 	queBuf;
    GeneralQMsgType genQMsg;
	httpReq *reqMsg;
	httpRes *resMsg;
	http_header *header;

//	pthread_t tid;
	int seqNum = 0, msgId;
	
	int myQid, restQid;
  
    struct msqid_ds qDs;

//    qDs.msg_perm = Vd 
//    qDs.msg_qbytes = 4096;

	myQid	= msgget(QueueKey, IPC_CREAT | 0777 );
	restQid = msgget(RestKey, IPC_CREAT | 0777);

//    msgctl(myQid, IPC_SET, &qDs);

//	memset(&queBuf, 0x00, sizeof(QUEUE));
//	memset( resMsg, 0x00, sizeof(httpRes));
    memset( &genQMsg, 0x00, sizeof(GeneralQMsgType));

	assert(myQid != -1);

	while( 1 )
	{
		//if ( -1 == msgrcv( myQid, (QUEUE *)&queBuf, sizeof(QUEUE), 0, 0))

		//if ( -1 == msgrcv( myQid, (httpReq *)&reqMsg, sizeof(httpReq), 0, 0))
		if ( -1 == msgrcv( myQid, (GeneralQMsgType *)&genQMsg, sizeof(GeneralQMsgType), 0, 0))
		{
			perror( "msgrcv()" );
			exit( 1);
		}
		printf("Message Recv Success \n");

        reqMsg = (httpReq *)genQMsg.body;

		header = &reqMsg->http_hdr;

		printf("HEADER=========================\n");
		printf("method: %d\n", header->method);
		printf("api_type : %d\n", header->api_type);
		printf("op_type : %d\n", header->op_type);
		printf("length : %d\n", header->length);
		printf("encoding : %c\n", header->encoding);
		printf("BODY===========================\n");
		printf("Qtype : %d\n", genQMsg.mtype);
		printf("mtype : %d\n", reqMsg->mtype);
		printf("tot_len : %d\n", reqMsg->tot_len);
		printf("msgId : %d\n", reqMsg->msgId);
		printf("ehttpf_idx : %d\n", reqMsg->ehttpf_idx);
		printf("tid : %d\n", reqMsg->tid);
		printf("srcQid : %d\n", reqMsg->srcQid);
		printf("srcSysId : %d\n", reqMsg->srcSysId);
		printf("jsonBody : %s\n", reqMsg->jsonBody);
		printf("===============================\n");

		//sprintf( queBuf.body, "%s" , "12345678901234567890");

        memset(&genQMsg, 0x00, sizeof(GeneralQMsgType));

		genQMsg.mtype = MTYPE_SERVER_MODE;

        resMsg= (httpRes *)genQMsg.body;

		resMsg->mtype = 10;
		memcpy(&resMsg->http_hdr, &reqMsg->http_hdr, sizeof(http_header));

		resMsg->tot_len = reqMsg->tot_len;
		resMsg->msgId = reqMsg->msgId;
		resMsg->tid = reqMsg->tid;
		resMsg->ehttpf_idx = reqMsg->ehttpf_idx;
		resMsg->srcQid = reqMsg->srcQid;
		resMsg->srcSysId = reqMsg->srcSysId;
		resMsg->nResult = 200;

		strcpy(resMsg->jsonBody,reqMsg->jsonBody);


        httpRes *tBody = (httpRes *) genQMsg.body;
        printf("genQMsg,body, jsonBody [%s]\n", tBody->jsonBody);
        printf("genQMsg Type, jsonBody [%d]\n", genQMsg.mtype);
        printf("genQMsg Type, jsonBody [%d]\n", tBody->mtype);
        printf("genQMsg Type, jsonBody [%d]\n", tBody->http_hdr.method);

        int ret = msgsnd(restQid, (void *)&genQMsg, sizeof(GeneralQMsgType) , 1);
        printf(" RET [%d] %d\n", ret, errno);
        sleep(1);

    }

}

