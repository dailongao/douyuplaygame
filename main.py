# -*- coding: utf-8 -*-  

import chat
import control
import parse
import time
import sys

# the max length of danmu on douyu.tv is 20..
DEFAULT_CHAT_ROOM = 6032
NO_EXEC = False

command_map = {

	#
	'8' : 'UPARROW',
	'2' : 'DOWNARROW',
	'4' : 'LEFTARROW',
	'6' : 'RIGHTARROW',

	#
	'SPACE' : 'SPACE',
	'CTRL' : 'LEFTCTRL',
	'SHIFT' : 'LEFTSHIFT',

	#
	'Z' : 'Z',
	'A' : 'A',
	'B' : 'B',
	'M' : 'M',
	'X' : 'X',
	'C' : 'C',
	'V' : 'V'
}

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
	#control.control_init('搶曽怱鉟極')
	while True:
		control.sendkey('Z')
		time.sleep(1)

	#chat.start_chat(DEFAULT_CHAT_ROOM, new_query)
