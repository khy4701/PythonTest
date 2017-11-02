
from _ctypes import Structure
from ctypes import c_int, c_ubyte, c_char, c_short, c_long

HTTPF_MSG_BUFSIZE = 1024

MTYPE_CLIENT_MODE = 500
MTYPE_SERVER_MODE = 600

class provMsg(Structure):
    
    _fields_ =  [("id", c_int),
         ("ce", c_char * 64),
         ("syms", c_int)]
        # ("ce", c_ubyte * 4),
                  # ("syms", c_ubyte * 4)]



# 4 * 5 = 20 (char -- 4bytes) 
class HttpHeader(Structure):
    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
    # But, this is not nessary under communication with C Messaage queue.
    #_pack_ = 1
    _fields_ = [("method", c_int),
               ("api_type", c_int),
               ("op_type", c_int),
               ("length", c_int),
               ("encoding", c_char ) ]

# 1024 + 8 + 4*5 + 20 =  1072
class HttpReq(Structure):

    MTYPE_APP_TO_RESTIF_REQ = 100   
    MTYPE_RESTIF_TO_APP_REQ = 101
    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
#    _pack_ = 1
    _fields_ = [("tot_len", c_int),      # 4
                ("msgId", c_int),        # 4
                ("ehttpf_idx", c_short), # 2
                ("srcQid", c_int),       # 4
                ("srcSysId", c_char ),   # 1
                ("http_hdr", HttpHeader),  # 17
                ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]  # 1024


class HttpRes(Structure):

    MTYPE_APP_TO_RESTIF_RES = 102
    MTYPE_RESTIF_TO_APP_RES = 103
    # Serialization ( if don't put this field, it'll calculate 4 byte each other )
#    _pack_ = 1
    _fields_ = [("tot_len", c_int),      # 4
                ("msgId", c_int),        # 4
                ("ehttpf_idx", c_short), # 2
                ("srcQid", c_int),       # 4
                ("srcSysId", c_char ),   # 1
                ("nResult", c_int),       # 4
                ("http_hdr", HttpHeader),  # 17
                ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]  # 1024

