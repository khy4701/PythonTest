from __main__ import p
from _ctypes import Structure
from ctypes import c_int, c_ubyte
import ctypes


class Packet(Structure):
    _fields_ = [("id", c_int),
                ("ce", c_ubyte * 4),
                ("syms", c_ubyte * 4)]
#     
#     
#     # cast the struct to a pointer to a char array
# pdata = ctypes.cast(ctypes.byref(p), ctypes.POINTER(ctypes.c_char * ctypes.sizeof(p)))
# # now you can just save/send the struct data
# someSocketObject.send(pdata.contents.raw)
# 
# 
#  raw = someSocketObject.read(ctypes.sizeof(p2))
#  ctypes.memmove(ctypes.pointer(p2),raw,ctypes.sizeof(p2))