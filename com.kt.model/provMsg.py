
from _ctypes import Structure
from ctypes import c_int, c_ubyte, c_char

class provMsg(Structure):
        _fields_ =  [("id", c_int),
         ("ce", c_char * 64),
         ("syms", c_int)]
        # ("ce", c_ubyte * 4),
                  # ("syms", c_ubyte * 4)]



