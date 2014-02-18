# -*- coding: utf-8 -*-  

import chat
import control
import parse

def try_opt(opt):
	vaildopt = False
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
	return vaildopt

def new_query(msg):
	try:
		MAX_OPT_N=16
		count = 1
		
		res = parse.getinfo(msg)
		opt_str = res[0]

		# check long operation
		if (opt_str == 'START') or (opt_str == 'SELECT'):
			vflag = try_opt(opt_str)
			if(vflag == True):
				print(res[1].decode('utf-8') + ": " + opt.decode('utf-8')), count
			else:
				return
			return

		# check single char operation
		opt_list = list(res[0])
		print opt_list
		first_opt = opt_list[0]
		print 'first is', first_opt
		
		for opt in opt_list:	
			print 'loop', opt
			if not(opt == first_opt):
				return
			if(count>MAX_OPT_N):
				return

			#print opt
			try:
				vflag = try_opt(opt)
			except:
				return
			
			#	
			if(vflag == True):
				print(res[1].decode('utf-8') + ": " + opt.decode('utf-8')), count
			else:
				return

			count = count + 1
	except:
		return

# setting
chatroom_id = 6032

# init
control.control_init()
chat.start_chat(chatroom_id, new_query)
