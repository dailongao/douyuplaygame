from win32api import *
from win32gui import *
from win32con import *

WND_CLASS_NAME = 'GUIWndClass'
WND_TITLE = 'Title'

g_hWnd = 0

message_map = {
	
}

def guiWndProc(hwnd,message,wparam,lparam):
	return

def guiRegisterClass(hIns):
	wc = WNDCLASS()
	wc.style = CS_HREDRAW | CS_VREDRAW
	wc.lpfnWndProc = message_map
	wc.lpszClassName = WND_CLASS_NAME

	return RegisterClass(wc)


def guiInitInstance(hIns):
	global g_hWnd
	g_hWnd = CreateWindow(
		WND_CLASS_NAME,
		WND_TITLE,
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,0,CW_USEDEFAULT,0,
		0,0,hIns,None)

	ShowWindow(g_hWnd, SW_SHOW)
	UpdateWindow(g_hWnd)


def wmain():
	
	hIns = GetModuleHandle(None)
	guiRegisterClass(hIns)
	guiInitInstance(hIns)

	while True:
		b, msg = GetMessage(0, 0, 0)
		print b,msg
		if not b:
			break;
		TranslateMessage(msg)
		DispatchMessage(msg)
		
	return

if __name__ == '__main__':
	wmain()
	

