# -*- coding: utf-8 -*-  

import chat
import control
import parse
import time
import sys

# the max length of danmu on douyu.tv is 20..
MAX_MSG_LEN = 16
DEFAULT_CHAT_ROOM = 6032
NO_EXEC = False
START_TIME_LIMIT = 30

command_map = {
	'U' : 'w',
	'D' : 's',
	'L' : 'a',
	'R' : 'd',
	'A' : 'z',
	'B' : 'e',
	'START' : 'c',
	'SELECT' : 'v'
}

#
class User:
	def __init__(self,name):
		self.name = name
		self.last_start_time = time.time() - 64
		self.last_cmd_time = time.time() - 64

	def check_start(self):
		if time.time() - self.last_start_time < START_TIME_LIMIT:
			print 
			return False

	def run(self,cmd):
		self.last_cmd_time = time.time()
		if cmd == 'START' and check_start():
			self.last_start_time = time.time()
		else:
			run_command(self.name,cmd)

#
users = {}

#
def print_strings(*strs):
	for s in strs:
		try:
			print s.decode('utf-8'),
		except:
			print "!@#$%^&*",
	print ''

def get_user(uname):
	if uname not in users:
		users[uname] = User
	return users[uname]

def check_command(umsg):
	# check string message
	if umsg in command_map:
		return True
	
	# check single-char message
	for c in umsg:
		if c not in command_map:
			return False

	# check message length
	if len(umsg) > MAX_MSG_LEN:
		print '指令长度限制为'.decode('utf-8'), MAX_MSG_LEN
		return False;

	return True

def print_log(uname,ucmd,cnt,ftime):
	if ftime:
		print "#", time.strftime('%H:%M:%S')
	try:
		print uname.decode('utf-8'), ':', ucmd, cnt
	except:
		print "!@#$%^&*", ':', ucmd, cnt

def do_send_key(cmd):
	if not NO_EXEC:
		control.sendkey(cmd)

def run_command(uname,ucmd):
	if ucmd in command_map:
		do_send_key(command_map[ucmd])
		print_log(uname,ucmd,1,True)
		return

	cnt = 0
	for c in ucmd:
		cnt = cnt + 1
		do_send_key(command_map[c])
		print_log(uname,c,cnt,cnt==1)

def new_query(raw_msg):
	try:
		# 
		msg = parse.getinfo(raw_msg)
		cmd_str = msg[0]
		user_name = msg[1]

		#
		if not check_command(cmd_str):
			return

		#
		run_command(user_name,cmd_str)
		
	except:
		print sys.exc_info()[0]
		print sys.exc_info()[1]
		return

#
if __name__ == '__main__':
	control.control_init('空之轨迹 ＦＣ')
	tstr = raw_input('hehe')
	#chat.start_chat(DEFAULT_CHAT_ROOM, new_query)
