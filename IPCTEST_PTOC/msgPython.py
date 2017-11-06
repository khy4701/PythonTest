import sysv_ipc
from _ctypes import Structure
from ctypes import c_int, c_ubyte, c_char
import ctypes, time

QueueKey=12345

class testFunc:
    def __init__(self, header, body):
        self.header = header
        self.body   = body
        pass

    def getter(self):
        return (self.header,self.body)
    

class Packet(Structure):
    _fields_ = [("id", c_int),
            ("ce", c_char * 64),
            ("syms", c_int)]
           # ("ce", c_ubyte * 4),
           # ("syms", c_ubyte * 4)]

if __name__ == '__main__' :

#    func = testFunc('Header Info', 'Body Info')
#    print( func.getter() )

    p = Packet()
    p.id = 555
    p.ce = "Hello1111111111111111111111111111111111222222222222222222222222"
    p.syms = 3

    # cast the struct to a pointer to a char array
    #pdata = ctypes.cast(ctypes.byref(p), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(p)))
    
    # now you can just save/send the struct data
    #someSocketObject.send(pdata.contents.raw)    

    try:
#        mq = sysv_ipc.MessageQueue(QueueKey, sysv_ipc.IPC_CREX)
        mq = sysv_ipc.MessageQueue(QueueKey, sysv_ipc.IPC_CREAT, mode= 0777, max_message_size = 32)

        #s = func.decode()
        #mq.send(s, True)
#        mq.send(pdata.contents.raw ,True)

        p2 = Packet()

        while True:
#            (message, mtype) = mq.receive(ctypes.sizeof(p2))
            (message, mtype) = mq.receive(10)
        
            mydata = ctypes.create_string_buffer( message )

            print (mydata)
#            print (message)

            #raw = someSocketObject.read(ctypes.sizeof(p2))
#            ctypes.memmove(ctypes.pointer(p2), mydata ,ctypes.sizeof(p2))

#            print (p2.id , p2.ce, p2.syms )
            
            time.sleep(1)

    except sysv_ipc.ExistentialError:
        print "ERROR: message queue creation failed"

    except Exception as e :
        print e
