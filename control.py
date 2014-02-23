import win32api,win32gui,win32con
import time
import virtual_key_map, scancode_map

#def list_child(hwnd, lParam):
#	global first_child
#	print 'list_child',hwnd
#	first_child = hwnd
#	return False
	
def control_init(title = 'No$gba Emulator '):
	global g_hwnd
	
	print title.decode('utf-8')
	g_hwnd = win32gui.FindWindow(None, title.decode('utf-8'))
	
		
def sendkey(key,pdelay = 0.05, rdelay = 0.05):
	vkeycode = virtual_key_map.virtual_key(key)
	skeycode = scancode_map.scancode(key)
	print vkeycode,skeycode

	if key == 'UPARROW' or key == 'DOWNARROW' or key == 'LEFTARROW' or key=='RIGHTARROW':
		print 'EXTENDED KEY'
		downkey = (skeycode << 16) + 1 + (1<<24)
		upkey = 0xC0000000 + (skeycode << 16) + 1 + (1<<24)
		win32api.PostMessage(g_hwnd, win32con.WM_KEYDOWN, vkeycode, downkey);
		time.sleep(pdelay)
		win32api.PostMessage(g_hwnd, win32con.WM_KEYUP, vkeycode, upkey)
		time.sleep(rdelay)
	else:
		downkey = (skeycode << 16) + 1
		upkey = 0xC0000000 + (skeycode << 16) + 1
		win32api.PostMessage(g_hwnd, win32con.WM_KEYDOWN, vkeycode, downkey);
		time.sleep(pdelay)
		win32api.PostMessage(g_hwnd, win32con.WM_KEYUP, vkeycode, upkey)
		time.sleep(rdelay)