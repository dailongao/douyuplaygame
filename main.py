# -*- coding: utf-8 -*-  

import chat
import control
import parse
import time
import sys

# the max length of danmu on douyu.tv is 20..
MAX_MSG_LEN = 20
DEFAULT_CHAT_ROOM = 6032
NO_EXEC = False

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

def check_command(umsg):
	# check string message
	if umsg in command_map:
		return True
	# check message length
	if len(umsg) > MAX_MSG_LEN:
		return False;
	# check single-char message
	for c in umsg:
		if c not in command_map:
			return False
	return True

def print_log(uname,ucmd,cnt,ftime):
	if ftime:
		print "#", time.strftime('%H:%M:%S')
	print uname.decode('utf-8'), ':', ucmd,cnt

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
	control.control_init()
	chat.start_chat(DEFAULT_CHAT_ROOM, new_query)
