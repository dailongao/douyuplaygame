import win32api,win32gui,win32con
import time

def list_child(hwnd, lParam):
	global first_child
	first_child = hwnd
	return False
  
title='No$gba Emulator '
hwnd = win32gui.FindWindow(None, title)
print(hwnd)
first_child = None
print(first_child)

try:
	win32gui.EnumChildWindows(hwnd, list_child, 0)
except:
	print "hehe"

print(first_child)

#send key  
win32api.PostMessage(first_child, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0x00390001)
time.sleep(0.05)
win32api.PostMessage(first_child, win32con.WM_KEYUP, win32con.VK_SPACE, 0xC0390001)  

#win32api.PostMessage(first_child, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
#time.sleep(0.05)
#win32api.PostMessage(first_child, win32con.WM_KEYUP, win32con.VK_SPACE, 0)  
