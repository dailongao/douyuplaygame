# -*- coding: utf-8 -*-  

import chat
import control
import parse

def new_query(msg):
	res = parse.getinfo(msg)
	opt = res[0]
	vaildopt = None
	if(opt == 'U'):
		control.sendkey('w')
		vaildopt = True
	elif(opt == 'D'):
		control.sendkey('s')
		vaildopt = True
	elif(opt == 'L'):
		control.sendkey('a')
		vaildopt = True
	elif(opt == 'R'):
		control.sendkey('d')
		vaildopt = True
	elif(opt == 'A'):
		control.sendkey('z')
		vaildopt = True
	elif(opt == 'B'):
		control.sendkey('e')
		vaildopt = True
	elif(opt == 'START'):
		control.sendkey('c')
		vaildopt = True
	elif(opt == 'SELECT'):
		control.sendkey('v')
		vaildopt = True
	else:
		vaildopt = False
	if(vaildopt == True):
		try:
			print(res[1].decode('utf-8') + ": " + opt.decode('utf-8'))
		except:
			print('error in print message')

# setting
chatroom_id = 620

# init
control.control_init()
chat.start_chat(chatroom_id, new_query)