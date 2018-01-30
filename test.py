from _ctypes import Structure
from ctypes import c_long, c_uint32
import ctypes


#MAX_GEN_QMSG_LEN  = 32768 - SIZE(c_long)
print ctypes.sizeof(ctypes.c_uint32)
