import socket 
import thread
import time

HOST='220.194.199.222'
PORT=27001
BUFSIZ=2048
ADDR=(HOST,PORT)

login="\x66\x00\x00\x00\x66\x00\x00\x00\xb1\x02\x00\x00type@=loginreq/username@=acfun_k66hppfz/password@=ee96f962b58e1574007a3af2d07195df/roomid@=8/\x00"
joingroup="\x27\x00\x00\x00\x27\x00\x00\x00\xb1\x02\x00\x00type@=joingroup/rid@=8/gid@=0/\x00"
keeplive="\x21\x00\x00\x00\x21\x00\x00\x00\xb2\x02\x00\x00type@=keeplive/tick@=41/\x00"

# 
tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

# login
tcpCliSock.send(login)
data=tcpCliSock.recv(BUFSIZ)
print(data)

# join group
tcpCliSock.send(joingroup)
data=tcpCliSock.recv(BUFSIZ)
print(data)

# loop : keep live & get data
while True:
	time.sleep(1)
	tcpCliSock.send(keeplive)

	data=tcpCliSock.recv(BUFSIZ)
	print(data)

tcpCliSock.close()
