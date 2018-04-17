#-*- encoding:gb2312 -*-
import hashlib

a = "123456"
print (hashlib.md5(a.encode()).hexdigest())
print (hashlib.sha1(a.encode()).hexdigest())
print (hashlib.sha224(a.encode()).hexdigest())
print (hashlib.sha256(a.encode()).hexdigest())
print (hashlib.sha384(a.encode()).hexdigest())
print (hashlib.sha512(a.encode()))