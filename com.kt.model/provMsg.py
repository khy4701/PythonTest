
from _ctypes import Structure
from ctypes import c_int, c_ubyte, c_char, c_short

HTTPF_MSG_BUFSIZE = 1024

class provMsg(Structure):
    
    _fields_ =  [("id", c_int),
         ("ce", c_char * 64),
         ("syms", c_int)]
        # ("ce", c_ubyte * 4),
                  # ("syms", c_ubyte * 4)]



class HttpHeader(Structure):
    _fields = [("method", c_int),
               ("api_type", c_int),
               ("op_type", c_int),
               ("length", c_int),
               ("encoding", c_char ) ]


class HttpReq(Structure):
    _fields = [("tot_len", c_int),
               ("msgId", c_int),
               ("ehttpf_idx", c_short),
               ("srcQid", c_int),
               ("srcSysId", c_char ),
               ("http_hdr", HttpHeader),
               ("jsonBody", c_char * HTTPF_MSG_BUFSIZE ) ]
    
    