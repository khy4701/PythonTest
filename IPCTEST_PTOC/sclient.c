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

#define MAXSIZE 1100

int QueueKey = 12345;
int RestKey = 54323;

//pthread_t threads[5];

//void *thread_main(void *);

int main(){

//	QUEUE 	queBuf;
//

    GeneralQMsgType genQReqMsg;
    GeneralQMsgType genQResMsg;
	httpReq *reqMsg;
	httpRes *resMsg;
	http_header *header;
    http_info  *info;

//	pthread_t tid;
	int seqNum = 0, msgId;
	
	int myQid, restQid;

	myQid	= msgget(QueueKey, IPC_CREAT | 0777 );
	restQid = msgget(RestKey, IPC_CREAT | 0777);

	//	memset(&queBuf, 0x00, sizeof(QUEUE));
	memset(&genQReqMsg, 0x00, sizeof(GeneralQMsgType));
	memset(&genQResMsg, 0x00, sizeof(GeneralQMsgType));

	assert(myQid != -1);
	assert(restQid != -1);

    genQReqMsg.mtype = MTYPE_CLIENT_MODE;
    reqMsg= (httpReq *)genQReqMsg.body;
	reqMsg->mtype = MTYPE_CLIENT_MODE;

	reqMsg->tot_len = 100;
	reqMsg->msgId = 200;
	reqMsg->tid = 999;
	reqMsg->ehttpf_idx = 300 ;
	reqMsg->srcQid = 400;
	reqMsg->srcSysId = '5';

    info = &reqMsg->info;
    sprintf(info->nfvo_ip, "%s", "None");
    info->nfvo_port = 5000;

	header = &reqMsg->http_hdr;
	header->method = 1;
	header->api_type = 2;
	header->op_type =3;
	header->length = 4;
	header->encoding = '5';

	sprintf(reqMsg->jsonBody, "%s", "{\"name\":\"Hoyoung\", \"age\": 123 }");

	int ret = msgsnd(restQid, (void *)&genQReqMsg, sizeof(GeneralQMsgType), 1);
	printf(" RET [%d] %d\n", ret, errno);

	assert(ret != -1);

	//if ( -1 == msgrcv( myQid, (QUEUE *)&queBuf, sizeof(QUEUE), 0, 0))
	if ( -1 == msgrcv( myQid, (httpRes *)&genQResMsg, sizeof(GeneralQMsgType), 0, 0))
	{
		perror( "msgrcv()" );
		exit( 1);
	}
	printf("Message Recv Success \n");

    resMsg = (httpRes *)genQResMsg.body;
	header = &resMsg->http_hdr;

	printf("HEADER=========================\n");
	printf("method: %d\n", header->method);
	printf("api_type : %d\n", header->api_type);
	printf("op_type : %d\n", header->op_type);
	printf("length : %d\n", header->length);
	printf("encoding : %c\n", header->encoding);
	printf("BODY===========================\n");
	printf("mtype : %d\n", resMsg->mtype);
	printf("tot_len : %d\n", resMsg->tot_len);
	printf("msgId : %d\n", resMsg->msgId);
	printf("ehttpf_idx : %d\n", resMsg->ehttpf_idx);
	printf("srcQid : %d\n", resMsg->srcQid);
	printf("srcSysId : %c\n", resMsg->srcSysId);
	printf("response : %d\n", resMsg->nResult);
	printf("jsonBody : %s\n", resMsg->jsonBody);
	printf("===============================\n");

	//sprintf( queBuf.body, "%s" , "12345678901234567890");



	sleep(1);

	return -1;

}

//void *myThreadFun(void *vargp)
//{
//	sleep(1);
//	printf("Printing GeeksQuiz from Thread \n");
//	return NULL;
//
//}




