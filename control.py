import win32api,win32gui,win32con,win32com,win32com.client
import time
import virtual_key_map, scancode_map

def list_child(hwnd, lParam):
	global first_child
	first_child = hwnd
	return False
	
def control_init(title = 'No$gba Emulator '):
	global shell
	shell = win32com.client.Dispatch('WScript.Shell')

	hwnd = win32gui.FindWindow(None, title)
	first_child = None

	try:
		win32gui.EnumChildWindows(hwnd, list_child, 0)
	except:
		print("control_init() ok")
		
#def sendkey(key,pdelay = 0.05, rdelay = 0.05):
def sendkey_old(key,pdelay = 0.05, rdelay = 0.05):
	global first_child
	vkeycode = virtual_key_map.virtual_key(key)
	skeycode = scancode_map.scancode(key)
	downkey = (skeycode << 16) + 1
	upkey = 0xC0000000 + (skeycode << 16) + 1
	win32api.PostMessage(first_child, win32con.WM_KEYDOWN, vkeycode, downkey);
	time.sleep(pdelay)
	win32api.PostMessage(first_child, win32con.WM_KEYUP, vkeycode, upkey)
	time.sleep(rdelay)

def sendkey(key,pdelay = 0.05, rdelay = 0.05):
	#shell = win32com.client.Dispatch('WScript.Shell')
	shell.SendKeys("ZZZZZ", 0)

if __name__ == '__main__':
	
	shell.Run('notepad')
	time.sleep(0.1)
	shell.AppActivate('notepad')
	shell.SendKeys("Hello World", 0)
	shell.SendKeys("Z", 0)
	shell.SendKeys("{F5}", 0)   # F5 prints the time/date