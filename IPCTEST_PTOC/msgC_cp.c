#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/msg.h>
#include <assert.h>
#include <string.h>
#include <errno.h>

#define MAXSIZE 512

int QueueKey = 12345;

typedef struct msgbuf {
    long mtype;       /* message type, must be > 0 */
//    char mtext[MAXSIZE];    /* message data */
    int id ;    /* message data */
    int ce;    /* message data */
    int syms;
}QUEUE;

int main(){

    QUEUE queBuf;
//    char message[MAXSIZE];
    int qid = msgget(QueueKey, IPC_CREAT | 0777);

    assert(qid != -1);

    memset(&queBuf, 0x00, sizeof(QUEUE));

    while( 1 )
    {
        if ( -1 == msgrcv( qid, (QUEUE *)&queBuf, sizeof(QUEUE), 0, 0))
        {
            perror( "msgrcv()" );
            exit( 1);
        }
//        printf("Message Recv Success : %s \n", queBuf.mtext);
        printf("ID : %d \n", queBuf.id);
        printf("CE : %d \n", queBuf.ce);
        printf("SYMS : %d\n", queBuf.syms);

        queBuf.id = 444;
        queBuf.ce = 555;
        queBuf.syms = 666;

        int ret = msgsnd(qid, &queBuf, sizeof(QUEUE)-1, 0);
        printf(" RET [%d] %d\n", ret, errno);
        sleep(1);
    }

    return -1;
}
