# -*- coding: utf-8 -*-  

import chat
import control
import parse

def new_query(msg):
	res = parse.getinfo(msg)
	opt = res[0]
	vaildopt = None
	if(opt == '上'):
		control.sendkey('w')
		vaildopt = True
	elif(opt == '下'):
		control.sendkey('s')
		vaildopt = True
	elif(opt == '左'):
		control.sendkey('a')
		vaildopt = True
	elif(opt == '右'):
		control.sendkey('d')
		vaildopt = True
	elif(opt == 'A'):
		control.sendkey('z')
		vaildopt = True
	elif(opt == 'B'):
		control.sendkey('x')
		vaildopt = True
	elif(opt == '开始'):
		control.sendkey('c')
		vaildopt = True
	elif(opt == '选择'):
		control.sendkey('v')
		vaildopt = True
	else:
		vaildopt = False
	if(vaildopt == True):
		print(res[1] + ": " + opt.decode('utf-8'))

# setting
chatroom_id = 620

# init
control.control_init()
chat.start_chat(chatroom_id, new_query)