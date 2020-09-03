from ctypes import *
mylib = CDLL('/mnt/hgfs/qrcreate/libadd.so')

add = mylib.add
print add(1,2)