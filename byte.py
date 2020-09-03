from ctypes import *
mylib = CDLL('/mnt/hgfs/qrcreate/libadd.so')
#https://www.yanxurui.cc/posts/python/2017-06-18-3-ways-of-calling-c-functions-from-python/
add = mylib.add
print add(1,2)