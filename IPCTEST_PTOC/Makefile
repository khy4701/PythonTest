#!/bin/sh

INCLUDES	= http_app.h

SRCS        = cclient.c
PROG1       = cclient

OBJS        = $(SRCS:.c=.o)

%.o : %.c
	$(CC) $(iNCLUDES) -c $<

$(PROG1): $(OBJS)
	$(CC) $(INCLUDES) -o cclient $(OBJS)

clean:
	/bin/rm -f *.o $(PROG1) core*

