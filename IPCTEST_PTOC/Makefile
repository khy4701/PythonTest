#!/bin/sh

INCLUDES	= http_app.h

SRCS        = msgC.c
PROG1       = msgC

OBJS        = $(SRCS:.c=.o)

%.o : %.c
	$(CC) $(iNCLUDES) -c $<

$(PROG1): $(OBJS)
	$(CC) $(INCLUDES) -o msgC $(OBJS)

clean:
	/bin/rm -f *.o $(PROG1) core*

