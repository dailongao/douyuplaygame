import win32api,win32gui,win32con
import time
import virtual_key_map, scancode_map

def list_child(hwnd, lParam):
	global first_child
	first_child = hwnd
	return False
	
def control_init():
	title='No$gba Emulator '
	hwnd = win32gui.FindWindow(None, title)
	first_child = None

	try:
		win32gui.EnumChildWindows(hwnd, list_child, 0)
	except:
		print("control_init() ok")
		
def sendkey(key):
	global first_child
	vkeycode = virtual_key_map.virtual_key(key)
	skeycode = scancode_map.scancode(key)
	downkey = (skeycode << 16) + 1
	upkey = 0xC0000000 + (skeycode << 16) + 1
	win32api.PostMessage(first_child, win32con.WM_KEYDOWN, vkeycode, downkey);
	time.sleep(0.05)
	win32api.PostMessage(first_child, win32con.WM_KEYUP, vkeycode, upkey)