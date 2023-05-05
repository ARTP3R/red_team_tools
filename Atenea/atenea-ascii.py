#!/usr/bin/env python3

import hashlib

msg = ''
text = '080 097 115 115 119 111 114 100 032 112 097 114 097 032 115 117 112 101 114 097 114 032 101 108 032 114 101 116 111 058 032 084 104 101 065 083 067 073 073 084 097 098 108 101 033'
for i in text.split(' '):
    msg += chr(int(i))
    
print (msg)

result = hashlib.md5(msg.encode())

print ("flag{", result, "}")
