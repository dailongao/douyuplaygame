import socket 
import thread
import threading
import time
import sys
import string
import re

# 
HOST='220.194.199.222'
PORT=27001
BUFSIZ=2048
ADDR=(HOST,PORT)
DEFAULT_ROOM=7

#
login_header = '\x00\x00\x00\x00\x00\x00\x00\x00\xb1\x02\x00\x00'
joingroup_header = "\x00\x00\x00\x00\x00\x00\x00\x00\xb1\x02\x00\x00"
keeplive_header = "\x00\x00\x00\x00\x00\x00\x00\x00\xb2\x02\x00\x00"

login_req = "type@=loginreq/username@=acfun_k66hppfz/password@=ee96f962b58e1574007a3af2d07195df/roomid@=%d/\x00"
joingroup_req = "type@=joingroup/rid@=%d/gid@=0/\x00"
keeplive_req = "type@=keeplive/tick@=23/\x00"

login = login_header + login_req
joingroup = joingroup_header + joingroup_req
keeplive = keeplive_header + keeplive_req

# -,-
TERMINATE = False

#
def set_len(str):
	dlen = len(str) - 4
	s = list(str)
	s[0] = chr(dlen)
	s[4] = chr(dlen)
	return ''.join(s)
#
def msg(str):
	return str[12:]

#
def recv_thread_func(hfunc,a2):
	while True:
		if TERMINATE:
			print 'recv thread terminate'
			return
		time.sleep(0.1)
		try:
			data = tcpCliSock.recv(BUFSIZ)
			str = msg(data)
			hfunc(str)
		except socket.timeout, e:
			err = e.args[0]
			if(err == 'timed out'):
				continue

#		
def keeplive_thread_func(a1,a2):
	data = set_len(keeplive)
	while True:
		if TERMINATE:
			print 'keeplive thread terminate'
			return
		time.sleep(5)
		tcpCliSock.send(data)
		
# 
def open_socket():
	global tcpCliSock
	tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	tcpCliSock.connect(ADDR)
	
#	
def close_socket():
	tcpCliSock.close()

#
def set_timeout():
	tcpCliSock.settimeout(1)

#
def dy_login(roomid):
	print '# Info : douyu.tv login'
	data = set_len(login % roomid)
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	print data

#
def dy_join_group(roomid):
	print '# Info : douyu.tv join group'
	data = set_len(joingroup % roomid)
	tcpCliSock.send(data)

#	
def start_chat(room_id, hfunc):
	print 'Kai Gao , Room ID :',room_id

	rt = threading.Thread(target=recv_thread_func, args=(hfunc,0))
	kt = threading.Thread(target=keeplive_thread_func, args=(0,0))
	
	open_socket()
	
	dy_login(room_id)
	dy_join_group(room_id)

	set_timeout()

	rt.start()
	kt.start()
	
	#
	while True:
		str = raw_input("Press q to exit")
		if str == 'q':
			break

	global TERMINATE
	TERMINATE = True

	try:
		kt.join();
	except e:
		print e

	try:
		rt.join();
	except e:
		print e

	close_socket()
	

def print_message(data):
	checkPattern = re.compile(r'content@=(.*)/scope@=/snick@=(.*)/dnick@=')
	cr = checkPattern.search(data).groups()

	print cr
	#print cr[1].decode('utf-8'), ':', cr[0].decode('utf-8')
	

if __name__ == '__main__':
	start_chat(DEFAULT_ROOM, print_message)

