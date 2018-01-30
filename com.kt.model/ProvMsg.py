
from _ctypes import Structure
from ctypes import c_int, c_ubyte, c_char, c_short, c_long, c_uint32
import ctypes

MAX_GEN_QMSG_LEN  = 32768 - ctypes.sizeof(ctypes.c_long)
HTTPF_MSG_BUFSIZE = 4096

#MTYPE_CLIENT_MODE = 500
#MTYPE_SERVER_MODE = 600

# SERVER MODE
# CLIENT MODE
MTYPE_NBRESTIF_TO_SLEE_REQ = 450
MTYPE_SLEE_TO_NBRESTIF_REQ = 451
MTYPE_NBRESTIF_TO_SLEE_RES = 452
MTYPE_SLEE_TO_NBRESTIF_RES = 453
MTYPE_SBRESTIF_TO_SLEE_REQ = 454
MTYPE_SLEE_TO_SBRESTIF_REQ = 455
MTYPE_SBRESTIF_TO_SLEE_RES = 456
MTYPE_SLEE_TO_SBRESTIF_RES = 457

class provMsg(Structure):
    
    _fields_ =  [("id", c_int),
         ("ce", c_char * 64),
         ("syms", c_int)]
        # ("ce", c_ubyte * 4),
      # ("syms", c_ubyte * 4)]

MAX_IP_LEN = 48
MAX_NS_INSTANCE_ID_LEN = 50
class HttpInfo(Structure):
    _fields_ = [("ns_instance_id", c_char * MAX_NS_INSTANCE_ID_LEN),
                ("nfvo_ip", c_char * MAX_IP_LEN ),
                ("nfvo_port", c_int)
            ]

# 4 * 5 = 20 (char -- 4bytes) 
class HttpHeader(Structure):
    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
    # But, this is not nessary under communication with C Messaage queue.
    #_pack_ = 1
    _fields_ = [("method", c_int),   # POST_METHOD_TYPE - ENUM
               ("api_type", c_int),  # 
               ("op_type", c_int),
               ("resource_type", c_int),
               ("length", c_int),
               ("encoding", c_char ) ]

# 1024 + 8 + 4*5 + 20 =  1072
class HttpReq(Structure):

    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
#    _pack_ = 1
    _fields_ = [("tot_len", c_int),      # 4
                ("msgId", c_int),        # 4
                ("ehttpf_idx", c_short), # 2
                ("tid", c_uint32),
                ("srcQid", c_int),       # 4     # REST Q ID
                ("srcSysId", c_char ),   # 1
                ("info", HttpInfo),
                ("http_hdr", HttpHeader),  # 17
                ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]  # 1024

class HttpRes(Structure):

    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
#    _pack_ = 1
    _fields_ = [("tot_len", c_int),      # 4
                ("msgId", c_int),        # 4
                ("ehttpf_idx", c_short), # 2
                ("tid", c_uint32),
                ("srcQid", c_int),       # 4
                ("srcSysId", c_char ),   # 1
                ("nResult", c_int),       # 4
                ("http_hdr", HttpHeader),  # 17
                ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]  # 1024
    
class GeneralQReqMsg(Structure):   
    MTYPE_APP_TO_RESTIF_REQ = 100   
    MTYPE_RESTIF_TO_APP_REQ = 101

    _fields_ = [("body", HttpReq)]
    
class GeneralQResMsg(Structure):   
    MTYPE_APP_TO_RESTIF_RES = 102
    MTYPE_RESTIF_TO_APP_RES = 103

    _fields_ = [("body", HttpRes)]    
